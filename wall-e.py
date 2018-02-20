from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def draw():
    # background
    glClearColor(1, 1, 1,1)
    glClear(GL_COLOR_BUFFER_BIT)
   ##################################
    glColor(.7, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-.45, .3)
    glVertex2f(.45, .3)
    glVertex2f(.7, -.85)
    glVertex2f(-.7, -.85)
    glEnd()
    glFlush()

    #HEAD
    glBegin(GL_POLYGON)
    glColor(255,.8,.4)
    glVertex2d(.25,.8)
    glVertex2d(-.25,.8)
    glVertex2d(-.25,.35)
    glVertex2d(.25,.35)
    glEnd()

    # NOSE
    glBegin(GL_POLYGON)
    glColor(0.96, 0.65, 0.4)
    glVertex2f(0,.65)
    glVertex2f(.05,.53)
    glVertex2f(-.05,.53)
    glEnd()

    #MOUTH
    glColor(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2d(.05, .4)
    glVertex2d(-.05, .4)
    glVertex2d(-.09, .46)
    glVertex2d(.09, .46)
    glEnd()
    glFlush()



    #NECK
    glColor(255,.8,.4)
    glBegin(GL_POLYGON)
    glVertex2d(-0.075, 0.35)
    glVertex2d(0.075, 0.35)
    glVertex2d(0.075, 0.1)
    glVertex2d(-0.075, 0.11)
    glEnd()

    # Body
    glColor(0,0,1)
    glBegin(GL_POLYGON)
    glVertex2d(.45,.3)
    glVertex2d(.32,-.17)
    glVertex2d(-.32,-.17)
    glVertex2d(-.45,.3)
    glEnd()

    # SUPER SHEHAB
    glColor(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2d(-.25, .23)
    glVertex2d(.25, .23)
    glVertex2f(.3,.18)
    glVertex2f(0,-.08)
    glVertex2f(-.3,.18)
    glEnd()

    glColor(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(-.12,.18)
    glVertex2d(.15,.18)
    glEnd()

    ##############
    glColor(1,0,0)
    glBegin(GL_POINTS)
    r = 0.051
    for theta in np.arange(pi / 2,pi *(3 / 2), 0.0001):
        x = r * cos(theta) - .12
        y = r * sin(theta) + .13
        glVertex2d(x, y)
    glEnd()

    glColor(1,0,0)
    glBegin(GL_LINES)
    glVertex2d(-.12,.0788)
    glVertex2d(.01,.0788)
    glEnd()

    glColor(1, 0, 0)
    glBegin(GL_POINTS)
    r = 0.05
    for theta in np.arange(pi * (23 / 18),(7 / 3) * pi , 0.0001):
        x = r * cos(theta)-.02
        y = r * sin(theta) +.035
        glVertex2d(x, y)
    glEnd()


    #RIGHT HAND

    glColor(1.000, 0.871, 0.678)
    glBegin(GL_POLYGON)
    glVertex2f(0.42, 0.2)
    glVertex2f(.49, 0.2)
    glVertex2f(0.49, .25)
    glVertex2f(0.43, .25)
    glEnd()

    glColor(0.804, 0.522, 0.247)
    glBegin(GL_POLYGON)
    glVertex2f(0.49, 0.3)
    glVertex2f(.63, 0.3)
    glVertex2f(0.63, .15)
    glVertex2f(0.49, .15)
    glEnd()

    glColor(0.804, 0.522, 0.247)
    glBegin(GL_POLYGON)
    glVertex2f(.53,.3)
    glVertex2f(.59, .3)
    glVertex2f(0.59, .58)
    glVertex2f(0.53, .58)
    glEnd()

    glColor(.824, 0.706, 0.549)
    glBegin(GL_POLYGON)
    glVertex2f(0.51, .42)
    glVertex2f(.61, .42)
    glVertex2f(0.61,.48)
    glVertex2f(0.51, .48)
    glEnd()
##############################
    glColor(0.804, 0.522, 0.247)
    glBegin(GL_POLYGON)
    glVertex2f(0.465, .58)
    glVertex2f(.65, .58)
    glVertex2f(.65, .645)
    glVertex2f(.465, .645)
    glEnd()

    glColor(0.804, 0.522, 0.247)
    glBegin(GL_POLYGON)
    glVertex2f(.465,.645)
    glVertex2f(.52, .645)
    glVertex2f(.52, .75)
    glVertex2f(.465, .75)
    glEnd()

    glColor(0.804, 0.522, 0.247)
    glBegin(GL_POLYGON)
    glVertex2f(.595, .645)
    glVertex2f(.65, .645)
    glVertex2f(0.65, .75)
    glVertex2f(0.595, .75)
    glEnd()
    #LEFT HAND
    glColor(1.000, 0.871, 0.678)
    glBegin(GL_POLYGON)
    glVertex2f(-0.42, 0.2)
    glVertex2f(-.49, 0.2)
    glVertex2f(-0.49, .25)
    glVertex2f(-0.43, .25)
    glEnd()


    glColor(0.804, 0.522, 0.247)
    glBegin(GL_POLYGON)
    glVertex2f(-0.49, 0.3)
    glVertex2f(-.63, 0.3)
    glVertex2f(-0.63, .15)
    glVertex2f(-0.49, .15)
    glEnd()
    glFlush()

    glColor(0.804, 0.522, 0.247)
    glBegin(GL_POLYGON)
    glVertex2f(-.53,.3)
    glVertex2f(-.59, .3)
    glVertex2f(-0.59,- .17)
    glVertex2f(-0.53, -.17)
    glEnd()

    glColor(.824, 0.706, 0.549)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, 0.0)
    glVertex2f(-.62, 0.0)
    glVertex2f(-0.62, -.055)
    glVertex2f(-0.5, -.055)
    glEnd()
##############################
    glColor(0.804, 0.522, 0.247)
    glBegin(GL_POLYGON)
    glVertex2f(-0.465, -.17)
    glVertex2f(-.65,- .17)
    glVertex2f(-.65, -.23)
    glVertex2f(-.465,- .23)
    glEnd()

    glColor(0.804, 0.522, 0.247)
    glBegin(GL_POLYGON)
    glVertex2f(-.465,- .23)
    glVertex2f(-.52,- .23)
    glVertex2f(-.52,-.335)
    glVertex2f(-.465,- .335)
    glEnd()

    glColor(0.804, 0.522, 0.247)
    glBegin(GL_POLYGON)
    glVertex2f(-.595, -.23)
    glVertex2f(-.65, -.23)
    glVertex2f(-0.65, -.335)
    glVertex2f(-0.595, -.335)
    glEnd()

    # WAIST
    glColor(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(.32, -.17)
    glVertex2d(-.32, -.17)
    glVertex2f(0,-.35)
    glEnd()

    #RIGHT LEG
    glColor(0,0,1)
    glBegin(GL_POLYGON)
    glVertex2f(0, -.35)
    glVertex2d(.32, -.17)
    glVertex2f(.42,-.9)
    glVertex2f(.33,-.9)
    glEnd()

    #LEFT LEG
    glColor(0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex2f(0, -.35)
    glVertex2d(-.32, -.17)
    glVertex2f(-.42, -.9)
    glVertex2f(-.33, -.9)
    glEnd()


    # Right Eye
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    r = 0.08
    for theta in np.arange(0, 2*pi, 0.01):
        x=r*cos(theta)+0.15
        y=r*sin(theta)+0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.28, 0.75, 1)
    glBegin(GL_POLYGON)
    r = 0.068
    for theta in np.arange(0, 2 * pi, 0.01):
        x = r * cos(theta) + 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.24, 0.13, 1)
    glBegin(GL_POLYGON)
    r = 0.05
    for theta in np.arange(0, 2 * pi, 0.01):
        x = r * cos(theta) + 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.5, 0.82, 1)
    glBegin(GL_POLYGON)
    r = 0.03
    for theta in np.arange(0, 2 * pi, 0.01):
        x = r * cos(theta) + 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()

    #LEFT EYE
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    r = 0.08
    for theta in np.arange(0, 2 * pi, 0.01):
        x = r * cos(theta) - 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.28, 0.75, 1)
    glBegin(GL_POLYGON)
    r = 0.068
    for theta in np.arange(0, 2 * pi, 0.01):
        x = r * cos(theta) - 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.24, 0.13, 1)
    glBegin(GL_POLYGON)
    r = 0.05
    for theta in np.arange(0, 2 * pi, 0.01):
        x = r * cos(theta) - 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.5, 0.82, 1)
    glBegin(GL_POLYGON)
    r = 0.03
    for theta in np.arange(0, 2 * pi, 0.01):
        x = r * cos(theta) - 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Wall.E")
glutInitWindowSize(1000,1000)  # Set the window's initial width & height
glutDisplayFunc(draw)
glutMainLoop()