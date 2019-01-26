import cv2
import numpy as np

img = cv2.imread('images/input.jpg')
num_rows, num_cols = img.shape[:2]
print('Dimensiones de la imagen \n',
      'renglones ', num_rows,'\n', 'columnas ', num_cols,'\n')
translation_matrix = np.float32([[1,0,100], [0,1,110]]) # La imagen se translada 100, 110
print('Matriz de translacion', translation_matrix)
img_translation=  cv2.warpAffine(img, translation_matrix, (num_cols+100, num_rows+110))
cv2.imshow('Contenedor de la imagen', img_translation)
translation_matrix= np.float32([[1,0,-30], [0,1,-30]]) # La imagen se translada -30, -30
print('Matriz de translacion', translation_matrix)
img_translation=  cv2.warpAffine(img, translation_matrix, (num_cols+100+30, num_rows+110+50))

cv2.imshow('Original', img)
cv2.imshow('Translation', img_translation)
renglones, columnas = img_translation.shape[:2]
print('Dimensiones', renglones, columnas)
cv2.waitKey()
