
import pygame
import collections

import utils
import mglobals
import dice
import infra
import property as _property

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

class PRINTUI(pygame.sprite.Sprite):
    def __init__(self, message="", color='black', fntsize='small_p', alias=False):
        super(PRINTUI, self).__init__()
        self.message = message
        self.color = mglobals.color_map[color]
        self.fntsize = mglobals.fontsize_map[fntsize]
        self.alias = alias
        textfont = pygame.font.Font('./monaco.ttf', self.fntsize)
        self.image = textfont.render(self.message, self.alias, self.color)
        self.rect = self.image.get_rect()
        self.unset_x_y()

    def set_x_y(self, x=120, y=600):
        self.x, self.y = x, y

    def unset_x_y(self):
        self.x, self.y = 900, 900

    def update(self):
        self.rect.x, self.rect.y = self.x, self.y

def init_printui():
    for player, color in zip ([mglobals.PLAYER_ONE, mglobals.PLAYER_TWO], \
                              [mglobals.PLAYER_ONE_COLOR, mglobals.PLAYER_TWO_COLOR]):
        temp_p = PRINTUI(player, color, 'mid', True)
        mglobals.PLAYER_NAME_DISPLAY.add(temp_p)
        mglobals.PLAYER_NAME_SPRITE[player] = temp_p
        temp = PRINTUI()
        temp.image = mglobals.P1_IMG if player == mglobals.PLAYER_ONE \
                                     else mglobals.P2_IMG
        mglobals.PLAYER_NAME_DISPLAY.add(temp)
        mglobals.CURRENTPLAYER_IMG[player] = temp

    for each in [mglobals.PLAYER_ONE, mglobals.PLAYER_TWO]:
        for i in xrange(1,12):
            temp = PRINTUI(str(i))
            mglobals.JAILCARD_DISPLAY.add(temp)
            mglobals.PLAYER_JAIL_CARD[each][i] = temp
        temp = PRINTUI("10+")
        mglobals.JAILCARD_DISPLAY.add(temp)
        mglobals.PLAYER_JAIL_CARD[each][11] = temp
    mglobals.JAIL_MSG = PRINTUI("In JAIL")
    mglobals.CHESTCHANCE_DISPLAYS.add(mglobals.JAIL_MSG)

    for i in xrange(16):
        temp = PRINTUI(infra.COMMUNITYCHEST[i])
        mglobals.CHESTCHANCE_DISPLAYS.add(temp)
        mglobals.CHEST_MAP[i] = temp
        temp1 = PRINTUI(infra.CHANCE[i])
        mglobals.CHESTCHANCE_DISPLAYS.add(temp1)
        mglobals.CHANCE_MAP[i] = temp1

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

    def set_x_y(self, x, y):
        self.x, self.y = x, y

    def unset_x_y(self):
        self.x, self.y = 900, 900

    def update(self):
        self.rect.x, self.rect.y = self.x, self.y

def init_property_displays():
    for i in _property.PROPERTIES:
        temp = PropertyDisplay(i.property_name, i.color)
        mglobals.PROPERTY_DISPLAYS.add(temp)
        mglobals.PROPERTY_NAME_SPRITE_MAP[i.property_name] = temp
        temp_m = PropertyDisplay(i.property_name, 'gray', True)
        mglobals.PROPERTY_DISPLAYS.add(temp_m)
        mglobals.PROPERTY_NAME_SPRITE_MAP[i.property_name+'_m'] = temp_m
    for i in _property.RAILWAYS + _property.UTILITIES:
        temp = PropertyDisplay(i.property_name[:1], i.color, True, 'mid')
        mglobals.PROPERTY_DISPLAYS.add(temp)
        mglobals.PROPERTY_NAME_SPRITE_MAP[i.property_name] = temp
        temp_m = PropertyDisplay(i.property_name[:1], 'gray', True, 'mid')
        mglobals.PROPERTY_DISPLAYS.add(temp_m)
        mglobals.PROPERTY_NAME_SPRITE_MAP[i.property_name+'_m'] = temp_m

class HouseCountDisplay(pygame.sprite.Sprite):
    def __init__(self, index, count, color='white', fntsize='small'):
        super(HouseCountDisplay, self).__init__()
        self.index = index
        self.count = count
        self.color = mglobals.color_map[color]
        textfont = pygame.font.Font('./monaco.ttf', mglobals.fontsize_map[fntsize])
        self.image = textfont.render(self.count, True, self.color)
        if self.index in xrange(11,20):
            self.image = pygame.transform.rotate(self.image, 270)
        elif self.index in xrange(21,30):
            self.image = pygame.transform.rotate(self.image, 180)
        elif self.index in xrange(31,40):
            self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.unset_x_y()

    def set_x_y(self, x, y):
        self.x, self.y = x, y

    def unset_x_y(self):
        self.x, self.y = 900, 900

    def update(self):
        self.rect.x, self.rect.y = self.x, self.y

def init_house_count_displays():
    for each in _property.PROPERTIES:
        for val in xrange(1, 6):
            temp = HouseCountDisplay(each.index, str(val))
            mglobals.HOUSE_COUNT_DISPLAYS.add(temp)
            mglobals.INDEX_HOUSE_COUNT_MAP[each.index][val] = temp

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

    def _print_color(self, properties_list, x, y, x_inc):
        for pname in properties_list:
            psprite = mglobals.PROPERTY_NAME_SPRITE_MAP[pname]
            psprite.set_x_y(x, y)
            x += x_inc

    # For each property in properties_list:
    #     Find the sprite of the property
    #     Compute x, y according to the player
    #     Do sprite.set_x_y(x, y)
    #     (in main loop update() is called)
    def _print_color2(self, properties_list, x, y, y_inc):
        for pname in properties_list:
            psprite = mglobals.PROPERTY_NAME_SPRITE_MAP[pname]
            psprite.set_x_y(x, y)
            y += y_inc

    def update_cash(self, cash):
        self.cash = cash
        self.render_name_cash()

    def add_property(self, color, pname):
        if pname not in self.properties[color]:
            self.properties[color].append(pname)
            self.render_properties()

    def replace_property(self, color, pname_old, pname_new):
        temp = self.properties[color]
        try:
            temp[temp.index(pname_old)] = pname_new
            mglobals.PROPERTY_NAME_SPRITE_MAP[pname_old].unset_x_y()
        except ValueError, e:
            pass

    def update_properties(self, properties):
        self.properties = properties
        self.render_properties()

    def render_properties(self):
        self._draw_rect()
        x_offset, y_offset = 90, 180
        y_start = 50
        x_current, y_current = 0, 0
        i = 0
        for color in sorted(self.properties.keys()):
            if color in ['purple', 'black']:
                if color == 'black':
                    x, y = self.x + 10, self.y + 340
                else:
                    x, y = self.x + 260, self.y + 340
                self._print_color(self.properties[color], x, y, 60)
            else:
                if i == 0:
                    x_current, y_current = self.x + 10, self.y + 70
                elif i == 4:
                    x_current, y_current = self.x + 10, self.y + 220
                    y_offset = y_start + y_offset + 5
                else:
                    x_current += 90

                self._print_color2(self.properties[color],
                                      x_current, y_current, 50)
                i += 1

    def render_name_cash(self):
        utils.clear_info(self.player_name)
        self._draw_rect()
        utils.message_display("%s : %d" %(self.player_name, self.cash),
                              self.x + 100,
                              self.y + 30,
                              color=self.color,
                              fntsize='mid')
        if self.player_name == mglobals.PLAYER_ONE:
            mglobals.GD.blit(mglobals.P1_IMG, (self.x + 200, self.y + 10))
        else:
            mglobals.GD.blit(mglobals.P2_IMG, (self.x + 200, self.y + 10))

    def jail_card_display(self, add=True):
        self.render_name_cash()
        val = mglobals.PLAYER_OBJ[self.player_name].jail.free_jail_pass
        if add and not(val - 1 == 0) and val < 12:
            mglobals.PLAYER_JAIL_CARD[self.player_name][val-1].unset_x_y()
        elif not(add) and val < 11:
            mglobals.PLAYER_JAIL_CARD[self.player_name][val+1].unset_x_y()
        if val in xrange(1,11):
            mglobals.PLAYER_JAIL_CARD[self.player_name][val].set_x_y(self.x + 350, self.y + 20)
        elif val == 11:
            mglobals.PLAYER_JAIL_CARD[self.player_name][11].set_x_y(self.x + 340, self.y + 20)
