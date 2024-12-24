# Smart-Automation-using-Body-detection
Description:

This project is a smart solution aimed at optimizing energy consumption in classrooms by detecting occupancy and automatically controlling electrical appliances. The system employs a computer vision algorithm using the YOLOv8 model to detect the number of people in a classroom through a camera feed. The detected occupancy data is sent to a microcontroller (Arduino) via serial communication. Based on the data, the microcontroller turns appliances like lights, fans, or air conditioners on or off, ensuring efficient energy usage.

Technologies Used:
	•	Computer Vision: YOLOv8 for object detection.
	•	Microcontroller: Arduino for appliance control.
	•	Programming Languages: Python for the detection system and Arduino IDE for microcontroller programming.
	•	Communication Protocol: Serial communication between Python and Arduino.
