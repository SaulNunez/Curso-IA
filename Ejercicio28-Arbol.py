import pygame
import math

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Arbol Fractal')
screen = pygame.display.get_surface()


def drawTree(x1, y1, angle, depth):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 5.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 5.0)
        pygame.draw.line(screen, (255, 0, 0), (x1, y1), (x2, y2), 2)
        drawTree(x2, y2, angle - 20, depth - 1)
        drawTree(x2, y2, angle + 20, depth - 1)


def input(event):
    if event.type == pygame.QUIT:
        exit(0)


drawTree(300, 550, -90, 15)
pygame.display.flip()
while True:
    input(pygame.event.wait())
