import logging
import pygame as pg

class Audio:
    def __init__(self):
        self.sounds = {}

    def load_sound(self, name, path):
        self.sounds[name] = pg.mixer.Sound(path)

    def load_sounds(self, sounds):
        for name in sounds:
            self.load_sound(name, sounds[name])

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()

    def stop(self, name=None):
        if name is None:
            # stop all
            for name in self.sounds:
                self.sounds[name].stop()
        else:
            if name in self.sounds:
                self.sounds[name].stop()
