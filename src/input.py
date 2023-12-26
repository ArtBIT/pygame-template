"""
This module handles input from the user.
"""

import logging
import pygame as pg
import pygame.constants as pgc
from pygame.locals import *

class Input:
    """
    Input class for handling input from the user
    """
    def __init__(self):
        self.keys_down = set()
        self.keys_pressed = set()
        # map modifier key values to aliases
        pygame_keys = (pgc.KMOD_LSHIFT, pgc.KMOD_RSHIFT, pgc.KMOD_SHIFT,
            pgc.KMOD_LCTRL, pgc.KMOD_RCTRL, pgc.KMOD_CTRL, pgc.KMOD_LALT,
            pgc.KMOD_RALT, pgc.KMOD_ALT, pgc.KMOD_LMETA, pgc.KMOD_RMETA,
            pgc.KMOD_META, pgc.KMOD_CAPS, pgc.KMOD_NUM, pgc.KMOD_MODE)
        keys_aliases = ('lshift', 'rshift', 'shift', 'lctrl', 'rctrl', 'ctrl', 'lalt', 'ralt', 'alt', 'lmeta', 'rmeta', 'meta', 'caps', 'num', 'mode')
        self.modifier_key_names = dict(zip(pygame_keys, keys_aliases))

    def is_key_down(self, key):
        """
        Check if a key is down

        key: key to check
        """
        if key == 'any':
            return len(self.keys_down) > 0
        return key in self.keys_down

    def is_key_pressed(self, key):
        """
        Check if a key is pressed
        A key is considered pressed if it was pressed in the current frame

        key: key to check
        """
        if key == 'any':
            return len(self.keys_pressed) > 0
        return key in self.keys_pressed

    def update(self):
        self.keys_pressed = set()

    def handle_event(self, event):
        """
        Handle an event
        Input class cares only about key events (KEYDOWN and KEYUP)

        event: event to handle
        """
        if event.type == pgc.KEYDOWN:
            if event.mod == pgc.KMOD_NONE:
                # If the key is not a modifier key, add the alias to the keys_down set
                key_name = pgc.key.name(event.key)
                self.keys_down.add(key_name)
                self.keys_pressed.add(key_name)
            else:
                # if the key is a modifier key, add the alias to the keys_down set
                for key in self.modifier_key_names.keys():
                    if event.mod & key:
                        key_name = self.modifier_key_names[key]
                        self.keys_down.add(key_name)
                        self.keys_pressed.add(key_name)

        if event.type == pgc.KEYUP:
            if event.mod == pgc.KMOD_NONE:
                # If the key is not a modifier key, remove the alias from the keys_down set
                key_name = pgc.key.name(event.key)
                self.keys_down.discard(key_name)
            else:
                # if the key is a modifier key, remove the alias from the keys_down set
                for key in self.modifier_key_names.keys():
                    if event.mod & key:
                        key_name = self.modifier_key_names[key]
                        self.keys_down.discard(key_name)
