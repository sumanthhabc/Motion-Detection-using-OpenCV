import cv2
import os
from datetime import datetime




class FaceDetector:


    def __init__(self):
        
        os.makedirs("outputs/detected_faces", exist_ok=True)
        self.face_detection_model = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )


    def detect_faces(self, frame):

        faces = self.face_detection_model.detectMultiScale(
            frame,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (50,50)
        )
        if len(faces) > 0:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"outputs/detected_faces/face_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
        return faces
    

    def draw_rectangles(self, frame, x, y, w, h):

        cv2.rectangle(
            frame,
            (x,y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )
