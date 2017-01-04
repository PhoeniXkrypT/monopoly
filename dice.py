
import random

import mglobals

class Dice(object):
    def __init__(self):
        self.number = 2
        self.dicemap = mglobals.DICE_NUMBER_MAP

    def roll(self):
        self.number = random.randrange(2, 13)
        self.show()

    def show(self):
        print self.number
        self.dicemap[self.number].set_x_y()

    def hide(self):
        print self.number
        self.dicemap[self.number].unset_x_y()

