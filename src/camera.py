from OpenGL.GL import glRotatef, glTranslatef
from OpenGL.GLU import gluPerspective


# Simple starting position for testing
def basic_static_perspective(display, distance=-100):
    gluPerspective = (45, (display[0] / display[1]), 0.1, 200.0)
    glTranslatef = (0, 0, distance)
    return gluPerspective, glTranslatef


# Camera System Boilerplate
class Camera:
    def __init__(self):
        self.position = [0, 0, -20]
        self.rotation = [0, 0, 0]

    def apply(self):
        glTranslatef(*self.position)
        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)
