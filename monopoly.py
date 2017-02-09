
import pygame
import time
import collections

import ui
import mglobals
import utils
import property as _property

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

    mglobals.PLAYER_OBJ[mglobals.PLAYER_ONE] = P1
    mglobals.PLAYER_OBJ[mglobals.PLAYER_TWO] = P2

    P1.pm.render()
    P2.pm.render()

    P1.buy_property(1)
    P1.buy_property(11)
    P1.buy_property(32)
    P2.buy_property(8)
    P2.buy_property(15)
    P2.buy_property(39)

    currentplayer, otherplayer = P1, P2
    double_count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    utils.draw_board()
                    currentplayer.ps.hide()
                    currentplayer.ps.advance()
                    currentplayer.ps.show()
                    otherplayer.ps.render()
                    currentplayer.pm.render()
                    otherplayer.pm.render()

                elif event.key == pygame.K_RIGHT:
                    utils.draw_board()
                    currentplayer.ps.hide()
                    currentplayer.ps.goback()
                    currentplayer.ps.show()
                    otherplayer.ps.render()
                    currentplayer.pm.render()
                    otherplayer.pm.render()

                # Dice roll
                elif event.key == pygame.K_d:
                    utils.draw_board()
                    mglobals.CHANCE_MAP[mglobals.CHANCE_CHEST_VALUE].unset_x_y()
                    mglobals.CHEST_MAP[mglobals.CHANCE_CHEST_VALUE].unset_x_y()
                    mglobals.DICEOBJ.hide()
                    currentplayer.ps.hide()
                    val, double = mglobals.DICEOBJ.roll()
                    currentplayer.pm.advance(val)
                    otherplayer.pm.render()

                    """
                    #TODO count = 3 goto Jail
                    if double:
                        double_count += 1
                    if double_count == 0:
                        currentplayer, otherplayer = otherplayer, currentplayer
                        print currentplayer.player_name, otherplayer.player_name
                    elif double_count == 3:
                        currentplayer, otherplayer = otherplayer, currentplayer
                        double_count = 0
                    """

                # Buy property
                elif event.key == pygame.K_b:
                    utils.draw_board()
                    currentplayer.pm.render()
                    otherplayer.pm.render()
                    currentplayer.buy_property(currentplayer.pm.position)

                # Mortgage property
                elif event.key == pygame.K_m:
                    utils.draw_board()
                    currentplayer.pm.render()
                    otherplayer.pm.render()
                    currentplayer.ps.show()
                    currentplayer.mortgage_property(currentplayer.ps.position)

                # Unmortgage property
                elif event.key == pygame.K_u:
                    utils.draw_board()
                    currentplayer.pm.render()
                    otherplayer.pm.render()
                    currentplayer.ps.show()
                    currentplayer.unmortgage_property(currentplayer.ps.position)

                # Build house/hotel
                elif event.key == pygame.K_h:
                    utils.draw_board()
                    currentplayer.pm.render()
                    otherplayer.pm.render()
                    currentplayer.ps.show()
                    currentplayer.build_house(currentplayer.ps.position)

        mglobals.DICE_DISPLAY.update()
        mglobals.DICE_DISPLAY.draw(mglobals.GD)
        mglobals.CENTRE_DISPLAYS.update()
        mglobals.CENTRE_DISPLAYS.draw(mglobals.GD)
        mglobals.PROPERTY_DISPLAYS.update()
        mglobals.PROPERTY_DISPLAYS.draw(mglobals.GD)
        mglobals.HOUSE_COUNT_DISPLAYS.update()
        mglobals.HOUSE_COUNT_DISPLAYS.draw(mglobals.GD)
        mglobals.CHESTCHANCE_DISPLAYS.update()
        mglobals.CHESTCHANCE_DISPLAYS.draw(mglobals.GD)

        pygame.display.update()
        mglobals.CLK.tick(30)

def main():
    mglobals.init()
    player_menu_loop()
    ui.init_dice()
    ui.init_chestchance()
    ui.init_centre_displays()
    ui.init_property_displays()
    ui.init_house_count_displays()
    _property.init_pobject_map()
    game_loop()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()

