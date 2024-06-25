import cv2
import threading
from hand_detector import HandDetector
from webcam_handler import WebcamHandler
from draw import Paint
from tkinter import *

class HandTracking:
    def __init__(self, paint_app):
        self.detector = HandDetector()
        self.webcam = WebcamHandler()
        self.pain_app = paint_app

    def run(self):
        while self.webcam.cap.isOpened():
            image = self.webcam.read_frame()
            if image is None:
                continue

            image.flags.writeable = False
            results = self.detector.process_image(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # print(hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y)

                    self.detector.move_cursor(hand_landmarks)
                    self.detector.handle_select(hand_landmarks)
                    # self.detector.handle_click(hand_landmarks)

            image = self.detector.draw_landmarks(image, results)

            cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

        self.webcam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    app = Paint(root)

    tracking = HandTracking(app)

    # Run hand tracking in a separate thread
    tracking_thread = threading.Thread(target=tracking.run)
    tracking_thread.daemon = True
    tracking_thread.start()

    root.mainloop()
