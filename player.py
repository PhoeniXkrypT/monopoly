
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
        self.free_jail_pass = False
        self.pm = PlayerMovement()
        self.piu = PlayerInfoUI(self.player_name, self.money, {})
        self.piu.render()

    def give(self, cash):
        pass

    def take(self, cash):
        pass

    def buy_property(self):
        pass

    def sell_property(self):
        pass

    def mortgage_property(self):
        pass

    def unmortgage_property(self):
        pass

