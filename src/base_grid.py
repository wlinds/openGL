import pygame
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective

from camera import basic_static_perspective


class GridDrawer:
    """
    Create a simple wireframe plane.

    Args:
        grid_spacing (float): The distance between grid lines.
        grid_size (int): The number of grid lines in each direction from the origin.
        grid_color (Tuple[float, float, float]): The color of the grid lines.
    """

    def __init__(self, grid_spacing, grid_size, grid_color):
        self.grid_spacing = grid_spacing
        self.grid_size = grid_size
        self.grid_color = grid_color

    def draw(self):
        glBegin(GL_LINES)
        glColor3f(*self.grid_color)
        spacing = self.grid_spacing
        size = self.grid_size

        for i in range(-size, size + 1):
            glVertex3f(i * spacing, size * spacing, 0.0)
            glVertex3f(i * spacing, -size * spacing, 0.0)

            glVertex3f(size * spacing, i * spacing, 0.0)
            glVertex3f(-size * spacing, i * spacing, 0.0)
        glEnd()


def run_test_grid():
    # Top down view
    perspective, translation = basic_static_perspective(display)
    gluPerspective(*perspective)
    glTranslatef(*translation)

    # Example grid
    grid_A = GridDrawer(grid_spacing=1.0, grid_size=128, grid_color=(0.0, 0.5, 0.5))

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()

        grid_A.draw()

        glPopMatrix()
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    run_test_grid()
