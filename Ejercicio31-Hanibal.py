import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(
    'C:\\Users\\sauln\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\\haarcascade_frontalface_alt.xml')
face_mask = cv2.imread('./images/mask.png')
h_mask, w_mask = face_mask.shape[:2]

print('mascara', h_mask, w_mask)
if face_cascade.empty():
    raise IOError('No se pudo cargar clasificador de caras')
cap = cv2.VideoCapture(0)
scaling_factor = 0.5
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor,
                       fy=scaling_factor, interpolation=cv2.INTER_LINEAR)
    face_rects = face_cascade.detectMultiScale(
        frame, scaleFactor=1.3, minNeighbors=3)
    print(face_rects)
    for(x, y, w, h) in face_rects:
        if h <= 0 or w <= 0:
            pass
        h, w = int(1.0*h), int(1.0*w)
        y -= int(-0.2*h)
        x = int(x)

        frame_roi = frame[y:y+h, x:x+w]
        face_mask_small = cv2.resize(
            face_mask, (w, h), interpolation=cv2.INTER_LINEAR)
        gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(gray_mask, 180, 255, cv2.THRESH_BINARY_INV)
        mask_inv = cv2.bitwise_not(mask)
        try:
            masked_face = cv2.bitwise_and(
                face_mask_small, face_mask_small, mask=mask)
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)
            frame[y:y+h, x:x+w] = cv2.add(masked_face, masked_frame)
        except cv2.error as e:
            print('Ignorando excepciones aritmeticas: ' + str(e))
        cv2.imshow('Detector de caras', frame)
        c = cv2.waitKey(1)
        if c == 27:
            break
cap.release()
cv2.destroyAllWindows()
