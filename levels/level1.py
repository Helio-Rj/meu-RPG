import pygame

from entities.player import Player


class Level1:

    def __init__(self, game):

        self.game = game

        self.player = Player(400, 300)

    def update(self):

        self.player.update()

    def draw(self, screen):

        self.player.draw(screen)