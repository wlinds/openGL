import numpy as np
import pygame


class InputHandler:
    def __init__(self):
        self.keys = {}

    def update(self):
        self.keys = pygame.key.get_pressed()

    def is_key_pressed(self, key):
        return self.keys[key]


def top_down_controls(player):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.move("up")
    if keys[pygame.K_s]:
        player.move("down")
    if keys[pygame.K_a]:
        player.move("left")
    if keys[pygame.K_d]:
        player.move("right")
    if keys[pygame.K_q]:
        player.move("forward")
    if keys[pygame.K_e]:
        player.move("backward")


def first_person_controls(player):
    keys = pygame.key.get_pressed()

    rotation_speed = 2.0

    if keys[pygame.K_a]:
        player.rotation -= rotation_speed
    if keys[pygame.K_d]:
        player.rotation += rotation_speed

    if keys[pygame.K_1]:
        player.rotation_y -= rotation_speed
    if keys[pygame.K_2]:
        player.rotation_y += rotation_speed

    if keys[pygame.K_z]:
        player.rotation_z -= rotation_speed
    if keys[pygame.K_x]:
        player.rotation_z += rotation_speed

    # 2D vector for direction in which the player should move
    rotation_radians = np.radians(player.rotation)
    forward_vector = np.array(
        [
            np.sin(rotation_radians),
            np.cos(rotation_radians),
            0,  # (ignore Z-axis, implement this for flight mode controls instead)
        ]
    )

    if keys[pygame.K_w]:
        player.position += forward_vector * player.speed
    if keys[pygame.K_s]:
        player.position -= forward_vector * player.speed
