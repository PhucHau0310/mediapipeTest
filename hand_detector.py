import mediapipe as mp
import cv2
import pydirectinput

class HandDetector:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)

    def process_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return self.hands.process(image)

    def draw_landmarks(self, image, results):
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style())
        return image

    def move_cursor(self, hand_landmarks):
        x = hand_landmarks.landmark[8].x
        y = hand_landmarks.landmark[8].y
        pydirectinput.moveTo(int((0.5 - x) * 1920), int(y * 1080))

    def handle_select(self, hand_landmarks):
        if (hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y
            and hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y
            and hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y
        ):
            pydirectinput.mouseDown()
        else:
            pydirectinput.mouseUp()
