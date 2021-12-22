import os
import logging
import pygame as pg
from components import *

class State:
    def __init__(self, game):
        self.game = game
        self.boot()

    def boot(self):
        pass

    def update(self):
        pass

    def enter(self):
        pass

    def exit(self):
        pass

class Intro(State):
    def boot(self):
        self.game.audio.load_sound('intro', os.path.join('assets', 'sounds', 'intro.wav'))
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(ImageSprite(self.game, os.path.join('assets', 'images', 'test.jpg')))
        text = TextSprite(self.game, os.path.join('assets', 'fonts', 'PressStart2P-Regular.ttf'), "Hello World", 24, color = (255,255,255))
        # center text on screen
        text.rect.center = self.game.screen.get_rect().center
        self.all_sprites.add(text)


    def enter(self):
        self.game.audio.play('intro')

    def update(self):
        self.all_sprites.update()

    def draw(self, screen):
        self.all_sprites.draw(screen)
