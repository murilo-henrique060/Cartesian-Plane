import pygame as pg
from pygame.locals import *

import numpy as np
from numpy import array, cross

import OpenGL.GL as gl
import OpenGL.GLU as glu

pg.init()
windowsSize = (800, 600)
screen = pg.display.set_mode(windowsSize, DOUBLEBUF | OPENGL)

# Set the camera perspective
glu.gluPerspective(45, (windowsSize[0] / windowsSize[1]), 0.1, 50.0)
camera_pos = array([0, 3, 0], dtype=np.float32)

def square():
    vetices = (
        (0., 0.),
        (0., 1.),
        (1., -1.),
        (0., -1.)
    )

    gl.glPointSize(5)
    gl.glBegin(gl.GL_POINTS)
    gl.glColor3fv((255., 0., 0.))
    for vertex in vetices:
        gl.glVertex2fv(vertex)
    gl.glEnd()

while True:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            pg.quit()
            quit()

    # Clear the screen
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    square()

    # Update the screen
    pg.display.flip()