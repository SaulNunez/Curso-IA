import numpy as np 
import cv2

img = np.zeros((512,512, 3), np.uint8)
lados = 512
magnitud = 1024
angulo = 45 * np.pi / 180
thicc = 2
color = (0, 255, 0)
punto_inicial = (-512, 0)
punto_final= (int(punto_inicial[0] + magnitud * np.cos(angulo)), int(punto_inicial[1] + magnitud * np.sin(angulo)))

for i in range(lados):
    punto_inicial = (punto_inicial[0] + 10, punto_inicial[1])
    punto_final= (int(punto_final[0] + 10), int(punto_final[1]))
    if i % 3 == 0:
        color = (255, 0, 0)
    elif i % 3 == 1:
        color = (0, 255, 0)
    else:
        color = (0, 0, 255)
    cv2.line(img, punto_inicial, punto_final, color, thicc)

cv2.imshow('Image', img)
cv2.waitKey()