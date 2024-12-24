# Smart-Automation-using-Body-detection
# Description:

This project is a smart solution aimed at optimizing energy consumption in classrooms by detecting occupancy and automatically controlling electrical appliances. The system employs a computer vision algorithm using the YOLOv8 model to detect the number of people in a classroom through a camera feed. The detected occupancy data is sent to a microcontroller (Arduino) via serial communication. Based on the data, the microcontroller turns appliances like lights, fans, or air conditioners on or off, ensuring efficient energy usage.

## Technologies Used:

   •	Computer Vision: YOLOv8 for object detection.
   <br>
   •	Microcontroller: Arduino for appliance control.
   <br>
   •	Programming Languages: Python for the detection system and Arduino IDE for microcontroller programming.
   <br>
   •	Communication Protocol: Serial communication between Python and Arduino.

## Hardware:
   •	A computer with a working webcam.
   <br>
   •	An Arduino connected to your computer.
   <br>
   •	Electric appliances connected to Arduino for control (optional).
   
## Software:
   •	Python installed on your computer.
   <br>
   •	Required Python packages: serial, ultralytics, cv2, numpy.

# Setting Up the Environment
1.	Install Required Packages:
    <br>
        •       Run the following commands in your terminal or command prompt to install dependencies
  	<br>
    Command : pip install pyserial ultralytics opencv-python-headless numpy

2.	Connect the Arduino:
	<br>
	•	Ensure your Arduino is connected via USB.
        <br>
	•	Replace '/dev/cu.usbserial-120' in the code with the appropriate port for your 
                Arduino (e.g., COM3 for Windows).

3.	Prepare the YOLO Model:
	•	Ensure you have the YOLOv8 model file (yolov8n.pt).
                <br>
                Download it from the Ultralytics 
  	
4.	Configure the Code:
	•	Update the path to your YOLO model in the line
                <br>
                Command : model = YOLO("yolov8n.pt")

## Running the Code
1.	Start the Script:
   <br>
   Execute the script in your terminal:
  	<br>
   Command : python /path/to/people_count.py

2.	Control the Camera:
        <br>
	•	The script will start your default webcam.
        <br>
	•	Ensure the camera is functional and the area being monitored is visible.

3.	Interacting with Arduino:
	<br>
	•	The code sends the smoothed count of people detected in the frame to the Arduino via 
                serial communication.
  	<br>
	•	The Arduino can then use this data to control appliances (modify your Arduino sketch 
                to respond accordingly).

4. Key Features in the Code:
        <br>
   Object Detection:
        <br>
	•	Detects “person” objects using YOLOv8.
        <br>
	•	Filters detections to count people in the frame.
        <br>
   Smoothing:
        <br>
	•	Averages the count over the last 10 frames to reduce noise.
        <br>
   Arduino Communication:
        <br>
	•	Sends the smoothed count to Arduino using serial communication.
        <br>
   Real-Time Display:
        <br>
	•	Displays the video feed with bounding boxes for detected persons and the people count.

5. Stopping the Script:
	•	Press the q key to stop the program.
        <br>
	•	It will release the camera resources and close the Arduino serial connection.





