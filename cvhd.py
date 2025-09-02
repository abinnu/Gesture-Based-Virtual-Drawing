"""
Created on Tue Apr  1 17:50:54 2025

@author: abinn
"""
import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)
canvas = np.zeros((480, 640, 3), dtype=np.uint8)
prev_x, prev_y = 0, 0
clear_canvas = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            index_finger_tip = hand_landmarks.landmark[8]
            h, w, _ = frame.shape
            x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y
            thumb_tip = hand_landmarks.landmark[4]
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            distance = np.hypot(x - thumb_x, y - thumb_y)
            if distance < 40:
                clear_canvas = True
            else:
                clear_canvas = False

            if clear_canvas:
                canvas = np.zeros_like(canvas)  
            else:
                cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 0, 255), 5)
            
            prev_x, prev_y = x, y
            
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0) 
    cv2.imshow("Virtual Drawing", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()