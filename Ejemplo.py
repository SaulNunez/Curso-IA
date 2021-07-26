import cv2

motorcicle = cv2.imread('./images/motocicleta.jpg')
rows, cols = motorcicle.shape[:2]

cv2.imshow('origen', motorcicle)
for i in range(rows):
    for j in range(cols):
        motorcicle[i,j][2] = 0
        motorcicle[i,j][1] = 0

cv2.imshow('modificada', motorcicle)
cv2.waitKey(0)