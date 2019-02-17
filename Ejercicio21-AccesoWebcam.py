import cv2
cap = cv2.VideoCapture(0)

# Revisa si la camara se ha abierto correctamente

if not cap.isOpened():
    raise IOError('No se puede abrir camara webcam')
while True:
    ret, frame = cap.read()
    # ret es un valor booleano que nos indica que se leyo la imagen
    frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
    # fx y fy definen el tamaño de la imagen
    cv2.imshow('Entrada', frame)
    c = cv2.waitKey(1)
    if c == 27:  # Revisamos si oprimimos la tecla ESC
        break

cap.release()
cv2.destroyAllWindows()
