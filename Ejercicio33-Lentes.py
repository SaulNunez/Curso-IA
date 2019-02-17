import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(
    'C:\\Users\\sauln\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\\haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier(
    'C:\\Users\\sauln\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\\haarcascade_eye.xml')
if face_cascade.empty():
    raise IOError('No se puede cargar el clasificador de caras')
if eye_cascade.empty():
    raise IOError('No se puede cargar el clasificador de ojos')
cap = cv2.VideoCapture(0)
sunglasses_img= cv2.imread('./images/glasses.png')

while True:
    ret, frame = cap.read()
    frame =  cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    vh, vw =  frame.shape[:2]
    vh, vw = int(vh), int(vw)
    gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=1)
    centers=[]
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes =  eye_cascade.detectMultiScale(roi_gray)
        for(x_eye, y_eye, w_eye, h_eye) in eyes:
            centers.append((x + int(x_eye + 0.5 * w_eye), y + int(y_eye + 0.5 * h_eye)))
    if len(centers) > 1:
        h, w = sunglasses_img.shape[:2]
        eye_distance = abs(centers[1][0] - centers[0][0])
        sunglasses_width = 2.12 * eye_distance
        scaling_factor = sunglasses_width / w
        print(scaling_factor, eye_distance)
        overlay_sunglasses = cv2.resize(sunglasses_img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        x = centers[0][0] if centers[0][0] < centers[1][0] else centers[1][0]
        x -= int(0.26 * overlay_sunglasses.shape[1])
        y += int(0.26 * overlay_sunglasses.shape[0])
        h, w = overlay_sunglasses.shape[:2]
        h,w = int(h), int(w)
        frame_roi = frame[y:y+h, x:x+w]
        gray_overlay_sunglasses =  cv2.cvtColor(overlay_sunglasses, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(gray_overlay_sunglasses, 180, 255, cv2.THRESH_BINARY_INV)
        mask_inv = cv2.bitwise_not(mask)
        try: 
            masked_face = cv2.bitwise_and(overlay_sunglasses, overlay_sunglasses, mask=mask)
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)
            frame[y:y+h, x:x+w] = cv2.add(masked_face, masked_frame)
        except cv2.error as e:
            print('Ignorando excepciones aritmeticas: ' + str(e))
        
    else:
        print('Eyes not detected')
    cv2.imshow('Eye Detector', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()