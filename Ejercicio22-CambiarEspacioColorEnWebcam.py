import cv2


def print_howto():
    print(""" 
        Cambiamos el espacio de color de la entrada de video usando el teclado como control.
        Las teclas de control son:
        1. Escala de grises - oprima 'g'
        2. YUV - Oprima 'y'
        3. HSV - Oprima 'h'
        """)


if __name__ == '__main__':
    print_howto()
    cap = cv2.VideoCapture(0)
    # Revisa que la camara este abierta correctamente
    if not cap.isOpened():
        raise IOError('No se pudo abrir Webcam')
    cur_mode = None
    while True:
        # Lee el cuadro activo de la camara
        ret, frame = cap.read()
        # Cambia el tamaño de la imagen capturada
        frame = cv2.resize(frame, None, fx=1, fy=1,
                           interpolation=cv2.INTER_AREA)
        c = cv2.waitKey(1)
        if(c == 27):
            break
        if c != -1 and c != 255 and c != cur_mode:
            cur_mode = c
        if cur_mode == ord('g'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif cur_mode == ord('y'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        elif cur_mode == ord('h'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        else:
            output = frame

        cv2.imshow('Webcam', output)
    cap.release()
    cv2.destroyAllWindows()
