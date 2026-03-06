Project Overview

This project is an AI-based Warehouse Monitoring System that counts bags being loaded into trucks and unloaded from trucks using computer vision.
The system detects workers carrying bags and counts them when they cross a virtual line between the warehouse and truck area.
A dashboard interface is created using Streamlit to display:

Live camera video
Bags In count
Bags Out count
Dummy IoT parameters

This project was developed as part of an AI internship assignment.

Features:

Real-time bag counting from video
Detects workers carrying bags
Counts Loading (Warehouse → Truck)
Counts Unloading (Truck → Warehouse)
Dashboard view for monitoring
Dummy IoT warehouse parameters

Technologies Used:

Python
OpenCV
YOLOv8 Object Detection
Streamlit Dashboard

Project Structure
warehouse-bag-counting-system
│
├── app.py            # Streamlit dashboard
├── bag_counter.py    # Bag counting logic
├── video.mp4         # Sample test video
├── requirements.txt  # Python libraries
└── README.md

Installation
git clone https://github.com/Avinash7084/warehouse-bag-counting-system.git

Go to project folder:
cd warehouse-bag-counting-system

Install required libraries:
pip install -r requirements.txt

Start the dashboard:
streamlit run app.py
