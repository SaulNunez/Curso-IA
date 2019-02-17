import cv2
import numpy as np


def print_howto():
    print("""
        Cambiar a modo caricatura la imagen:
        1. Caricatura sin color oprima 's'
        2. Caricatura con color oprima 'c'
    """)


def cartoonize_image(img, ksize=5, sketch_mode=False):
    num_repetitions, sigma_color,  sigma_space, ds_factor = 10, 5, 7, 4
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img_gray, 7)
    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=ksize)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    if sketch_mode:
        return cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    img_small = cv2.resize(img, None, fx=1.0/ds_factor,
                           fy=1.0/ds_factor, interpolation=cv2.INTER_AREA)
    for i in range(num_repetitions):
        img_small = cv2.bilateralFilter(
            img_small, ksize, sigma_color, sigma_space)
    img_output = cv2.resize(img_small, None, fx=ds_factor,
                            fy=ds_factor, interpolation=cv2.INTER_LINEAR)
    dst = np.zeros(img_gray.shape)
    dst = cv2.bitwise_and(img_output, img_output, mask=mask)
    return dst


if __name__ == '__main__':
    print_howto()
    cap = cv2.VideoCapture(0)

    cur_mode = None
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        c = cv2.waitKey(1)
        if c == 27:
            break
        
        if c != -1 and c != 255 and c != cur_mode:
            cur_mode = c
        
        if cur_mode == ord('s'):
            cv2.imshow('Cartoonize', cartoonize_image(frame, ksize=5, sketch_mode=True))
        elif cur_mode == ord('c'):
            cv2.imshow('Cartoonize', cartoonize_image(frame, ksize=5, sketch_mode=False))
        else:
            cv2.imshow('Cartoonize', frame)

    cap.release()
    cv2.destroyAllWindows()