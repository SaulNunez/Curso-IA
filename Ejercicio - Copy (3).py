import numpy as np 
import cv2

img = np.zeros((512,512, 3), np.uint8)
circulos = int(input('Cuantos circulos habra?'))
magnitud = int(input('Y su magnitud?'))

color = (0, 255, 0)
punto_inicial = (256, 256)

for i in range(circulos):
    magnitud += 15
    if i % 3 == 0:
        color = (255, 0, 0)
    elif i % 3 == 1:
        color = (0, 255, 0)
    else:
        color = (0, 0, 255)
    cv2.circle(img, punto_inicial, magnitud, color, 2)

cv2.imshow('Image', img)
cv2.waitKey()