import cv2
import os
import time
from datetime import datetime




class MotionDetector:


    def __init__(self):
        
        os.makedirs("outputs/detected_motions", exist_ok=True)
        self.recording = False
        self.video_writer = None
        self.last_motion_time = None


    def detect_motions(self, prev_frame, curr_frame):

        prev_frame = cv2.GaussianBlur(prev_frame, (31, 31), 0)
        curr_frame = cv2.GaussianBlur(curr_frame, (31, 31), 0)

        diff = cv2.absdiff(prev_frame, curr_frame)

        _, thresh = cv2.threshold(
            diff,
            25,
            255,
            cv2.THRESH_BINARY
        )

        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        return contours
    

    def draw_rectangles(self, frame, contours, fps:float):

        fps = fps if fps and fps > 0 else 20.0

        for contour in contours:

            if cv2.contourArea(contour)<1000:
                continue

            motion_found = True

            x, y ,w ,h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x,y),
                (x+w, y+h),
                (0, 0, 255),
                2
            )

            self.record_frame(frame=frame, motion_found=motion_found, fps=fps)

    
    def record_frame(self, frame, motion_found:bool, fps:float=20.0):

        if motion_found:

            self.last_motion_time = time.time()
            if not self.recording:
            
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"outputs/detected_motions/motion_{timestamp}.mp4"
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                self.video_writer = cv2.VideoWriter(
                    filename,
                    fourcc,
                    fps,
                    (frame.shape[1], frame.shape[0])
                )
                self.recording = True
                print("recording...")

            if self.recording:

                self.video_writer.write(frame)
                if time.time() - self.last_motion_time > 5:

                    self.recording = False
                    self.video_writer.release()
                    self.video_writer = None
                    print("recording stopped")
