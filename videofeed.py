import mediapipe as mp
import numpy as np
import cv2 as cv

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
 
cap = cv.VideoCapture("./data/infantvideo.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    cv.imshow('Mediapipe Feed', frame)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # cv.imshow('frame',gray)
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()