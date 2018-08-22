import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, OPENGL | DOUBLEBUF)

gluPerspective(45, display[0]/display[1], 0.1, 50)
glTranslatef(0, 0, -5)
glColor3fv((0, 127, 127))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_QUADS)
    glVertex3fv((-1,-1, 0))
    glVertex3fv((-1, 1, 0))
    glVertex3fv(( 1, 1, 0))
    glVertex3fv(( 1,-1, 0))
    glEnd()

    glRotatef(1, 1, 0, 0)
    pygame.display.flip()
    pygame.time.wait(10)
