from bag_counter import BagCounter
import cv2

counter = BagCounter("video.mp4")

while True:

    frame, bags_in, bags_out = counter.process_frame()

    if frame is None:
        break

    cv2.putText(frame, f"Bags In: {bags_in}", (40,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, f"Bags Out: {bags_out}", (40,100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Bag Counter", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()