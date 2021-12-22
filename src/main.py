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
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_TITLE)
        self.clock = pg.time.Clock()
        self.input = Input()
        self.audio = Audio()
        self.init_states()

    def init_states(self):
        self.state = None
        self.states = {}
        # iterate over __all__ states from states.py instantiate them
        # and register to the self.states with state.name as the key and state instance 
        # as value
        for State in map(states.__dict__.get, states.__all__):
            state = State(self)
            name = type(state).__name__
            self.states[name] = state

        # initialize the first state
        first_state = list(self.states.keys())[0]
        self.change_state(first_state)

    def change_state(self, state):
        if state in self.states.keys():
            if self.state:
                self.state.exit()
            self.state = self.states[state]
            self.state.enter()

    def loop(self):
        self.is_playing = True
        while self.is_playing:
            if self.input.is_key_down("escape"):
                self.quit()
            # elapsed time in ms
            self.ms = pg.time.get_ticks()
            # elapsed time since last frame 
            self.dt = self.clock.tick(FPS) / 1000
            self.handle_events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def handle_events(self):
        self.input.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            self.input.handle_event(event)

    def update(self):
        if self.state:
            self.state.update()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        if self.state:
            self.state.draw(self.screen)
        pg.display.flip()

game = Game()
while True:
    game.loop()
