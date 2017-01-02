
class PlayerMovement(object):
    def __init__(self):
        pass

    def advance(self, count):
        pass

    def goback(self, count):
        pass




class Player(object):
    def __init__(self):
        self.properties = None
        self.money = 1500
        self.in_jail = False
        self.free_jail_pass = False
        self.pm = PlayerMovement()

    def give(self, cash):
        pass

    def take(self, cash):
        pass

