import cv2

image = cv2.imread('./images/input.jpg')
imageGris = cv2.imread('./images/input.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Color Image', image)
cv2.imshow('Grayscale', imageGris)
cv2.imwrite('./images/output_gray.png', imageGris, [cv2.IMWRITE_PNG_COMPRESSION])

cv2.waitKey()
