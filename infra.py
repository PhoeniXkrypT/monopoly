# -*- coding: utf-8 -*-

import random

import mglobals
import property as _property

CHANCE_INDEXLIST = [7, 22, 36]
CHEST_INDEXLIST = [2, 17, 33]

class Jail(object):
    def __init__(self, player_name):
        self.player_name = player_name
        self.free_jail_pass = 0
        self.in_jail = False

    def use_cash(self):
        if self.in_jail:
            mglobals.PLAYER_OBJ[self.player_name].take_player_cash(50)
            self.in_jail = False
            mglobals.JAIL_MSG.unset_x_y()

    def use_jail_pass(self):
        if self.in_jail and self.free_jail_pass:
            self.free_jail_pass -= 1
            mglobals.PLAYER_OBJ[self.player_name].piu.jail_card_display(False)
            self.in_jail = False
            mglobals.JAIL_MSG.unset_x_y()

class ChanceChest(object):
    def __init__(self):
        pass

    def chance_chest(self, player_name):
        player_obj = mglobals.PLAYER_OBJ[player_name]
        mglobals.CHANCE_CHEST_VALUE = random.randrange(16)
        if player_obj.pm.position in CHANCE_INDEXLIST:
            mglobals.CHANCE_MAP[mglobals.CHANCE_CHEST_VALUE].set_x_y()
            self.chance(player_obj, mglobals.CHANCE_CHEST_VALUE)
        else:
            mglobals.CHEST_MAP[mglobals.CHANCE_CHEST_VALUE].set_x_y()
            self.chest(player_obj, mglobals.CHANCE_CHEST_VALUE)

    def deduct_house_hotel_repair(self, player_obj, house_cost, hotel_cost):
        repair_amt = 0
        for color in player_obj.properties:
            for pname in player_obj.properties[color]:
                if '_' in pname:
                    pname = pname[:-2]
                prop = mglobals.PNAME_OBJ_MAP[pname]
                if prop in _property.PROPERTIES and not(prop.mortgaged):
                    if prop.house_count > 4:
                        repair_amt += hotel_cost
                    else:
                        repair_amt += prop.house_count * house_cost
        return repair_amt

    def chance(self, player_obj, value):
        if value == 0:
            player_obj.pm.advance(mglobals.BOARD_SQUARES - player_obj.pm.position)
        elif value == 1:
            player_obj.pm.advance(mglobals.BOARD_SQUARES + 10 - player_obj.pm.position)
            player_obj.jail.in_jail= True
        elif value == 2:
            player_obj.pm.advance(mglobals.BOARD_SQUARES + 11 - player_obj.pm.position)
        elif value == 3:
            player_obj.pm.advance(mglobals.BOARD_SQUARES + 15 - player_obj.pm.position)
        elif value == 4:
            player_obj.pm.advance(mglobals.BOARD_SQUARES + 24 - player_obj.pm.position)
        elif value == 5:
            player_obj.pm.advance(mglobals.BOARD_SQUARES + 39 - player_obj.pm.position)
        elif value == 6:
            player_obj.pm.goback(3)
        elif value == 7:
            amt = self.deduct_house_hotel_repair(player_obj, 25, 100)
            player_obj.take_player_cash(amt)
        elif value == 8:
            amt = self.deduct_house_hotel_repair(player_obj, 40, 115)
            player_obj.take_player_cash(amt)
        elif value == 9:
            player_obj.take_player_cash(150)
        elif value == 10:
            player_obj.take_player_cash(20)
        elif value == 11:
            player_obj.take_player_cash(15)
        elif value == 12:
            player_obj.give_player_cash(150)
        elif value == 13:
            player_obj.give_player_cash(100)
        elif value == 14:
            player_obj.give_player_cash(50)
        elif value == 15:
            player_obj.jail.free_jail_pass += 1
            player_obj.piu.jail_card_display()

    def chest(self, player_obj, value):
        if value == 0:
            player_obj.pm.advance(mglobals.BOARD_SQUARES - player_obj.pm.position)
        elif value == 1:
            player_obj.pm.advance(mglobals.BOARD_SQUARES + 1 - player_obj.pm.position)
        elif value == 2:
            player_obj.pm.advance(mglobals.BOARD_SQUARES + 10 - player_obj.pm.position)
            player_obj.jail.in_jail= True
        elif value == 3:
            player_obj.take_player_cash(100)
        elif value == 4 or value == 5:
            player_obj.take_player_cash(50)
        elif value == 6:
            player_obj.give_player_cash(200)
        elif value == 7 or value == 8:
            player_obj.give_player_cash(100)
        elif value == 9:
            player_obj.give_player_cash(50)
        elif value == 10:
            player_obj.give_player_cash(25)
        elif value == 11:
            player_obj.give_player_cash(20)
        elif value == 12:
            player_obj.give_player_cash(10)
        elif value == 13:
            for player, obj in mglobals.PLAYER_OBJ.iteritems():
                if not(player == player_obj.player_name):
                    obj.take_player_cash(10)
            player_obj.give_player_cash(10)
        elif value == 14:
            player_obj.jail.free_jail_pass += 1
            player_obj.piu.jail_card_display()
        elif value == 15:
            player_obj.take_player_cash(10)

CHANCE = {
        0: 'Advance to GO',
        1: 'Go to jail. Move directly to jail. Do not pass GO.',
        2: 'Advance to Pall Mall. If you pass GO collect £200',
        3: 'Take a trip to Marylebone Station. If you pass GO collect £200',
        4: 'Advance to Trafalgar Square. If you pass "Go" collect £200',
        5: 'Advance to Mayfair',
        6: 'Go back three spaces',
        7: 'General repairs. Pay £25 per house, £100 per hotel.',
        8: 'Street repairs: Pay £40 per house, £115 per hotel.',
        9: 'Pay school fees of £150',
        10: '"Drunk in charge" fine £20',
        11: 'Speeding fine £15',
        12: 'Your building loan matures. Receive £150',
        13: 'You have won a crossword competition. Collect £100',
        14: 'Bank pays you dividend of £50',
        15: 'Get out of jail free.',
}

COMMUNITYCHEST={
        0: 'Advance to GO',
        1: 'Go back to Old Kent Road',
        2: 'Go to jail. Move directly to jail. Do not pass GO.',
        3: 'Pay hospital £100',
        4: "Doctor's fee. Pay £50",
        5: 'Pay your insurance premium £50',
        6: 'Bank error in your favour. Collect £200',
        7: 'Annuity matures. Collect £100',
        8: 'You inherit £100',
        9: 'From sale of stock you get £50',
        10: 'Receive interest on 7% preference shares: £25',
        11: 'Income tax refund. Collect £20',
        12: 'You have won second prize in a beauty contest. Collect £10',
        13: 'It is your birthday. Collect £10 from each player',
        14: 'Get out of jail free.',
        #TODO Take Chance
        15: 'Pay a £10 fine or take a "Chance"',
}
