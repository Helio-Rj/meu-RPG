import pygame
from core.settings import PLAYER_SPEED


class Player:

    def __init__(self, x, y):

        self.sprite = pygame.image.load(
            "assets/sprites/player.png"
        ).convert_alpha()

        self.x_sprite = 0
        self.y_sprite = 0

        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.animation_timer = 0
        self.animation_speed = 5

    def update(self):

        keys = pygame.key.get_pressed()

        moving = False

        # movimento (SEM diagonal)
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
            self.y_sprite = 0
            moving = True

        elif keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED
            self.y_sprite = 90
            moving = True

        elif keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
            self.y_sprite = 172
            moving = True

        elif keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
            self.y_sprite = 254
            moving = True

        # animação só quando anda
        if moving:
            self.animation_timer += 1

            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.x_sprite += 1

                if self.x_sprite > 5:
                    self.x_sprite = 0
        else:
            self.x_sprite = 0  # parado

    def draw(self, screen):

        frame = pygame.Rect(self.x_sprite * 80, self.y_sprite, 80, 80)

        screen.blit(self.sprite, self.rect, frame)
