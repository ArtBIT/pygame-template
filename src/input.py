import logging
import pygame as pg
from pygame.locals import *

class Input:
    def __init__(self):
        self.keys_down = set()
        self.keys_pressed = set()
        self.modifier_key_names = dict(zip((pg.KMOD_LSHIFT, pg.KMOD_RSHIFT, pg.KMOD_SHIFT, pg.KMOD_LCTRL, pg.KMOD_RCTRL, pg.KMOD_CTRL, pg.KMOD_LALT, pg.KMOD_RALT, pg.KMOD_ALT, pg.KMOD_LMETA, pg.KMOD_RMETA, pg.KMOD_META, pg.KMOD_CAPS, pg.KMOD_NUM, pg.KMOD_MODE), ('lshift', 'rshift', 'shift', 'lctrl', 'rctrl', 'ctrl', 'lalt', 'ralt', 'alt', 'lmeta', 'rmeta', 'meta', 'caps', 'num', 'mode')))

    def is_key_down(self, key):
        if key == 'any':
            return len(self.keys_down) > 0
        return key in self.keys_down

    def is_key_pressed(self, key):
        if key == 'any':
            return len(self.keys_pressed) > 0
        return key in self.keys_pressed

    def update(self):
        self.keys_pressed = set()

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.mod == pg.KMOD_NONE:
                key_name = pg.key.name(event.key)
                self.keys_down.add(key_name)
                self.keys_pressed.add(key_name)
            else:
                for key in self.modifier_key_names.keys():
                    if event.mod & key:
                        key_name = self.modifier_key_names[key]
                        self.keys_down.add(key_name)
                        self.keys_pressed.add(key_name)

        if event.type == pg.KEYUP:
            if event.mod == pg.KMOD_NONE:
                key_name = pg.key.name(event.key)
                self.keys_down.discard(key_name)
            else:
                for key in self.modifier_key_names.keys():
                    if event.mod & key:
                        key_name = self.modifier_key_names[key]
                        self.keys_down.discard(key_name)
