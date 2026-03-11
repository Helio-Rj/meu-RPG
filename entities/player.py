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

        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED

        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

    def draw(self, screen):

        screen.blit(self.image, self.rect)
