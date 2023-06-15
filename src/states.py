import os
import logging
import pygame as pg
from components import *

class State:
    def __init__(self, game):
        self.game = game
        self.all_sprites = pg.sprite.Group()
        self.boot()

    def boot(self):
        # override this method to add logic that happens when the state is first initialized
        pass

    def update(self):
        # override this method to add logic that happens on every frame
        self.all_sprites.update()

    def enter(self):
        # override this method to add logic that happens when this state becomes the current state
        pass

    def exit(self):
        # override this method to add logic that happens when changing from this state to some other state
        pass

    def draw(self, screen):
        self.all_sprites.draw(screen)

class Intro(State):
    def boot(self):
        self.game.audio.load_sound('intro', os.path.join('assets', 'sounds', 'intro.wav'))
        self.all_sprites.add(ImageSprite(self.game, os.path.join('assets', 'images', 'test.jpg')))
        text = TextSprite(self.game, os.path.join('assets', 'fonts', 'PressStart2P-Regular.ttf'), "Intro", 24, color = (255,255,255))
        # center text on screen
        text.rect.center = self.game.screen.get_rect().center
        self.all_sprites.add(text)
        any_key_text = TextSprite(self.game, os.path.join('assets', 'fonts', 'PressStart2P-Regular.ttf'), "Press any key to switch to Outro", 12, color = (255,255,255))
        any_key_text.rect.center = self.game.screen.get_rect().center
        any_key_text.rect.top = text.rect.bottom + 10
        self.all_sprites.add(any_key_text)


    def enter(self):
        self.game.audio.play('intro')

    def update(self):
        super().update()
        if self.game.input.is_key_pressed('any'):
            self.game.change_state('Outro')

class Outro(State):
    def boot(self):
        text = TextSprite(self.game, os.path.join('assets', 'fonts', 'PressStart2P-Regular.ttf'), "Outro", 24, color = (255,255,255))
        # center text on screen
        text.rect.center = self.game.screen.get_rect().center
        any_key_text = TextSprite(self.game, os.path.join('assets', 'fonts', 'PressStart2P-Regular.ttf'), "Press any key to quit", 12, color = (255,255,255))
        any_key_text.rect.center = self.game.screen.get_rect().center
        any_key_text.rect.top = text.rect.bottom + 10
        self.all_sprites.add(any_key_text)
        self.all_sprites.add(text)

    def update(self):
        super().update()
        if self.game.input.is_key_pressed('any'):
            self.game.quit()

__all__ = ['Intro', 'Outro']
