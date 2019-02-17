import cv2
import numpy as np

mouth_cascade = cv2.CascadeClassifier(
    'C:\\Users\\sauln\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\\haarcascade_mcs_mouth.xml')
if mouth_cascade.empty():
    raise IOError('No se puede cargar el clasificador de la boca')
cap = cv2.VideoCapture(0)

ds_factor = 0.5
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor,
                       fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mouth_rects = mouth_cascade.detectMultiScale(
        gray, scaleFactor=1.7, minNeighbors=11)
    for(x, y, w, h) in mouth_rects:
        y = int(y - 0.15 * h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (227, 11, 92), 10)

    cv2.imshow('Mouth Detector', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()
