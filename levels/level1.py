import pygame
from entities.player import Player
from entities.npc import NPC


class Level1:

    def __init__(self, game):

        self.game = game

        self.player = Player(400, 300)
        self.npc = NPC(200, 200)

        self.show_dialogue = False
        self.player_response = None

        self.font = pygame.font.Font(None, 28)

    def update(self):

        self.player.update()

        keys = pygame.key.get_pressed()

        # iniciar conversa
        if self.player.rect.colliderect(self.npc.rect):

            if keys[pygame.K_e]:
                self.show_dialogue = True

        # respostas
        if self.show_dialogue:

            if keys[pygame.K_1]:
                self.player_response = "Vou encontrar seu gato!"
                self.show_dialogue = False

            if keys[pygame.K_2]:
                self.player_response = "Talvez depois..."
                self.show_dialogue = False

    def draw(self, screen):

        self.npc.draw(screen)
        self.player.draw(screen)

        if self.show_dialogue:

            text = self.font.render(self.npc.dialogue, True, (255,255,255))
            screen.blit(text, (50,520))

            y = 550

            for response in self.npc.responses:

                r = self.font.render(response, True, (200,200,200))
                screen.blit(r,(50,y))

                y += 25

        if self.player_response:

            response_text = self.font.render(
                self.player_response,
                True,
                (150,255,150)
            )

            screen.blit(response_text,(50,480))
