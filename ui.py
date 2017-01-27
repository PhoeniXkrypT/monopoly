
import pygame
import collections

import utils
import mglobals
import property as _property
import dice

class CentralUI(pygame.sprite.Sprite):
    def __init__(self, pindex):
        super(CentralUI, self).__init__()
        self.pindex = pindex
        self.image = pygame.image.load("./property_pics/%d.png" % (pindex)).convert()
        self.image = pygame.transform.scale(self.image, (350, 350))
        self.rect = self.image.get_rect()
        self.unset_x_y()

    def set_x_y(self):
        self.x, self.y = 225, 225

    def unset_x_y(self):
        self.x, self.y = 900, 900

    def update(self):
        self.rect.x, self.rect.y = self.x, self.y

def init_centre_displays():
    for index in xrange(40):
        try:
            temp = CentralUI(index)
            mglobals.CENTRE_DISPLAYS.add(temp)
            mglobals.INDEX_PROPPIC_MAP[index] = temp
        except pygame.error, e:
            pass

class DiceUI(pygame.sprite.Sprite):
    def __init__(self, number1, number2):
        super(DiceUI, self).__init__()
        self.number1 = number1
        self.number2 = number2
        textfont = pygame.font.Font('./monaco.ttf', mglobals.fontsize_map['mid'])
        self.image = textfont.render('You rolled : %d & %d' % (self.number1, self.number2), \
                                     False, mglobals.color_map['black'])
        self.rect = self.image.get_rect()
        self.unset_x_y()

    def set_x_y(self):
        self.x, self.y = 250, 630

    def unset_x_y(self):
        self.x, self.y = 900, 900

    def update(self):
        self.rect.x, self.rect.y = self.x, self.y

def init_dice():
    mglobals.DICEOBJ = dice.Dice()
    for number1 in xrange(1, 7):
        for number2 in xrange(1, 7):
            temp = DiceUI(number1, number2)
            mglobals.DICE_DISPLAY.add(temp)
            mglobals.DICE_NUMBER_MAP[(number1, number2)] = temp

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

class PropertyDisplay(pygame.sprite.Sprite):
    def __init__(self, property_name, color, alias=False, fntsize='small'):
        super(PropertyDisplay, self).__init__()
        self.property_name = property_name[:12]
        self.color = mglobals.color_map[color]
        self.alias = alias
        textfont = pygame.font.Font('./monaco.ttf', mglobals.fontsize_map[fntsize])
        self.image = textfont.render(self.property_name, self.alias, self.color)
        self.rect = self.image.get_rect()
        self.unset_x_y()

    def update(self):
        self.rect.x, self.rect.y = self.x, self.y

    def set_x_y(self, x, y):
        self.x = x
        self.y = y

    def unset_x_y(self):
        self.x, self.y = 900, 900

def init_property_displays():
    for i in _property.PROPERTIES + _property.RAILWAYS + _property.UTILITIES:
        temp = PropertyDisplay(i.property_name, i.color)
        mglobals.PROPERTY_DISPLAYS.add(temp)
        mglobals.PROPERTY_NAME_SPRITE_MAP[i.property_name] = temp
        temp_m = PropertyDisplay(i.property_name, 'gray', True)
        mglobals.PROPERTY_DISPLAYS.add(temp_m)
        mglobals.PROPERTY_NAME_SPRITE_MAP[i.property_name+'_m'] = temp_m

class PlayerInfoUI(object):
    def __init__(self, player_name, color, cash=mglobals.CASH_INITIAL, \
                 properties=collections.defaultdict(list)):
        self.player_name = player_name
        if self.player_name == mglobals.PLAYER_ONE:
            self.x = 810
            self.y = 10
        elif self.player_name in [mglobals.PLAYER_TWO, mglobals.PLAYER_AI]:
            self.x = 810
            self.y = 410
        self.cash = cash
        self.properties = properties
        self.color = color
        self._draw_rect()

    def _draw_rect(self):
        pygame.draw.rect(mglobals.GD, mglobals.color_map[self.color],
                         [self.x, self.y, 375, 375], 4)

    def _print_color(self, color, properties_list, x, y, y_inc):
        utils.message_display_lines([i[:10] for i in properties_list],
                                    x, y, y_inc, color, fntsize='small')

    def _print_color2(self, color, properties_list, x, y, y_inc):
        # For each property in properties_list:
        #     Find the sprite of the property
        #     Compute x, y according to the player
        #     Do sprite.set_x_y(x, y)
        #     (in main loop update() is called)
        print "_print_color2", self.player_name, color, properties_list
        for pname in properties_list:
            psprite = mglobals.PROPERTY_NAME_SPRITE_MAP[pname]
            psprite.set_x_y(x, y)
            y += y_inc

    def update_cash(self, cash):
        self.cash = cash
        self._render_name_cash()

    def add_property(self, color, pname):
        if pname not in self.properties[color]:
            self.properties[color].append(pname)
            self._render_properties()

    def replace_property(self, color, pname_old, pname_new):
        temp = self.properties[color]
        try:
            temp[temp.index(pname_old)] = pname_new
            mglobals.PROPERTY_NAME_SPRITE_MAP[pname_old].unset_x_y()
        except ValueError, e:
            pass
        #self.render()

    def update_properties(self, properties):
        self.properties = properties
        self._render_properties()

    def _render_properties(self):
        self._draw_rect()
        x_offset, y_offset = 90, 180
        y_start = 50
        x_current, y_current = 0, 0
        for i, color in enumerate(sorted(self.properties.keys())):
            if i == 0:
                x_current, y_current = self.x + 10, self.y + 70
            elif i == 4:
                x_current, y_current = self.x + 10, self.y + 220
                y_offset = y_start + y_offset + 5
            else:
                x_current += 90

            self._print_color2(color, self.properties[color],
                              x_current, y_current, 50)

    def _render_name_cash(self):
        utils.clear_info(self.player_name)
        self._draw_rect()
        utils.message_display("%s : %d" %(self.player_name, self.cash),
                              self.x + 100,
                              self.y + 30,
                              color=self.color,
                              fntsize='mid')
