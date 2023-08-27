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
