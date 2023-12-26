"""
This file contains the classes for the components of the game
"""

import pygame as pg

class ImageSprite(pg.sprite.Sprite):
    """
    Sprite class for loading and displaying images
    """
    def __init__(self, game, path):
        """
        game: game object
        path: path to the image file
        """

        super().__init__()
        self.game = game
        # load the image
        self.image = pg.image.load(path)
        # set the colorkey to black
        self.image.set_colorkey((0,0,0))
        # get the rect
        self.rect = self.image.get_rect()

class TextSprite(pg.sprite.Sprite):
    """
    Sprite class for displaying text
    """
    def __init__(self, game, font_path, text="", size = 10, color = (0, 0, 0)):
        """
        game: game object
        font_path: path to the font file
        text: text to display
        size: font size
        color: font color
        """
        super().__init__()
        self.game = game
        self.font_path = font_path
        self.draw_text(text, size, color)

    def draw_text(self, text, size = 10, color = (0,0,0), alias = True):
        """
        Draw the text

        text: text to display
        size: font size
        color: font color
        alias: whether to use anti-aliasing
        """
        self.text = text
        self.image = self.get_font_size(size).render(text, alias, color)
        self.rect = self.image.get_rect()

    def get_font_size(self, size):
        """
        Get the font object with the given size
        """
        return pg.font.Font(self.font_path, size)
