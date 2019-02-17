import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(
    'C:\\Users\\sauln\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\\haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

scaling_factor = 0.5
while True:
    ret, frame = cap.read()
    face_rects = face_cascade.detectMultiScale(
        frame, scaleFactor=1.3, minNeighbors=3)
    for(x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (227, 11, 92), 10)
        cv2.imshow('Face Detector', frame)
        c = cv2.waitKey(1)
        if c == 27:
            break
cap.release()
cv2.destroyAllWindows()
