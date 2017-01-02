
import pygame
import time

import mglobals
import utils

def player_menu():
    mglobals.GD.fill(mglobals.WHITE)
    utils.message_display_lines(["Monopoly!", "PvP OR PvAI"])


def game_loop():
    while True:
        for event in pygame.event.get():
            print event
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                utils.draw_background()

        pygame.display.update()
        mglobals.CLK.tick(30)

def main():
    mglobals.init()
    player_menu()
    game_loop()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()

