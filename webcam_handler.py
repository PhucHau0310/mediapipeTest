import cv2

class WebcamHandler:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def read_frame(self):
        success, image = self.cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            return None
        return image

    def release(self):
        self.cap.release()