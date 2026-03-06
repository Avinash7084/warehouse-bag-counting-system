import streamlit as st
import cv2
from bag_counter import BagCounter

# Page settings
st.set_page_config(page_title="Warehouse System", layout="wide")

# Title
st.title("Warehouse Management System")
st.subheader("Bag Counting Dashboard")

# Create 3 columns for cameras
cam1, cam2, cam3 = st.columns(3)

# Camera 1 Section
with cam1:
    st.write("Gate Number : 01")

    video_box = st.empty()   # place to show video
    bags_in_box = st.empty() # place to show bags in
    bags_out_box = st.empty()# place to show bags out

# Camera 2 and 3 (dummy cameras)
cam2.info("Camera 02 : Waiting for video...")
cam3.info("Camera 03 : Offline")

# IOT Sensor Section

st.markdown("---")
st.subheader("IOT Sensor Monitoring")

sensor1, sensor2 = st.columns(2)

with sensor1:
    st.write("Temperature : 30°C")
    st.write("Humidity : 65%")
    st.write("Gas Level : Normal")

with sensor2:
    st.write("Smoke/Fire : Safe")
    st.write("Gate Status : Open")


# Video Processing

# start bag counter
counter = BagCounter("video.mp4")

while True:

    frame, bags_in, bags_out = counter.process_frame()

    if frame is None:
        break

    # convert BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # show video
    video_box.image(frame, use_column_width=True)

    # show bag count
    bags_in_box.write(f"Bags In : {bags_in}")
    bags_out_box.write(f"Bags Out : {bags_out}")