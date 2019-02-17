import cv2
import numpy as np 

img = cv2.imread('images/green_dots.png')
output = cv2.medianBlur(img, ksize = 7)
cv2.imshow('Input', img)
cv2.imshow('Filtro de medianas', output)
cv2.waitKey()