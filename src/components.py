import logging
import pygame as pg

class ImageSprite(pg.sprite.Sprite):
    def __init__(self, game, path):
        super().__init__()
        self.game = game
        self.image = pg.image.load(path);
        self.image.set_colorkey((0,0,0));
        self.rect = self.image.get_rect()

class TextSprite(pg.sprite.Sprite):
    def __init__(self, game, font_path, text="", size = 10, color = (0, 0, 0)):
        super().__init__()
        self.game = game
        self.font_path = font_path
        self.draw_text(text, size, color) 

    def draw_text(self, text, size = 10, color = (0,0,0), alias = True):
        self.text = text
        self.image = self.get_font_size(size).render(text, alias, color)
        self.rect = self.image.get_rect()

    def get_font_size(self, size):
        return pg.font.Font(self.font_path, size)
