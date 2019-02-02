from PyQt5 import QtGui
import cv2
import numpy as np

class Projection(object):
    def __init__(self):
        self.tabName = 'Proyección'
        self.horizontal_swipe_reason = 0.33
        self.vertical_swipe_reason = 0.66

        # Warranty image exist in instance
        UpdateImage('./image.jpg')

    def GuiSetup(self):
        layout = QtGui.QVBoxLayout()

        return layout

    def Render(self):
        
        rows, cols = image.shape[:2]
        src_points = np.float32([[0,0], [cols-1, 0], [0, rows-1], [cols-1, rows-1]])
        dst_points = np.float32([[0,0], [cols-1, 0], [int(self.horizontal_swipe_reason * cols), rows-1], [int(self.vertical_swipe_reason * cols), rows-1]])

        projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        img_output = cv2.warpPerspective(image, projective_matrix, (cols, rows))
        cv2.imshow('Input', image)
        cv2.imshow('Output', img_output)
        cv2.waitKey()

    def UpdateImage(self, path):
        self.image = cv2.imread(path)
        self.Render()

    def SaveImage(self, path):
        pass