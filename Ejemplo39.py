import cv2

import numpy as np 
img = cv2. imread('images/ari.png')
img2 = cv2.imread('images/ojo.png')
cv2.imshow('ojo', img2)
cv2.imshow('imagen',img)
x,y,z = img.shape 
ojo = img2[0:110, 0:110]
cv2.imshow('ojo', ojo)
img[200:310, 390:500] = ojo
cv2.imshow('modificada', img)

cv2.waitKey(0)