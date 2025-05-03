# SENTINEL: Sign Enabled Navigation with Traffic Interaction and Effective Learning

SENTINEL is an end-to-end autonomous robotic system that combines real-time obstacle detection with traffic sign recognition for intelligent decision-making and navigation. Built entirely from scratch using Raspberry Pi, custom sensor logic, and deep learning models, SENTINEL adapts to dynamic environments and follows road-like rules using visual cues and distance awareness.

## 🚗 Key Features

- Real-time obstacle avoidance using ultrasonic sensors (front, left, right, back)
- Traffic sign recognition using YOLOv5-Lite (Turn Left, Turn Right, Stop, Honk)
- Decision mapping engine to fuse sensor + sign input and determine next action
- Directional motor control logic with safe-distance thresholds
- Modular Python-based control architecture built from scratch
- SPI-based TFT display integration for live feedback (optional)
- Clean GPIO and I2C handling without relying on external libraries

## 🧰 Technologies Used

- Python (modular scripts for movement, sensing, and sign response)
- YOLOv5-Lite (PyTorch-based traffic sign detection)
- GPIOZero for GPIO control
- Custom sensor logic using ultrasonic range finders
- I2C for motor driver communication
- SPI for optional TFT display
- Raspberry Pi 5

## 🧠 How It Works

1. **Ultrasonic Sensing:**  
   Sensors monitor object proximity in multiple directions. Distance thresholds are tuned for safe stopping and turning decisions.

2. **Traffic Sign Detection:**  
   A Pi camera streams frames to a YOLOv5-Lite model that detects traffic signs in real time.

3. **Decision Logic:**  
   The system prioritizes obstacles and then adjusts motion based on sign recognition — e.g., turns only when clear and sign says so.

4. **Motor Control:**  
   Movement commands (forward, left, right, stop) are executed via I2C-based motor driver communication.

## 🔗 Traffic Sign Detection Module

This project builds on the traffic sign recognition model developed in [Traffic-Sign-Detection-YOLOv5Lite-Rohit](https://github.com/yourusername/Traffic-Sign-Detection-YOLOv5Lite-Rohit), which includes model training, inference code, and label mapping. SENTINEL integrates this module for real-time sign-based navigation decisions.


