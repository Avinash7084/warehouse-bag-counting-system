import cv2
from ultralytics import YOLO

class BagCounter:
    def __init__(self, video_path):

        # open video
        self.cap = cv2.VideoCapture(video_path)

        # load YOLO model
        self.model = YOLO("yolov8n.pt")

        # position of vertical counting line
        self.line_position = 520

        # counters
        self.bags_loaded = 0
        self.bags_unloaded = 0

        # store last position of each person
        self.last_position = {}

        # store counted people so we don't count twice
        self.counted_people = set()

    def process_frame(self):

        ret, frame = self.cap.read()

        if not ret:
            return None, self.bags_loaded, self.bags_unloaded

        # detect and track persons
        results = self.model.track(frame, persist=True, classes=[0], conf=0.4, verbose=False)

        if results[0].boxes.id is not None:

            boxes = results[0].boxes.xywh.cpu()
            ids = results[0].boxes.id.int().cpu().tolist()

            for box, person_id in zip(boxes, ids):

                # center x position of person
                x = int(box[0])

                if person_id in self.last_position:

                    previous_x = self.last_position[person_id]

                    # moving right → left (Loading truck)
                    if previous_x > self.line_position and x <= self.line_position:

                        if person_id not in self.counted_people:
                            self.bags_loaded += 1
                            self.counted_people.add(person_id)

                    # moving left → right (Unloading truck)
                    elif previous_x < self.line_position and x >= self.line_position:

                        if person_id not in self.counted_people:
                            self.bags_unloaded += 1
                            self.counted_people.add(person_id)

                # update last position
                self.last_position[person_id] = x

                # draw bounding box
                x1 = int(box[0] - box[2] / 2)
                y1 = int(box[1] - box[3] / 2)
                x2 = int(box[0] + box[2] / 2)
                y2 = int(box[1] + box[3] / 2)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # draw red counting line
        cv2.line(frame,
                 (self.line_position, 0),
                 (self.line_position, frame.shape[0]),
                 (0, 0, 255),
                 3)

        return frame, self.bags_loaded, self.bags_unloaded