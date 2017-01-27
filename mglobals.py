
import pygame
import collections

DISPLAY_W, DISPLAY_H = 1200, 800
BOARD_WIDTH = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BROWN = (165, 42, 42)
PURPLE = (128,0,128)
BLUE = (0, 0, 255)
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
GRAY = (169,169,169)

PLAYER_ONE = 'Player 1'
PLAYER_TWO = 'Player 2'

PLAYER_ONE_COLOR = 'royal_blue'
PLAYER_TWO_COLOR = 'sea_green'

PLAYER_AI  = 'Player AI'
BANK       = 'BANK'

BOARD_SQUARES = 40

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
        'white': WHITE,
        'gray': GRAY,
};

fontsize_map = {
        'big': 50,
        'mid': 25,
        'small': 12,
};

GD = None
CLK = None
BACK_IMG = None
P1_IMG = None
P2_IMG = None
PvAI = False
CASH_INITIAL = 1500
P_INFO_CLRSCR = None

PLAYER_OBJ = {}
DICEOBJ = None
DICE_NUMBER_MAP = {}
DICE_DISPLAY = pygame.sprite.Group()
PROPERTY_NAME_SPRITE_MAP = {}
PROPERTY_DISPLAYS = pygame.sprite.Group()
CENTRE_DISPLAYS = pygame.sprite.Group()
POBJECT_MAP = {}
PROP_COLOR_INDEX = collections.defaultdict(list)
INDEX_PROPPIC_MAP = {}

def load_imgs():
    global BACK_IMG, P1_IMG, P2_IMG, P_INFO_CLRSCR
    BACK_IMG = pygame.image.load('pics/board_uk.jpg')
    P1_IMG = pygame.image.load('pics/p1.png')
    P2_IMG = pygame.image.load('pics/p2.png')
    BACK_IMG = pygame.transform.scale(BACK_IMG, (DISPLAY_W - 400, DISPLAY_H))
    #P1_IMG = pygame.transform.scale(P1_IMG, (int(DISPLAY_W*0.1), int(DISPLAY_H*0.1)))
    P_INFO_CLRSCR = pygame.Surface([380, 400])

def init_pygame():
    global GD, CLK
    pygame.init()
    GD = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption('Monopoly')
    CLK = pygame.time.Clock()
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

def init():
    init_pygame()
    load_imgs()
