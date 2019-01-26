import cv2

img = cv2.imread('./images/input.jpg')
img_scaled = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_LINEAR)
# Imagen, tamano imagen de salida none=default
# fx= Factor de escala en el eje x, fy en y
# Metodo de interpolacion
cv2.imshow('Imagen original', img)
print(img.shape[:2])
cv2.imshow('Scaling - Linear Interpolation', img_scaled)
img_scaled=cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', img_scaled)

img_scaled=cv2.resize(img, (450,400), interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling - tamano sesgado', img_scaled)
img_scaled=cv2.resize(img, (450,200), interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling - tamano sesgado2', img_scaled)
print(img_scaled.shape[:2])
cv2.waitKey()
