import cv2
import mediapipe as mp
import pyautogui

x1=0
y1=0
x2=0
y2=0
webcam= cv2.VideoCapture(0)
my_hands =  mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    _, image=webcam.read()
    image = cv2.flip(image, 1)  # Mirror image for better UX
    rgb= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = my_hands.process(rgb)
    hands = results.multi_hand_landmarks
    overlay = image.copy()  # For transparent drawings

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(overlay, hand, 
                mp.solutions.hands.HAND_CONNECTIONS,
                drawing_utils.DrawingSpec(color=(0, 150, 250), thickness=2, circle_radius=4),
                drawing_utils.DrawingSpec(color=(250, 150, 0), thickness=2))

            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x= int(landmark.x * image.shape[1])
                y= int(landmark.y * image.shape[0])
                if id==8:
                    cv2.circle(overlay, center=(x,y), radius=10, color=(0,255,255), thickness=-1)
                    x1=x
                    y1=y
                if id==4:
                    cv2.circle(overlay, center=(x,y), radius=10, color=(0,0,255), thickness=-1)
                    x2=x
                    y2=y
        
        cv2.line(overlay, (x1, y1), (x2, y2), (255, 255, 0), 3)
        distance = int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        if distance>50:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")
        # Add a filled rectangle at the top as a background for text
        cv2.rectangle(overlay, (0,0), (image.shape[1], 40), (0,0,0,50), -1)

        # Display distance value and volume direction
        text = f"Distance: {distance} | " + ("Volume Up" if distance>50 else "Volume Down")
        color = (0,255,0) if distance>50 else (0,0,255)
        cv2.putText(overlay, text, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # Draw distance bar
        bar_x = 10
        bar_y = image.shape[0] - 30
        bar_width = min(distance*2, 300)  # cap width for aesthetics
        cv2.rectangle(overlay, (bar_x, bar_y), (bar_x + bar_width, bar_y + 20), color, -1)

    # Blend overlay with original image
    alpha = 0.7
    image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

    cv2.imshow("Hand Volume Control", image)
    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' to exit
        break

webcam.release()
cv2.destroyAllWindows()
