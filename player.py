
from ui import PlayerInfoUI

class PlayerMovement(object):
    def __init__(self):
        pass

    def advance(self, count):
        pass

    def goback(self, count):
        pass




class Player(object):
    def __init__(self, player_name):
        self.player_name = player_name
        self.properties = None
        self.money = 1500
        self.in_jail = False
        self.free_jail_pass = 0
        self.pm = PlayerMovement()
        self.piu = PlayerInfoUI(self.player_name, self.money, {})
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

