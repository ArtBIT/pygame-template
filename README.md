# PyGame Template
![GitHub issues badge](https://img.shields.io/github/issues/ArtBIT/pygame-template)
![GitHub forks badge](https://img.shields.io/github/forks/ArtBIT/pygame-template)
![GitHub stars badge](https://img.shields.io/github/stars/ArtBIT/pygame-template)
![GitHub license badge](https://img.shields.io/github/license/ArtBIT/pygame-template)


### What is this?
This is a basic project template for [PyGame](https://www.pygame.org/)
It contains the basic pygame setup, the basic game loop, and input and sound helpers.

---

### Usage
Clone this repo

    git clone https://github.com/ArtBIT/pygame-template

Install PyGame if you haven't already

    python3 -m pip install -U pygame --user

And run the main.py

    python3 src/main.py

### Example

```
# src/states.py

class State:
...

class Intro(State):
    def boot(self):
        self.game.audio.load_sound('intro', os.path.join('assets', 'sounds', 'intro.wav'))
        
        # Show "Press any key" centered on screen
        font_path = os.path.join('assets', 'fonts', 'PressStart2P-Regular.ttf')
        text = "Press any key to switch to Outro"
        any_key_text = TextSprite(self.game, font_path, text, 12, color = (255,255,255))
        any_key_text.rect.center = self.game.screen.get_rect().center
        self.all_sprites.add(any_key_text)

    def enter(self):
        # When this state is entered, play the intro sound
        self.game.audio.play('intro')

    def update(self):
        # On every frame, update all the sprites and check for keypress
        super().update();
        if self.game.input.is_key_pressed('any'):
            # you can change to a different state
            # self.game.change_state('Outro')
            # but for this example we simply quit
            self.game.quit()

...

# Define the export order of the states. src/game.py will atomatically register all the states and load the first one
__all__ = ['Intro']
```

# Credits

Intro sound is from https://freesound.org/s/438921/ licensed under [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/).

# License
MIT
