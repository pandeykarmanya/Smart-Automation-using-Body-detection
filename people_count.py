import serial
import time
from ultralytics import YOLO
import cv2
import numpy as np

# Initialize serial communication with Arduino
try:
    arduino = serial.Serial(port='/dev/cu.usbserial-120', baudrate=9600, timeout=1)  # Replace 'COM3' with your Arduino port
    time.sleep(2)  # Wait for the connection to initialize
    print("Serial communication established.")
except Exception as e:
    print(f"Error initializing serial communication: {e}")
    arduino = None  # Proceed without Arduino if connection fails

def send_integer_to_arduino(value):
    """Send an integer value to Arduino via serial."""
    if arduino is not None:
        try:
            arduino.write(f"{value}\n".encode())  # Send integer as a string followed by a newline
            print(f"Sent to Arduino: {value}")
        except Exception as e:
            print(f"Error sending data to Arduino: {e}")

# Load the YOLOv8 model pre-trained on COCO (you can replace this with a custom model if needed)
model = YOLO("yolov8n.pt")  # Replace 'yolov8n.pt' with your specific YOLOv8 model path

# Start video capture from the laptop's camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 'q' to exit.")

# Initialize a list to store people count values across frames
people_counts = []

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Perform inference on the frame
    results = model(frame)  # Inference on the frame, returns a list of Results objects

    # Initialize people count for this frame
    people_count = 0

    # Iterate over the list of results (though there should only be one result here)
    for result in results:
        # Access the detected boxes
        boxes = result.boxes  # This contains the bounding boxes for all detected objects

        # Filter for "person" detections
        detections = boxes[boxes.cls == 0]  # Class 0 is "person" in COCO dataset
        people_count = len(detections)

        # Draw bounding boxes for detected persons
        for box in detections:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get coordinates of the bounding box
            confidence = box.conf[0]  # Confidence score
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"Person {confidence:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Store the people count for smoothing
    people_counts.append(people_count)

    # Limit the size of the list to the last 10 frames for smoothing
    if len(people_counts) > 10:
        people_counts.pop(0)

    # Calculate the smoothed count (average of the last 10 frames)
    smoothed_count = int(np.mean(people_counts))

    # Send smoothed count to Arduino
    send_integer_to_arduino(smoothed_count)

    # Display the smoothed people count on the frame
    cv2.putText(frame, f"People Count: {smoothed_count}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("People Counter", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Close the serial connection when done
if arduino is not None:
    arduino.close()
    print("Serial communication closed.")