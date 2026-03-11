import pygame

from core.settings import *
from levels.level1 import Level1


class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        # level atual
        self.level = Level1(self)

    def run(self):

        while self.running:

            self.clock.tick(FPS)

            self.events()
            self.update()
            self.draw()

        pygame.quit()

    def events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

    def update(self):

        self.level.update()

    def draw(self):

        self.screen.fill(GRAY)

        self.level.draw(self.screen)

        pygame.display.flip()