# 🎯 Real-Time Object Detection & Direction Tracking

This project uses **OpenCV** and **HSV color filtering** to detect and track colored objects in real time using a webcam. It also provides direction feedback like **Left**, **Right**, or **Stop** based on the object’s position and distance from the camera.

---

## 🧪 Tools Used

- Python  
- OpenCV  
- imutils  
- Webcam  

---

## 📊 Sample Output

**Input:**  
Live webcam feed detecting a red-colored object  
**Output:**  
Overlayed tracking circle + Direction text (e.g., `Direction: Right`)  

---

## 🚀 How to Run

1. Run `object_detection.py` to calibrate HSV values using sliders
2. Adjust HSV until the object is correctly highlighted in the **Mask**
3. Update those HSV values in `object_detection_output.py`
4. Run `object_detection_output.py` to track object and view direction output
5. Press `q` to quit the window

---

## 📈 Key Concepts

- HSV color space filtering  
- Real-time webcam feed processing  
- Noise reduction (blurring, erosion, dilation)  
- Contour detection and shape tracking  
- Direction logic based on object size and position

---
