"""
This is the main game file. It is responsible for the game loop and
changing states.
"""

import os
import sys
import logging
import pygame as pg
from input import Input
from audio import Audio
from settings import *
from components import *
import states

class Game:
    """
    Main game class
    """
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_TITLE)
        self.clock = pg.time.Clock()
        self.input = Input()
        self.audio = Audio()
        self.init_states()

    def register_state(self, state):
        """
        Register a state

        state: state object
        """
        self.states[type(state).__name__] = state

    def init_states(self):
        """
        Initialize all the states
        """
        self.state = None
        self.states = {}
        # iterate over __all__ states from states.py instantiate them
        # and register to the self.states with state.name as the key and state instance 
        # as value
        for State in map(states.__dict__.get, states.__all__):
            self.register_state(State(self))

        # initialize the first state
        first_state = list(self.states.keys())[0]
        self.change_state(first_state)

    def change_state(self, state):
        """
        Change the current state

        state: name of the state to change to
        """
        if state in self.states.keys():
            # exit the current state
            if self.state:
                self.state.exit()
            # enter the new state
            self.state = self.states[state]
            self.state.enter()

    def loop(self):
        """
        Main game loop
        """
        self.is_playing = True
        while self.is_playing:
            # quit the game if escape is pressed
            if self.input.is_key_down("escape"):
                self.quit()
            # elapsed time in ms
            self.ms = pg.time.get_ticks()
            # elapsed time since last frame 
            self.dt = self.clock.tick(FPS) / 1000
            # handle events
            self.handle_events()
            # update and draw
            self.update()
            self.draw()

    def quit(self):
        """
        Quit the game
        """
        pg.quit()
        sys.exit()

    def handle_events(self):
        """
        Handle events
        """
        self.input.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            self.input.handle_event(event)

    def update(self):
        """
        Update the game (update the current state)
        """
        if self.state:
            self.state.update()

    def draw(self):
        """
        Draw the game (draw the current state)
        """
        # clear the screen
        self.screen.fill(BACKGROUND_COLOR)
        # draw the current state
        if self.state:
            self.state.draw(self.screen)
        # flip the display
        pg.display.flip()
