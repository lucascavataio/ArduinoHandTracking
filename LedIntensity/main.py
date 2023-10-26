import pyfirmata2
import time
import cv2
import mediapipe as mp
import math

# Initialize Arduino board and LED pin
board = pyfirmata2.Arduino('COM3')
targetLedPin = board.get_pin('d:10:p')
targetLedIntensity = 0

# Initialize video capture
videoCap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands
mpSolutionHands = mp.solutions.hands
uHands = mpSolutionHands.Hands()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0


# Function to calculate and display frames per second (FPS)
def displayFPS(_img):
    global cTime, pTime

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(_img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)


# Function to process hand landmarks and control LED intensity
def process_hands():
    _success, video_img = videoCap.read()
    img_rgb = cv2.cvtColor(video_img, cv2.COLOR_BGR2RGB)
    _videoResults = uHands.process(img_rgb)

    _handLandmarks = _videoResults.multi_hand_landmarks

    if _handLandmarks:
        for handLms in _handLandmarks:
            x4, y4, z4 = 0, 0, 0
            x8, y8, z8 = 0, 0, 0
            for id, lm in enumerate(handLms.landmark):
                if id == 4:
                    x4, y4, z4 = int(lm.x * video_img.shape[1]), int(lm.y * video_img.shape[0]), int(lm.z * 100)
                elif id == 8:
                    x8, y8, z8 = int(lm.x * video_img.shape[1]), int(lm.y * video_img.shape[0]), int(lm.z * 100)

            mpDraw.draw_landmarks(video_img, handLms, mpSolutionHands.HAND_CONNECTIONS)

            distance = math.sqrt((x8 - x4) ** 2 + (y8 - y4) ** 2 + (z8 - z4) ** 2)

            # Draw a line between lm 4 and lm 8
            cv2.line(video_img, (x8, y8), (x4, y4), (0, 255, 0), 2)  # Green line

            print(f'Distance between lm 4 and 8: {round(distance, 2)}')

            # Calculate targetLedIntensity as a normalized value between 0 and 1
            global targetLedIntensity

            targetLedIntensity = (distance - 20) / (300 - 20)

            # Ensure targetLedIntensity is within the 0 to 1 range
            targetLedIntensity = min(max(targetLedIntensity, 0), 1)

            targetLedIntensity = round(targetLedIntensity, 2)

            mpDraw.draw_landmarks(video_img, handLms, mpSolutionHands.HAND_CONNECTIONS)

    return video_img


# Main loop for capturing frames, processing hands, and updating LED
while True:
    img = process_hands()
    displayFPS(img)
    cv2.imshow("image", img)
    cv2.waitKey(1)
    targetLedPin.write(targetLedIntensity)
