import numpy as np
from OpenGL.GL import *


class CubeRenderer:
    def __init__(self, grid_spacing, grid_size):
        self.grid_spacing = grid_spacing
        self.grid_size = grid_size
        self.cube_size = grid_spacing * 0.5

    def render(self, pattern=False):
        glPushMatrix()
        glColor3f(0.6, 0.6, 0.6)
        spacing = self.grid_spacing
        size = self.grid_size

        # Place cubes in a predefined pattern
        if pattern:
            for i in range(-size, size + 1):
                for j in range(-size, size + 1):
                    if i % 2 == 0 and j % 2 == 0:  # Even spaces
                        self.draw_cube(i * spacing, j * spacing)
                    elif i % 2 == 1 and j % 2 == 1:  # Odd spaces
                        self.draw_cube(i * spacing, j * spacing)
        else:
            np.random.seed(42)
            random_positions = np.random.randint(-size, size + 1, size=(100, 2))
            for position in random_positions:
                x, y = position
                self.draw_cube(x * spacing, y * spacing)

        glPopMatrix()

    def draw_cube(self, x, y):
        vertices = [
            (x, y, 0),
            (x + self.cube_size, y, 0),
            (x + self.cube_size, y + self.cube_size, 0),
            (x, y + self.cube_size, 0),
            (x, y, self.cube_size),
            (x + self.cube_size, y, self.cube_size),
            (x + self.cube_size, y + self.cube_size, self.cube_size),
            (x, y + self.cube_size, self.cube_size),
        ]

        faces = [
            (0, 1, 2, 3),  # Front face
            (4, 5, 6, 7),  # Back face
            (0, 1, 5, 4),  # Top face
            (2, 3, 7, 6),  # Bottom face
            (0, 3, 7, 4),  # Left face
            (1, 2, 6, 5),  # Right face
        ]

        glBegin(GL_QUADS)
        for face in faces:
            for vertex_index in face:
                glVertex3f(*vertices[vertex_index])
        glEnd()
