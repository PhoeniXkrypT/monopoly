# -*- coding: utf-8 -*-

import random

import mglobals

CHANCE_INDEXLIST = [7, 22, 36]
CHEST_INDEXLIST = [2, 17, 33]

class MonopolyChance(object):
    def __init__(self):
        pass

class MonopolyCommunityChest(object):
    pass

class IncomeTax(object):
    pass

class LuxuryTax(object):
    pass

def deduct_house_hotel_repair(player_obj, house_cost, hotel_cost):
    repair_amt = 0
    for each_color in player_obj.properties:
        pindex_list = mglobals.PROP_COLOR_INDEX[each_color]
        for each_prop in player_obj.properties[each_color]:
            for index in pindex_list:
                if mglobals.POBJECT_MAP[index].property_name == each_prop:
                    prop = mglobals.POBJECT_MAP[index]
                    if prop.house_count > 4:
                        repair_amt += hotel_cost
                    else:
                        repair_amt += prop.house_count * house_cost
    return repair_amt

#TODO unset CHANCE CHEST MESSAGE
def chance_chest(player_name):
    player_obj = mglobals.PLAYER_OBJ[player_name]
    value = random.randrange(16)
    if player_obj.pm.position in CHANCE_INDEXLIST:
        mglobals.CHANCE_MAP[value].set_x_y()
        chance(player_obj, value)
    else:
        mglobals.CHEST_MAP[value].set_x_y()
        chest(player_obj, value)

def chance(player_obj, value):
    if value == 0:
        player_obj.pm.advance(mglobals.BOARD_SQUARES - player_obj.pm.position)
    elif value == 1:
        player_obj.pm.advance(mglobals.BOARD_SQUARES + 10 - player_obj.pm.position, True)
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
        amt = deduct_house_hotel_repair(player_obj, 25, 100)
        player_obj.take_player_cash(amt)
    elif value == 8:
        amt = deduct_house_hotel_repair(player_obj, 40, 115)
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
        pass

def chest(player_obj, value):
    if value == 0:
        player_obj.pm.advance(mglobals.BOARD_SQUARES - player_obj.pm.position)
    elif value == 1:
        player_obj.pm.advance(mglobals.BOARD_SQUARES + 1 - player_obj.pm.position)
    elif value == 2:
        player_obj.pm.advance(mglobals.BOARD_SQUARES + 10 - player_obj.pm.position, True)
    elif value == 3:
        player_obj.take_player_cash(100)
    elif value == 4:
        player_obj.take_player_cash(50)
    elif value == 5:
        player_obj.take_player_cash(50)
    elif value == 6:
        player_obj.give_player_cash(200)
    elif value == 7:
        player_obj.give_player_cash(100)
    elif value == 8:
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
        pass
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
