import numpy as np 
import cv2

img = np.zeros((512,512, 3), np.uint8)
lados = int(input('Cuantos lados tendra nuestra figura?'))
magnitud = int(input('Y su magnitud?'))
vueltas = int(input('Vueltas?'))

thicc = 2
color = (0, 255, 0)
punto_inicial = (256, 256)
angulo = 0
variacion= 1.075
punto_final= (int(punto_inicial[0] + magnitud * np.cos(angulo)), int(punto_inicial[1] + magnitud * np.sin(angulo)))
anguloEntreLineas = (vueltas * 360 / lados) * np.pi / 180

for i in range(lados):
    angulo += anguloEntreLineas
    magnitud *= variacion
    punto_inicial= punto_final
    punto_final= (int(punto_inicial[0] + magnitud * np.cos(angulo)), int(punto_inicial[1] + magnitud * np.sin(angulo)))
    if i % 2 == 0:
        color = (255, 0, 0)
    else:
        color = (0, 0, 255)
    cv2.line(img, punto_inicial, punto_final, color, thicc)

cv2.imshow('Image', img)
cv2.waitKey()