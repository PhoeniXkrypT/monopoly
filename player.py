
import pygame
import collections

import mglobals
from ui import PlayerInfoUI

class PlayerMovement(object):
    def __init__(self):
        pass

    def advance(self, count):
        pass

    def goback(self, count):
        pass

class PlayerSelection(object):
    BOX_THICKNESS = 5
    RECT_WIDTH = 65
    RECT_HEIGHT = 106
    SQ_HEIGHT_WIDTH = 106

    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.x, self.y = 0, 0
        self.cw, self.ch = 0, 0
        self.reposition()
        self.render()

    def reposition(self):
        # If the position corresponds to a square
        if self.position % 10 == 0:
            if self.position in [0, 10]:
                self.y = mglobals.DISPLAY_H - PlayerSelection.SQ_HEIGHT_WIDTH
                self.x = 0 if self.position == 10 \
                           else mglobals.BOARD_WIDTH - PlayerSelection.SQ_HEIGHT_WIDTH
            else:
                self.y = 0
                self.x = 0 if self.position == 20 \
                           else mglobals.BOARD_WIDTH - PlayerSelection.SQ_HEIGHT_WIDTH
            self.cw, self.ch = PlayerSelection.SQ_HEIGHT_WIDTH, PlayerSelection.SQ_HEIGHT_WIDTH

        # If the position corresponds to a vertical rectangle
        elif (self.position > 0 and self.position < 10) or \
             (self.position > 20 and self.position < 30):
            if self.position > 0 and self.position < 10:
                self.y = (mglobals.DISPLAY_H - PlayerSelection.RECT_HEIGHT)
                self.x = mglobals.BOARD_WIDTH \
                         - PlayerSelection.SQ_HEIGHT_WIDTH \
                         - (PlayerSelection.RECT_WIDTH * self.position)
            else:
                self.y = 0
                self.x = PlayerSelection.SQ_HEIGHT_WIDTH \
                         + (PlayerSelection.RECT_WIDTH * ((self.position % 10) - 1))
            self.cw, self.ch = PlayerSelection.RECT_WIDTH, PlayerSelection.RECT_HEIGHT

        # If the position corresponds to a horizontal rectangle
        else:
            if self.position > 10 and self.position < 20:
                self.x = 0
                self.y = mglobals.DISPLAY_H \
                         - PlayerSelection.SQ_HEIGHT_WIDTH \
                         - (PlayerSelection.RECT_WIDTH * (self.position % 10))
            else:
                self.x = mglobals.BOARD_WIDTH - PlayerSelection.SQ_HEIGHT_WIDTH
                self.y = PlayerSelection.SQ_HEIGHT_WIDTH \
                         + (PlayerSelection.RECT_WIDTH * ((self.position % 10) -1))
            self.ch, self.cw = PlayerSelection.RECT_WIDTH, PlayerSelection.RECT_HEIGHT


    def advance(self):
        self.position += 1
        if self.position >= mglobals.BOARD_SQUARES:
            self.position %= mglobals.BOARD_SQUARES
        self.reposition()
        self.render()

    def goback(self):
        self.position -= 1
        if self.position < 0:
            self.position %= mglobals.BOARD_SQUARES
        self.reposition()
        self.render()

    def render(self):
        pygame.draw.rect(mglobals.GD, mglobals.color_map[self.color],
                         [self.x, self.y, self.cw, self.ch],
                         PlayerSelection.BOX_THICKNESS)
    def show(self):
        psprite = mglobals.PROPNAME_INDEX_MAP.get(self.position, None)
        if not psprite:
            return
        psprite.set_x_y()

    def hide(self):
        pass

class Player(object):
    def __init__(self, player_name):
        self.player_name = player_name
        self.color = mglobals.PLAYER_ONE_COLOR \
                            if self.player_name == mglobals.PLAYER_ONE \
                            else mglobals.PLAYER_TWO_COLOR
        self.properties = collections.defaultdict(list)
        self.money = 1500
        self.in_jail = False
        self.free_jail_pass = 0
        self.pm = PlayerMovement()
        self.ps = PlayerSelection(0, self.color)
        self.piu = PlayerInfoUI(self.player_name, self.color)
        self.piu.render()

    def give_player_money(self, cash):
        self.money += cash
        self.piu.update_cash(self.money)

    def take_player_money(self, cash):
        self.money -= cash
        self.piu.update_cash(self.money)
        #TODO handle negative money, mortgage etc

    def buy_property(self):
        pass

    #def sell_property(self):

    def mortgage_property(self):
        pass

    def unmortgage_property(self):
        pass

    def test_set_property(self, properties):
        self.properties = properties
        self.piu.update_properties(properties)

