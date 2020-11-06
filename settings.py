import os

# game options / settings
TITLE = "Mythical Wars"
WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up directories
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")