import cv2
from services.face_detector import FaceDetector
from services.motion_detector import MotionDetector


camera = cv2.VideoCapture(0)
face_detector = FaceDetector()
motion_detector = MotionDetector()
prev_frame = None
video_writer = None
recording = False
last_motion_found = None


while True:

    ret, frame = camera.read()
    fps = camera.get(cv2.CAP_PROP_FPS)

    if not ret:
        break

    frame = cv2.resize(frame, (620, 480))
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detect_faces(frame=gray)

    for (x, y, w, h) in faces:
        face_detector.draw_rectangles(frame=frame, x=x, y=y, w=w, h=h)

    if prev_frame is None:
        prev_frame = gray
        continue

    contours = motion_detector.detect_motions(prev_frame=prev_frame, curr_frame=gray)
    motion_detector.draw_rectangles(frame=frame, contours=contours, fps=fps)
    prev_frame = gray

    if cv2.waitKey(1) == ord("q"):
        break

    cv2.imshow("MiniSmartCamera", frame)
camera.release()
cv2.destroyAllWindows()