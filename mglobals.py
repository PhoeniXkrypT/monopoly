
import pygame

DISPLAY_W, DISPLAY_H = 1200, 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BROWN = (165, 42, 42)
PURPLE = (128,0,128)
SKY_BLUE = (576, 226, 255)
DEEP_SKY_BLUE = (0, 191, 255)
DARK_BLUE = (0, 0, 139)
ROYAL_BLUE = (65, 105, 225)
PINK = (255, 0, 255)
ORANGE = (255, 140, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARKER_YELLOW = (200, 160, 30)
GREEN = (0, 255, 0)
SEA_GREEN = (46, 139, 87)
BLUE = (0, 0, 255)

color_map = {
        'purple': PURPLE,
        'black': BLACK,
        'brown': BROWN,
        'sky_blue': DEEP_SKY_BLUE,
        'pink': PINK,
        'orange': ORANGE,
        'red': RED,
        'yellow': DARKER_YELLOW,
        'green': GREEN,
        'blue': BLUE,
        'sea_green': SEA_GREEN,
        'royal_blue': ROYAL_BLUE,
};

fontsize_map = {
        'big': 50,
        'mid': 25,
        'small': 14,
};

GD = None
CLK = None
BACK_IMG = None
P1_IMG = None
PvAI = False
CASH_INITIAL = 1500

def load_imgs():
    global BACK_IMG, P1_IMG
    BACK_IMG = pygame.image.load('pics/board-800.jpg')
    P1_IMG = pygame.image.load('pics/man1.png')
    BACK_IMG = pygame.transform.scale(BACK_IMG, (DISPLAY_W - 400, DISPLAY_H))
    P1_IMG = pygame.transform.scale(P1_IMG, (int(DISPLAY_W*0.1), int(DISPLAY_H*0.1)))

def init_pygame():
    global GD, CLK
    pygame.init()
    GD = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption('Monopoly')
    CLK = pygame.time.Clock()


def init():
    init_pygame()
    load_imgs()
