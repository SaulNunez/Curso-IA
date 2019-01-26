import cv2
import numpy as np

img=cv2.imread('./images/input.jpg')
rows, cols = img.shape[:2]
print('renglones, columnas\n', rows, cols)
# Contornos de la imagen (x0, y0), (xn, y0), (x0, ym), (xn, yn)
src_points = np.float32([[0,0], [cols-1, 0], [0, rows -1]])
# Contornos a mandar (x0, y0), (xn, y0), (xn, y0)
print('Puntos origen\n', src_points)
dst_points = np.float32([[cols-1, 0], [0,0], [cols-1, rows-1]])
dst_points2 = np.float32([[0,0], [int(0.6*(cols-1)), 0], [int(0.4*(cols-1)), rows-1]])

print('Puntos destino\n', dst_points)
affine_matrix = cv2.getAffineTransform(src_points, dst_points)
print('Matriz afin\n', affine_matrix)
img_output = cv2.warpAffine(img, affine_matrix, (cols, rows))

cv2.imshow('Imagen original', img)
cv2.imshow('Imagen afin', img_output)
cv2.waitKey()
