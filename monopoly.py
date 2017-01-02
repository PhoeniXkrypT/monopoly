
import pygame
import time

import mglobals
import utils

def player_menu_loop():
    one, two = 'black', 'blue'
    utils.draw_player_menu(one, two)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                    one, two = two, one
                    utils.draw_player_menu(one, two)

                elif event.key == pygame.K_RETURN:
                    print one, two
                    return


        pygame.display.update()
        mglobals.CLK.tick(30)

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                utils.draw_background()

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

