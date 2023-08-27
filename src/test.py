import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

from base_grid import GridDrawer
from camera import basic_static_perspective
from input_handler import player_controls
from player_entity import PlayerTwo


def run():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    # Default Camera: Top down view
    perspective, translation = basic_static_perspective(display, distance=-50)
    gluPerspective(*perspective)
    glTranslatef(*translation)

    grid_A = GridDrawer(grid_spacing=1.0, grid_size=128, grid_color=(0.0, 0.5, 0.5))
    player_two = PlayerTwo()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        player_controls(player_two)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()

        grid_A.draw()
        player_two.draw()

        glPopMatrix()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run()
