"""
This module contains the various states that the game can be in. Each state is a class that inherits from the State class.

The State class is a base class that contains the basic functionality that every state should have. It is not meant to be used directly.

The State class has the following methods:
    boot: called when the state is first initialized
    update: called on every frame
    enter: called when the state becomes the current state
    exit: called when the state is no longer the current state
    draw: called on every frame

The State class has the following attributes:
    game: the game object
    all_sprites: a sprite group that contains all the sprites in the state
"""

import os
import pygame as pg
from components import *

class State:
    """
    Base class for all states
    """
    def __init__(self, game):
        """
        game: game object
        """
        self.game = game
        # all sprites in the state
        self.all_sprites = pg.sprite.Group()
        self.boot()

    def boot(self):
        """
        Called when the state is first initialized
        """
        # override this method to add logic that happens when the state is first initialized
        pass

    def update(self):
        """
        Called on every frame
        """
        # override this method to add logic that happens on every frame
        self.all_sprites.update()

    def enter(self):
        """
        Called when the state becomes the current state
        """
        # override this method to add logic that happens when this state becomes the current state
        pass

    def exit(self):
        """
        Called when the state is no longer the current state
        """
        # override this method to add logic that happens when changing
        # from this state to some other state
        pass

    def draw(self, screen):
        """
        Called on every frame
        """
        self.all_sprites.draw(screen)

class Intro(State):
    """
    Intro state
    """
    def boot(self):
        # load the intro sound
        self.game.audio.load_sound('intro', os.path.join('assets', 'sounds', 'intro.wav'))
        # add a background image
        self.all_sprites.add(ImageSprite(self.game, os.path.join('assets', 'images', 'test.jpg')))
        # add some text
        text = TextSprite(self.game, os.path.join('assets', 'fonts', 'PressStart2P-Regular.ttf'),
                "Intro", 24, color = (255,255,255))
        # center text on screen
        text.rect.center = self.game.screen.get_rect().center
        # add the text to the all_sprites group
        self.all_sprites.add(text)
        # add some more text
        any_key_text = TextSprite(self.game,
                os.path.join('assets', 'fonts', 'PressStart2P-Regular.ttf'),
                "Press any key to switch to Outro", 12, color = (255,255,255))
        any_key_text.rect.center = self.game.screen.get_rect().center
        any_key_text.rect.top = text.rect.bottom + 10
        # add the text to the all_sprites group
        self.all_sprites.add(any_key_text)

    def enter(self):
        # when the state becomes the current state, play the intro sound
        self.game.audio.play('intro')

    def update(self):
        # on every frame, call the update method of the base class
        super().update()
        # check if any key is pressed
        if self.game.input.is_key_pressed('any'):
            # if any key is pressed, change the state to Outro
            self.game.change_state('Outro')

class Outro(State):
    """
    Outro state
    """
    def boot(self):
        # add some text
        text = TextSprite(self.game,
                os.path.join('assets', 'fonts', 'PressStart2P-Regular.ttf'),
                "Outro", 24, color = (255,255,255))
        # center text on screen
        text.rect.center = self.game.screen.get_rect().center
        # add the text to the all_sprites group
        self.all_sprites.add(text)

        # add the "any key" text
        any_key_text = TextSprite(self.game,
                os.path.join('assets', 'fonts', 'PressStart2P-Regular.ttf'),
                "Press any key to quit", 12, color = (255,255,255))
        any_key_text.rect.center = self.game.screen.get_rect().center
        any_key_text.rect.top = text.rect.bottom + 10
        # add the text to the all_sprites group
        self.all_sprites.add(any_key_text)

    def update(self):
        super().update()
        # check if any key is pressed
        if self.game.input.is_key_pressed('any'):
            self.game.quit()

# add the states to the __all__ list
# this is needed so that the states can be imported using the * syntax
# the first item in the list is the default state
__all__ = ['Intro', 'Outro']
