# Mini Smart Camera

A real-time computer vision based smart surveillance system built using Python and OpenCV.

This project can:
- Detect faces
- Detect motion
- Capture screenshots when faces are detected
- Record videos automatically when motion is detected

---

# Features

- Real-time webcam streaming
- Face detection using Haar Cascade
- Motion detection using frame differencing
- Automatic screenshot capture
- Automatic video recording on motion detection
- Bounding box visualization
- Modular project structure

---

# Tech Stack

- Python
- OpenCV

---

# Project Structure

```bash
mini-smart-camera/
│
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
│
└── services
    ├── face_detector.py
    └── motion_detector.py