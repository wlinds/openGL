import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

from base_grid import GridDrawer
from camera import *
from cube_renderer import CubeRenderer
from input_handler import first_person_controls, top_down_controls
from player_entity import PlayerTwo


def run():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    # Default Camera: Top down view | Not used - testing top_down_follwing() in the game loop instead
    # perspective, translation = basic_static_perspective(display, distance=-50)
    # gluPerspective(*perspective)
    # glTranslatef(*translation)

    grid_A = GridDrawer(grid_spacing=1.0, grid_size=16, grid_color=(0.0, 0.5, 0.5))
    player_two = PlayerTwo()
    clock = pygame.time.Clock()

    cube_renderer = CubeRenderer(
        grid_spacing=1.0, grid_size=128
    )  # Testing cubes with perspective change

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if (
                    event.key == pygame.K_f
                ):  # !! Only for testing purpose, all keybinds should be in input_handler.py
                    player_two.toggle_first_person_mode()

        # first_person_controls(player_two)
        # top_down_controls(player_two)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()

        # Change camera for first_person_mode
        if player_two.first_person_mode:
            camera_position = first_person_perspective(
                display, player_two.position, player_two.rotation
            )
            # Currently updates position in function, does not return anything
            # glTranslatef(*camera_position)

            first_person_controls(player_two)
            print(camera_position)

            print(player_two.rotation, player_two.rotation_y, player_two.rotation_z)
            print(player_two.position)

        else:
            camera_position = top_down_follwing(display, player_two.position)
            glTranslatef(*camera_position)

            # top_down_controls(player_two)  # Top_down camera works for both first_person_controls and top_down_controls, really a matter of personal preference.
            first_person_controls(player_two)
            player_two.adjust_size(6.0)
            print(player_two.rotation, player_two.rotation_y, player_two.rotation_z)

        grid_A.draw()
        cube_renderer.render()

        player_two.draw()
        glPopMatrix()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run()
