import numpy as np
import pygame
from OpenGL.GL import glRotatef, glTranslatef
from OpenGL.GLU import gluPerspective

from base_grid import *
from cube_renderer import CubeRenderer


def basic_static_perspective(display, distance=-100):
    """Simple starting position for testing (top down perspective)

    distance (float): The distance along the negative Z-axis from which the scene will be viewed.

    Returns:
        tuple: A tuple containing the perspective parameters and translation values in the form of (gluPerspective, glTranslatef).
    """

    gluPerspective = (45, (display[0] / display[1]), 0.1, 200.0)
    glTranslatef = (0, 0, distance)
    return gluPerspective, glTranslatef


def top_down_follwing(display, player_position, translation=[0, 0, -200]):
    "Follow the player (top down perspective)"

    aspect_ratio = display[0] / display[1]
    fov = 45
    near_clip = 0.1
    far_clip = 200.0
    gluPerspective(fov, aspect_ratio, near_clip, far_clip)

    # Calculate the camera position centered on the player
    camera_position = [
        player_position[0] + translation[0],
        player_position[1] + translation[1],
        player_position[2] + translation[2],
    ]
    return camera_position

    # TODO: Rewrite first_person_perspective + add new keybinds.


def first_person_perspective(
    display, player_position, player_rotation, translation=[1, 0, 0], z_offset=1
):
    aspect_ratio = display[0] / display[1]
    fov = 90
    near_clip = 0.1
    far_clip = 200.0
    gluPerspective(fov, aspect_ratio, near_clip, far_clip)

    # Calculate the camera position based on player position and rotation
    rotation_radians = np.radians(player_rotation)
    forward_vector = np.array([np.cos(rotation_radians), np.sin(rotation_radians), 0])

    # Offset z above grid
    camera_position = player_position + forward_vector * translation[1]
    camera_position[2] += z_offset

    # Again, this might be better to return, but we do it in here first
    glTranslatef(-camera_position[0], -camera_position[1], -camera_position[2])
    glRotatef(-player_rotation, 1, 0, 0)


if __name__ == "__main__":
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    grid_A = GridDrawer(grid_spacing=1.0, grid_size=128, grid_color=(0.0, 0.5, 0.5))
    cubes = CubeRenderer(4.0, 128)

    test_modulation_z = 0.0

    test_modulation_x = 0.0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

        # Adjust the camera's Z-axis position based on key presses
        if keys[pygame.K_w]:
            test_modulation_z += 1.0  # Z-axis position
        if keys[pygame.K_s]:
            test_modulation_z -= 1.0  # Z-axis position
        if keys[pygame.K_d]:
            test_modulation_x -= 1.0  # X-axis position
        if keys[pygame.K_a]:
            test_modulation_x += 1.0  # X-axis position

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()

        p, t = basic_static_perspective(display, distance=-100 + test_modulation_z)
        gluPerspective(*p)
        glTranslatef(t[0] + test_modulation_x, t[1], t[2])

        grid_A.draw()

        cubes.render(pattern=False)

        glPopMatrix()
        pygame.display.flip()
