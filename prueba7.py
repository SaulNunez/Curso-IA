import cv2
import numpy as np
img = cv2.imread('images/input.jpg')
num_rows, num_cols = img.shape[:2]
print('Dimensiones de la images renglones, columnas \n', num_rows, num_cols)
matrix_translation= np.float32([[1,0,int(0.5 * num_cols)], [0,1, int(0.5 * num_rows)]])
print('Matriz de translacion\n', matrix_translation)
rotation_matrix = cv2.getRotationMatrix2D((num_cols - 2, num_rows - 2),90,1)
print('Matriz de rotation\n',rotation_matrix)
img_translation = cv2.warpAffine(img, matrix_translation, (2* num_cols, 2 * num_rows))
cv2.imshow('Translation', img_translation)
img_rotation = cv2.warpAffine(img_translation, rotation_matrix, (num_cols * 2, num_rows * 2))
cv2.imshow('Rotation', img_rotation)
cv2.waitKey()
