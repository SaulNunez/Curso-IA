import cv2
import numpy as np

img = cv2.imread('images/input.jpg')
cv2.imshow('Original', img)

size = 15

#Generar el kernel
kernel_motion_blur = np.zeros((size, size))
print('Primer kernel\n', kernel_motion_blur)
kernel_motion_blur[int((size -1) / 2), :] = np.ones(size)
print('Segundo kernel\n', kernel_motion_blur)
kernel_motion_blur= kernel_motion_blur / size
print('Tercer kernel\n', kernel_motion_blur)
# Aplicando el kernel a la imagen original
output = cv2.filter2D(img, -1, kernel_motion_blur)

cv2.imshow('Motion Blur', output)
cv2.waitKey(0)