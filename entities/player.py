import pygame
from core.settings import PLAYER_SPEED


class Player:

    def __init__(self, x, y):

        self.sprite = pygame.image.load(
            "assets/sprites/player.png"
        ).convert_alpha()

        self.rect = pygame.Rect(x, y, 58, 58)

        # animação
        self.x_sprite = 0
        self.y_sprite = 0

        self.frame_width = 96
        self.frame_height = 96

        self.animation_timer = 0
        self.animation_speed = 8

    def update(self):

        keys = pygame.key.get_pressed()

        moving = False

        # ↓ frente
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED
            self.y_sprite = 0
            moving = True

        # ↑ costas
        elif keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
            self.y_sprite = 1
            moving = True

        # ← esquerda
        elif keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
            self.y_sprite = 2
            moving = True

        # → direita
        elif keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
            self.y_sprite = 3
            moving = True

        # animação
        if moving:
            self.animation_timer += 1

            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.x_sprite += 1

                if self.x_sprite > 2:
                    self.x_sprite = 0
        else:
            self.x_sprite = 1  # frame parado (meio)

    def draw(self, screen):

        frame = pygame.Rect(
            self.x_sprite * self.frame_width + 6,  # ajuste fino X
            self.y_sprite * self.frame_height + 12,  # ajuste fino Y
            self.frame_width - 32,  # corta sobra lateral
            self.frame_height - 32,  # corta sobra vertical

        )

        screen.blit(self.sprite, self.rect, frame)
