
import pygame

import utils
import mglobals

class CentralUI(object):
    pass

class DiceUI(CentralUI):
    pass

class MonopolyChanceUI(CentralUI):
    pass

class MonopolyCommunityChestUI(CentralUI):
    pass

class IncomeTaxUI(CentralUI):
    pass

class LuxuryTaxUI(CentralUI):
    pass

color_offset = {
        'blue': (5, 15),
        'brown': ( ),
        'green': (),
        'orange': (),
        'pink': (),
        'red': (),
        'sky_blue': (),
        'yellow': (),
};


class PlayerInfoUI(object):
    def __init__(self, player_name, cash=mglobals.CASH_INITIAL, properties={}):
        self.player_name = player_name
        if self.player_name == mglobals.PLAYER_ONE:
            self.x = 810
            self.y = 10
            self.color = 'royal_blue'
        elif self.player_name in [mglobals.PLAYER_TWO, mglobals.PLAYER_AI]:
            self.x = 810
            self.y = 410
            self.color = 'sea_green'
        self.cash = cash
        self.properties = properties
        self._draw_rect()

    def _draw_rect(self):
        pygame.draw.rect(mglobals.GD, mglobals.color_map[self.color],
                        [self.x, self.y, 375, 375], 4)

    def _print_color(self, color, properties_list, x, y, y_inc):
        utils.message_display_lines([i[:10] for i in properties_list],
                                    x, y, y_inc, color, fntsize='small')

    def update_cash(self, cash):
        self.cash = cash
        self.render()

    #TODO seperate render for cash and properties

    def update_properties(self, properties):
        self.properties = properties

    def _render_properties(self):
        self._draw_rect()
        x_offset, y_offset = 90, 180
        y_start = 50
        x_current, y_current = 0, 0
        for i, color in enumerate(sorted(self.properties.keys())):
            if i == 0:
                x_current, y_current = self.x + 50, self.y + 70
            elif i == 4:
                x_current, y_current = self.x + 50, self.y + 220
                y_offset = y_start + y_offset + 5
            else:
                x_current += 90

            self._print_color(color, self.properties[color],
                              x_current, y_current, 50)

    def _render_name_cash(self):
        utils.message_display("%s : %d" %(self.player_name, self.cash),
                              self.x + 100,
                              self.y + 30,
                              color=self.color,
                              fntsize='mid')

    def render(self):
        self._render_name_cash()
        self._render_properties()

