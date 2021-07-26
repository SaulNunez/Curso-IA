import cv2
import numpy as np 
import time

# Constantes
DIM_CANCHA = {'x': 600, 'y': 400}
DIM_PALETA = 5
BARRA_DIM = 20
PALETA_VEL = 150

# Colores
COLOR_PELOTA = (255, 255, 255)
COLOR_PALETA = (255, 255, 255)

pos_paleta_izq = (DIM_CANCHA['x'] - DIM_PALETA * 2, DIM_CANCHA['y']/2)
pos_paleta_der = (0 + DIM_PALETA * 2 , DIM_CANCHA['y']/2)
pelota_delta = (100, 100)
pelota_pos = (DIM_CANCHA['x']/2, DIM_CANCHA['y']/2)
pelot = cv2.imread('pelota.jpg')
# Pelota para rellenar donde ha estado nuestra pelota
black_pel = np.zeros(pelot.shape, dtype=np.uint8)

time_of_last_frame = time.time()

cancha = np.zeros((DIM_CANCHA['y'], DIM_CANCHA['x'], 3), np.uint8)

def pelota(img, pelota_img, orig):
    img[orig[0]:orig[0]+pelota_img.shape[0],orig[1]:orig[1]+pelota_img.shape[1]] = pelota_img

def paleta(img, orig, thicc, color):
    cv2.line(img, (orig[0], orig[1] + BARRA_DIM), (orig[0], orig[1] - BARRA_DIM), color, thicc)


while True:
    time_of_current_frame = time.time()
    delta_time = time_of_current_frame - time_of_last_frame
    time_of_last_frame = time_of_current_frame

    # Primero necesitamos borrar pelota anterior y luego dibujamos pelota en posicion actual

    #Pelota negra
    pelota(cancha, black_pel, (int(pelota_pos[0]),int(pelota_pos[1])))
    #Detectar si en esta nueva posición nos salimos de la pantalla
    if(pelota_pos[0] > DIM_CANCHA['x'] or pelota_pos[0] < 0):
        pelota_pos = (DIM_CANCHA['x']/2, DIM_CANCHA['y']/2)
        pelota_delta = (100, 100)
    # Si chocamos abajo o arriba rebotamos
    if(pelota_pos[1] > DIM_CANCHA['y'] or pelota_pos[1] < 0):
        pelota_delta = (pelota_delta[0] * -1, pelota_delta[1] * -1)
    # Si chocamos con las paletas también rebotamos
    if(pelota_pos[0] + pelot.shape[0] < pos_paleta_der[0] - DIM_PALETA and 
        (pelota_pos[1] > pos_paleta_der[1] - BARRA_DIM and pelota_pos[1] < pos_paleta_der[1] + BARRA_DIM)):
        pelota_delta = (pelota_delta[0] * -1, pelota_delta[1] * -1)
    if(pelota_pos[0] - pelot.shape[0] > pos_paleta_izq[0] + DIM_PALETA and 
        (pelota_pos[1] > pos_paleta_izq[1] - BARRA_DIM and pelota_pos[1] < pos_paleta_izq[1] + BARRA_DIM)):
        pelota_delta = (pelota_delta[0] * -1, pelota_delta[1] * -1)
    #Sumar velocidad pelota
    pelota_pos = (pelota_pos[0] + pelota_delta[0] * delta_time, pelota_pos[1] + pelota_delta[1] * delta_time)
    #Pelota blanca
    pelota(cancha, pelot, (int(pelota_pos[0]),int(pelota_pos[1])))

    # Paleta izquierda
    paleta(cancha, (int(pos_paleta_izq[0]), int(pos_paleta_izq[1])), DIM_PALETA, (0,0,0))
    # Paleta derecha
    paleta(cancha, (int(pos_paleta_der[0]), int(pos_paleta_der[1])), DIM_PALETA, (0,0,0))
    k = cv2.waitKey(1)
    if k == ord('w') and not k == ord('s') and pos_paleta_izq[1] + BARRA_DIM < DIM_CANCHA['y']:
        pos_paleta_izq = (pos_paleta_izq[0], pos_paleta_izq[1] + delta_time * PALETA_VEL)
    elif k == ord('s') and not k == ord('w') and pos_paleta_izq[1] - BARRA_DIM > 0:
        pos_paleta_izq = (pos_paleta_izq[0], pos_paleta_izq[1] - delta_time * PALETA_VEL)

    if k == 2490368 and not k == 2621440 and pos_paleta_izq[1] + BARRA_DIM < DIM_CANCHA['y']:
        pos_paleta_der = (pos_paleta_der[0], pos_paleta_der[1] + delta_time * PALETA_VEL)
    elif k == 2621440 and not k == 2490368 and pos_paleta_izq[1] - BARRA_DIM > 0:
        pos_paleta_der = (pos_paleta_der[0], pos_paleta_der[1] - delta_time * PALETA_VEL)

    # Paleta izquierda
    paleta(cancha, (int(pos_paleta_izq[0]), int(pos_paleta_izq[1])), DIM_PALETA, COLOR_PALETA)
    # Paleta derecha
    paleta(cancha, (int(pos_paleta_der[0]), int(pos_paleta_der[1])), DIM_PALETA, COLOR_PALETA)

    cv2.imshow('pong', cancha)
    
