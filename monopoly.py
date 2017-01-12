
import pygame
import time
import collections

import mglobals
import utils
import property as _property

from ui import PlayerInfoUI
import ui
from player import Player, PlayerSelection, PlayerMovement

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
    utils.draw_board()

    """
    prop = collections.defaultdict(list)
    prop2 = collections.defaultdict(list)

    x = 0
    for i in _property.PROPERTIES:
        if x == 0:
            prop[i.color].append(i.property_name)
            x = 1
        elif x == 1:
            prop2[i.color].append(i.property_name)
            x = 0
    """
    # p1 = PlayerInfoUI(mglobals.PLAYER_ONE, 'royal_blue')
    # p1.update_properties(prop)
    # p2 = PlayerInfoUI(mglobals.PLAYER_TWO, 'sea_green')
    # p2.update_properties(prop)

    # p1.render()
    # p2.render()

    # utils.clear_p2_info()

    # ps1 = PlayerSelection(1, 'royal_blue')
    # ps1.render()

    P1 = Player(mglobals.PLAYER_ONE)
    P2 = Player(mglobals.PLAYER_TWO)
    P1.pm.render()
    P2.pm.render()

    #P1.test_set_property(prop)
    #P2.test_set_property(prop2)

    currentplayer, otherplayer = P1, P2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    utils.draw_board()
                    mglobals.DICEOBJ.hide()
                    currentplayer.ps.hide()
                    currentplayer.ps.advance()
                    currentplayer.ps.show()
                    otherplayer.ps.render()
                    currentplayer.pm.render()
                    otherplayer.pm.render()

                elif event.key == pygame.K_RIGHT:
                    utils.draw_board()
                    mglobals.DICEOBJ.hide()
                    currentplayer.ps.hide()
                    currentplayer.ps.goback()
                    currentplayer.ps.show()
                    otherplayer.ps.render()
                    currentplayer.pm.render()
                    otherplayer.pm.render()

                # Dice roll
                elif event.key == pygame.K_d:
                    utils.draw_board()
                    mglobals.DICEOBJ.hide()
                    currentplayer.ps.hide()
                    val, double = mglobals.DICEOBJ.roll()
                    currentplayer.pm.advance(val)
                    otherplayer.pm.render()

                # Buy property
                elif event.key == pygame.K_b:
                    utils.draw_board()
                    utils.clear_p1_info()
                    mglobals.DICEOBJ.hide()
                    currentplayer.pm.render()
                    otherplayer.pm.render()
                    currentplayer.buy_property(currentplayer.pm.position)

                # Mortgage property

                # Unmortgage property

        mglobals.CENTRE_DISPLAYS.update()
        mglobals.CENTRE_DISPLAYS.draw(mglobals.GD)
        mglobals.PROPERTY_DISPLAYS.update()
        mglobals.PROPERTY_DISPLAYS.draw(mglobals.GD)
        mglobals.DICE_DISPLAY.update()
        mglobals.DICE_DISPLAY.draw(mglobals.GD)

        pygame.display.update()
        mglobals.CLK.tick(30)

def main():
    mglobals.init()
    player_menu_loop()
    ui.init_property_displays()
    ui.init_centre_displays()
    ui.init_dice()
    _property.init_pobject_map()
    game_loop()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()

