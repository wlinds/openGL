import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *


class PlayerTwo:
    def __init__(self):
        self.position = [0.0, 0.0, 0.0]
        self.radius = 0.1
        self.speed = 0.1
        self.player_color = np.array([1.0, 1.0, 1.0])

    def adjust_color(self, new_color):
        self.player_color = np.clip(new_color, 0.0, 1.0)

    def draw(self):
        x, y, z = self.position
        glPushMatrix()
        glTranslatef(x, y, z)
        glColor3fv(self.player_color)
        quadric = gluNewQuadric()
        gluSphere(quadric, self.radius, 20, 20)
        gluDeleteQuadric(quadric)
        glPopMatrix()

    def move(self, direction):
        if direction == "up":
            self.position[1] -= self.speed
        elif direction == "down":
            self.position[1] += self.speed

        elif direction == "left":
            self.position[0] -= self.speed
        elif direction == "right":
            self.position[0] += self.speed

        if direction == "forward":
            self.position[2] -= self.speed
        elif direction == "backward":
            self.position[2] += self.speed
