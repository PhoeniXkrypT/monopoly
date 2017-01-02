
import pygame

DISPLAY_W, DISPLAY_H = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GD = None
CLK = None
BACK_IMG = None
P1_IMG = None

def load_imgs():
    global BACK_IMG, P1_IMG
    BACK_IMG = pygame.image.load('pics/board-800.jpg')
    P1_IMG = pygame.image.load('pics/man1.png')
    BACK_IMG = pygame.transform.scale(BACK_IMG, (DISPLAY_W, DISPLAY_H))
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
