
import pygame
import collections

import mglobals
import utils
import property as _property

from ui import PlayerInfoUI

class PlayerMovement(object):
    RECT_WIDTH = 65
    RECT_HEIGHT = 106
    SQ_HEIGHT_WIDTH = 106
    PIMG_WIDTH = 60
    PIMG_HEIGHT = 40

    def __init__(self, player_name, player_img, position=0):
        self.position = position
        self.player_name = player_name
        self.player_img = player_img
        self.x, self.y = 720, 730

    def find_rent_amount(self):
        for player, obj in mglobals.PLAYER_OBJ.iteritems():
            if player == self.player_name:
                currentplayer = obj
            else:
                otherplayer = obj
        try:
            p_object = mglobals.POBJECT_MAP[self.position]
            val = p_object.compute_rent(self.player_name)
            currentplayer.cash -= val
            utils.clear_info(currentplayer.player_name)
            currentplayer.piu.update_cash(currentplayer.cash)
            otherplayer.cash += val
            utils.clear_info(otherplayer.player_name)
            otherplayer.piu.update_cash(otherplayer.cash)
        except KeyError, e:
            pass

    def advance(self, count):
        self.position = (self.position + count) % mglobals.BOARD_SQUARES
        self.reposition()
        self.find_rent_amount()
        self.render()

    def goback(self, count):
        self.position = (self.position - count) % mglobals.BOARD_SQUARES
        self.reposition()
        self.find_rent_amount()
        self.render()

    def reposition(self):
        # If the position corresponds to a square
        if self.position % 10 == 0:
            if self.position in [0, 10]:
                self.y = mglobals.DISPLAY_H - PlayerMovement.PIMG_HEIGHT - 33
                self.x = 720 if self.position == 0 \
                           else 25
            else:
                self.y = 33
                self.x = 720 if self.position == 30 \
                           else 25

        # If the position corresponds to a vertical rectangle
        elif (self.position > 0 and self.position < 10) or \
             (self.position > 20 and self.position < 30):
            if self.position > 0 and self.position < 10:
                self.y = 730
                self.x = mglobals.BOARD_WIDTH - PlayerMovement.SQ_HEIGHT_WIDTH \
                         - PlayerMovement.PIMG_WIDTH  - 3 \
                         - ((self.position - 1) * PlayerMovement.RECT_WIDTH)
            else:
                self.y = 33
                self.x = PlayerMovement.SQ_HEIGHT_WIDTH + 3 \
                         + (((self.position % 10) - 1) * PlayerMovement.RECT_WIDTH)

        # If the position corresponds to a horizontal rectangle
        else:
            if self.position > 10 and self.position < 20:
                self.x = 25
                self.y = mglobals.DISPLAY_H - PlayerMovement.SQ_HEIGHT_WIDTH \
                         - PlayerMovement.PIMG_HEIGHT - 12 \
                         - (((self.position % 10) - 1) * PlayerMovement.RECT_WIDTH)
            else:
                self.x = 720
                self.y = PlayerMovement.SQ_HEIGHT_WIDTH + 12 \
                         + (((self.position % 10) - 1) * PlayerMovement.RECT_WIDTH)

    def render(self):
        mglobals.GD.blit(self.player_img, (self.x, self.y))

class PlayerSelection(object):
    BOX_THICKNESS = 5
    RECT_WIDTH = 65
    RECT_HEIGHT = 106
    SQ_HEIGHT_WIDTH = 106

    def __init__(self, color, position=0):
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
        psprite = mglobals.INDEX_PROPPIC_MAP.get(self.position, None)
        if not psprite:
            return
        psprite.set_x_y()

    def hide(self):
        psprite = mglobals.INDEX_PROPPIC_MAP.get(self.position, None)
        if not psprite:
            return
        psprite.unset_x_y()

class Player(object):
    def __init__(self, player_name):
        self.player_name = player_name
        self.color = mglobals.PLAYER_ONE_COLOR \
                            if self.player_name == mglobals.PLAYER_ONE \
                            else mglobals.PLAYER_TWO_COLOR
        self.properties = collections.defaultdict(list)
        self.cash = 1500
        self.in_jail = False
        self.free_jail_pass = 0
        self.ps = PlayerSelection(self.color)
        self.piu = PlayerInfoUI(self.player_name, self.color)
        self.piu._render_name_cash()
        self.pm = PlayerMovement(self.player_name, mglobals.P1_IMG) \
                            if self.player_name == mglobals.PLAYER_ONE \
                            else PlayerMovement(self.player_name, mglobals.P2_IMG)

    def give_player_cash(self, cash):
        self.cash += cash
        self.piu.update_cash(self.cash)

    def take_player_cash(self, cash):
        self.cash -= cash
        self.piu.update_cash(self.cash)
        #TODO handle negative cash

    #def sell_property(self):

    #TODO Change color_all when sell_property
    def set_color_all(self, color, unset=False):
        for each in mglobals.PROP_COLOR_INDEX[color]:
            p_object = mglobals.POBJECT_MAP[each]
            if unset:
                p_object.color_all = False
            else:
                p_object.color_all = True

    def buy_property(self, index):
        try:
            p_object = mglobals.POBJECT_MAP[index]
            if p_object.purchase(self.player_name, self.cash)[0]:
                prop_list = self.properties.get(p_object.color, None)
                if not prop_list or p_object.property_name not in prop_list:
                    self.properties[p_object.color].append(p_object.property_name)
                    self.cash -= p_object.cost
                    if len(self.properties[p_object.color]) == \
                       len(mglobals.PROP_COLOR_INDEX[p_object.color]):
                        self.set_color_all(p_object.color)
                    utils.clear_info(self.player_name)
                    self.piu.update_cash(self.cash)
                    self.piu.update_properties(self.properties)
        except KeyError, e:
            pass

    def mortgage_property(self, index):
        try:
            p_object = mglobals.POBJECT_MAP[index]
            val = p_object.mortgage(self.player_name)
            if not val:
                return False
            self.cash += val
            utils.clear_info(self.player_name)
            self.piu.replace_property(p_object.color, p_object.property_name, p_object.property_name+'_m')
            self.piu.update_cash(self.cash)
            self.piu.update_properties(self.properties)
            return True
        except KeyError, e:
            pass

    def unmortgage_property(self, index):
        try:
            p_object = mglobals.POBJECT_MAP[index]
            val = p_object.unmortgage(self.player_name, self.cash)
            if not val:
                return False
            self.cash -= val
            utils.clear_info(self.player_name)
            self.piu.replace_property(p_object.color, p_object.property_name+'_m', p_object.property_name)
            self.piu.update_cash(self.cash)
            self.piu.update_properties(self.properties)
            return True
        except KeyError, e:
            pass

    def build_house(self, index):
        try :
            p_object = mglobals.POBJECT_MAP[index]
            val = p_object.build(self.player_name, self.cash)
            if not val:
                return False
            self.cash -= val
            utils.clear_info(self.player_name)
            self.piu.update_cash(self.cash)
        except KeyError, e:
            pass
