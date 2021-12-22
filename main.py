import os
import sys
import logging
import pygame as pg
from input import Input
from audio import Audio
from settings import *
from components import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_TITLE)
        self.clock = pg.time.Clock()
        self.input = Input()
        self.audio = Audio()
        self.load()
        self.boot()

    def load(self):
        self.audio.load_sound('intro', os.path.join('assets', 'sounds', 'intro.wav'))

    def boot(self):
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(ImageSprite(self, os.path.join('assets', 'images','test.jpg')))
        self.audio.play('intro')

    def loop(self):
        self.is_playing = True
        while self.is_playing:
            if self.input.is_key_down("escape"):
                self.quit()
            self.dt = self.clock.tick(FPS) / 1000
            self.handle_events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def handle_events(self):
        self.input.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            self.input.handle_event(event)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

game = Game()
while True:
    game.loop()
