import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *


class PlayerTwo:
    def __init__(self):
        self.position = [0.0, 0.0, 0.0]
        self.radius = 0.1
        self.speed = 0.1
        self.player_color = np.array([1.0, 1.0, 1.0])
        self.rotation = 0.0

    def adjust_color(self, new_color):
        self.player_color = np.clip(new_color, 0.0, 1.0)

    def adjust_size(self, new_size):
        self.radius = new_size

    def draw(self):
        x, y, z = self.position
        glPushMatrix()
        glTranslatef(x, y, z)
        glColor3fv(self.player_color)
        quadric = gluNewQuadric()

        # Adjusted for smoother interpolation, not sure how it affects performance
        gluSphere(quadric, self.radius, int(20 * self.radius), int(20 * self.radius))
        gluDeleteQuadric(quadric)

        # Arrow to visualize player direction (This can be removed, just for visual feedback)
        arrow_length = self.radius // 2
        arrow_color = np.array([0.3, 0.3, 0.3])
        glPushMatrix()
        glRotatef(self.rotation, 0.0, 0.0, -1.0)
        glColor3fv(arrow_color)
        glBegin(GL_TRIANGLES)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(-arrow_length, -arrow_length * 1.5, 0.0)
        glVertex3f(arrow_length, -arrow_length * 1.5, 0.0)
        glEnd()
        glPopMatrix()
        ## / END test arrow

        glPopMatrix()

    def move(self, direction):
        if direction == "up":
            self.position[1] += self.speed
        elif direction == "down":
            self.position[1] -= self.speed

        elif direction == "left":
            self.position[0] -= self.speed
        elif direction == "right":
            self.position[0] += self.speed

        if direction == "forward":
            self.position[2] -= self.speed
        elif direction == "backward":
            self.position[2] += self.speed
