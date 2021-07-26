import cv2
import numpy as np

cancha = np.zeros((400, 600, 3), dtype=np.uint8)
messi = cv2.imread('images/messi.png')
balon = messi[240:276, 280:330]
mask = np.zeros((36,50,3), dtype=np.uint8)
cv2.circle(mask,(int(balon.shape[0] /2), int(balon.shape[1] /2)), int(balon.shape[0] /2) , (255,255,255), -1)
final = np.zeros((36,50,3), dtype=np.uint8)
for i in range(balon.shape[0]):
    for j in range(balon.shape[1]):
        if mask[i, j].all() == False:
            final[i, j] = (0,0,0)
        else:
            final[i, j] = balon[i,j]
cv2.imshow('pong', cancha)
cv2.imshow('messi', messi)
cv2.imshow('balon', final)
cv2.imwrite('pelota.jpg', final)
cv2.waitKey()
