import cv2
import numpy
global img 

img = cv2.imread('images/messi.png')
balon = img[230:276, 260:330]
pasto = img[230:276, 50:120]
cv2.imshow('Messi', img)
events = [i for i in dir(cv2) if 'EVENT' in i]
def daCoordenadas(event, x, y, flags, param):
    if event == cv2. EVENT_LBUTTONDOWN:
        print(x,y)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        img[225:271, 100:170] = balon
        img[230:276, 260:330] = pasto
    if event == cv2.EVENT_RBUTTONDOWN:
        img[230:276, 260:330] = balon
cv2.namedWindow('Messi')
cv2.setMouseCallback('Messi', daCoordenadas)
while(True):
    cv2.imshow('Messi', img)
    if(cv2.waitKey(20) & 0xFF == 27):
        break
cv2.destroyAllWindows()