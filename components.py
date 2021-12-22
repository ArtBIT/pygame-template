import logging
import pygame as pg

class ImageSprite(pg.sprite.Sprite):
    def __init__(self, game, path):
        super().__init__()
        self.game = game
        self.image = pg.image.load(path);
        self.image.set_colorkey((0,0,0));
        self.rect = self.image.get_rect()
