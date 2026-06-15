# 📷 Mini Smart Camera

A real-time smart surveillance system built using **Python** and **OpenCV** that can detect faces, identify motion, capture screenshots, and automatically record videos when activity is detected.

## 🚀 Overview

Mini Smart Camera is a computer vision project designed to enhance basic webcam monitoring by integrating face detection and motion detection capabilities. The system continuously analyzes webcam footage and automatically performs actions such as capturing screenshots and recording videos whenever suspicious activity is detected.

This project demonstrates practical applications of **Computer Vision**, **Image Processing**, and **Automation** using OpenCV.

---

## ✨ Features

* 🎥 Real-time webcam video streaming
* 👤 Face detection using Haar Cascade Classifier
* 🚶 Motion detection using frame differencing
* 📸 Automatic screenshot capture when a face is detected
* 🎬 Automatic video recording when motion is detected
* 🟩 Bounding box visualization for detected objects
* 📂 Modular and maintainable project structure

---

## 🛠️ Tech Stack

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| Python     | Core Programming Language          |
| OpenCV     | Computer Vision & Image Processing |

---

## 📁 Project Structure

```text
mini-smart-camera/
│
├── main.py
├── README.md
├── requirements.txt
│
└── services/
    ├── face_detector.py
    └── motion_detector.py
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mini-smart-camera.git
cd mini-smart-camera
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application using:

```bash
python main.py
```

The webcam will start automatically and the system will:

* Detect faces in real time
* Detect motion in the frame
* Save screenshots when faces are detected
* Record videos when motion is detected

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

* Computer Vision fundamentals
* OpenCV image processing techniques
* Face detection algorithms
* Motion detection systems
* Real-time video stream processing
* Python project structuring

---

## 🔮 Future Improvements

* Deep Learning based face recognition
* Intruder alert notifications
* Email/SMS alerts
* Cloud storage integration
* Multi-camera support
* Object detection using YOLO

---

## 👨‍💻 Author

**Sumanth Yadla**

AI & Data Science Student | Python Developer | Computer Vision Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
