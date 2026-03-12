import pygame
from core.settings import PLAYER_SPEED


class Player:

    def __init__(self, x, y):

        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 200, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):

        keys = pygame.key.get_pressed()

        move_x = 0
        move_y = 0

        # apenas uma direção por vez
        if keys[pygame.K_UP]:
            move_y = -PLAYER_SPEED

        elif keys[pygame.K_DOWN]:
            move_y = PLAYER_SPEED

        elif keys[pygame.K_LEFT]:
            move_x = -PLAYER_SPEED

        elif keys[pygame.K_RIGHT]:
            move_x = PLAYER_SPEED

        self.rect.x += move_x
        self.rect.y += move_y

    def draw(self, screen):

        screen.blit(self.image, self.rect)
