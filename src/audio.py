"""
Audio class for loading and playing sounds
"""
import logging
import pygame as pg

class Audio:
    """
    Audio class for loading and playing sounds
    """
    def __init__(self):
        self.sounds = {}

    def load_sound(self, name, path):
        """
        Load a sound file

        name: name of the sound
        path: path to the sound file
        """
        if name in self.sounds:
            logging.warning("Sound %s already loaded", name)
            return
        self.sounds[name] = pg.mixer.Sound(path)

    def load_sounds(self, sounds):
        """
        Load multiple sounds

        sounds: dictionary of sounds, where the key is the name of the
                sound and the value is the path to the sound file
        """
        for name in sounds:
            self.load_sound(name, sounds[name])

    def play(self, name):
        """
        Play a sound

        name: name of the sound
        """
        if name in self.sounds:
            self.sounds[name].play()

    def stop(self, name=None):
        """
        Stop a sound

        name: name of the sound
        """
        if name is None:
            # stop all
            for sound_name in self.sounds:
                self.sounds[sound_name].stop()
        else:
            if name in self.sounds:
                self.sounds[name].stop()
