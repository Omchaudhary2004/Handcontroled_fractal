# Handcontroled_fractal

# 🌿 Fern Fractal Hand-Controlled Visualization

This project creates an **interactive Barnsley Fern fractal**, where the fractal dynamically changes based on the distance between your **thumb** and **index finger**, detected in real-time using your webcam and **OpenCV + MediaPipe Hands**.

---

## 📂 Project Structure

fern-fractal-hand-control/
├── handstrackingmodule.py # Handles hand tracking using MediaPipe
├── fractal.py # Generates and animates the fern fractal
├── scale_sender.py # Detects finger distance and sends scale values
└── README.md


## 🎯 Features

- 🖐️ Real-time hand landmark detection using MediaPipe
- 🌿 Dynamic Barnsley fern fractal generation using Matplotlib
- 🔗 Real-time communication between hand detection and fractal animation via sockets
- 📏 Distance between thumb and index finger mapped to fractal's scale
- 🎨 Hypnotic, continuously changing fractal animation

---

## 🚀 How It Works

1. **fractal.py**  
   - Starts a socket server on **localhost:5001**
   - Generates and displays the fern fractal using Matplotlib
   - Continuously updates the fractal scale based on received data

2. **scale_sender.py**  
   - Captures your hand using OpenCV and MediaPipe
   - Measures the distance between the thumb and index finger
   - Sends the calculated scale factor to the `fractal.py` server

3. **handstrackingmodule.py**  
   - A helper class for hand detection and landmark extraction using MediaPipe

---

## ⚙️ Installation

Install the required libraries:

```bash
pip install opencv-python mediapipe matplotlib numpy
```
🛠️ Usage
1. Start the Fractal Animation
Run the following command to start the fractal server and animation:

```bash
Copy
Edit
python fractal.py
```
This will open a window displaying the fern fractal and start listening for scale updates.

2. Start the Hand Detection and Scale Sender
Run this in another terminal window:

```bash
python scale_sender.py
```
This will activate your webcam and send scaling values to the fractal animation based on the distance between your thumb and index finger.

3. Stop the Programs
Press Ctrl + C in the terminal OR close the visualization and OpenCV windows.

🔍 Hand Control Mapping
Gesture	Effect on Fractal
Fingers close together	Fern shrinks
Fingers far apart	Fern expands

The finger distance (measured in pixels) is mapped from 50 - 300 pixels → scale 0.5 - 1.0.

🧠 Concepts Used
Barnsley Fern Fractal: An iterative fractal generation algorithm

MediaPipe Hands: Google’s real-time hand tracking API

OpenCV: For webcam input and drawing landmarks

Sockets: To send scaling data between processes

Matplotlib: For rendering the animated fractal

🔗 Future Improvements
Add dynamic color schemes for a more psychedelic effect

Smoothen scaling transitions using filters

Add support for multi-hand or gesture-based fractal type switching

Deploy as a web app using Flask & WebSockets
