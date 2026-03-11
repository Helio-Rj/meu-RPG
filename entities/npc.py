import pygame


class NPC:

    def __init__(self, x, y):

        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 200, 0))  # cor do npc

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.dialogue = "Voce viu meu gato Lua?"

        self.responses = [
            "1 - Vou procurar seu gato",
            "2 - Agora nao posso ajudar"
        ]

    def draw(self, screen):

        screen.blit(self.image, self.rect)