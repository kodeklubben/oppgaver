import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, OPENGL | DOUBLEBUF)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()
    pygame.time.wait(10)
"""
"""
