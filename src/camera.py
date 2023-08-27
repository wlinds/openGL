import numpy as np
from OpenGL.GL import glRotatef, glTranslatef
from OpenGL.GLU import gluPerspective


# Simple starting position for testing (top down perspective)
def basic_static_perspective(display, distance=-100):
    gluPerspective = (45, (display[0] / display[1]), 0.1, 200.0)
    glTranslatef = (0, 0, distance)
    return gluPerspective, glTranslatef


# Follow the player (top down perspective)
def top_down_follwing(display, player_position, translation=[0, 0, -200]):
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


# First person perspective
def first_person_perspective(
    display, player_position, player_rotation, translation=[1, 0, 0], camera_z_offset=10
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
    camera_position = player_position + forward_vector * translation[2]
    camera_position[2] += camera_z_offset

    # Again, this might be better to return, but we do it in here first
    glTranslatef(-camera_position[0], -camera_position[1], -camera_position[2])
    glRotatef(-player_rotation, 1, 0, 0)


# Camera System Boilerplate (Still unused. TODO: use this instead of stand-alone functions.)
class Camera:
    def __init__(self):
        self.position = [0, 0, -20]
        self.rotation = [0, 0, 0]

    def apply(self):
        glTranslatef(*self.position)
        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)
