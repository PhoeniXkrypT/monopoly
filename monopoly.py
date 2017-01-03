
import pygame
import time

import mglobals
import utils

from ui import PlayerInfoUI
from player import PlayerSelection

def player_menu_loop():
    one, two = 'black', 'blue'
    utils.draw_player_menu(one, two)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                    one, two = two, one
                    utils.draw_player_menu(one, two)

                elif event.key == pygame.K_RETURN:
                    if (one, two) == ('black', 'blue'):
                        PvAI = True
                        return
                    elif (one, two) == ('blue', 'black'):
                        PvAI = False
                        return

        pygame.display.update()
        mglobals.CLK.tick(30)

def game_loop():
    utils.draw_background()
    prop ={
            'blue':['North Carolina Avenue']*2,
            'purple':['Mediteranean Avenue']*2,
            'sky_blue':['North Carolina Avenue']*3,
            'pink':['North Carolina Avenue']*3,
            'orange':['North Carolina Avenue']*3,
            'red':['North Carolina Avenue']*3,
            'yellow':['North Carolina Avenue']*3,
            'green':['North Carolina Avenue']*3,
    }
    p1 = PlayerInfoUI(mglobals.PLAYER_ONE)
    p1.update_properties(prop)
    p2 = PlayerInfoUI(mglobals.PLAYER_TWO)
    p2.update_properties(prop)
    p1.render(); p2.render();

    ps1 = PlayerSelection(1, 'royal_blue')
    ps1.render()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    utils.draw_background()
                    ps1.advance()
                elif event.key == pygame.K_RIGHT:
                    utils.draw_background()
                    ps1.goback()

        pygame.display.update()
        mglobals.CLK.tick(30)

def main():
    mglobals.init()
    player_menu_loop()
    game_loop()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()

