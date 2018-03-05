from Player import Player
from Axe import Axe


class Chark(Player):

    def __init__(self, posx, posy, index, game):
        Player.__init__(self,100, 4, posx, posy, index, game)

        self.myString = "C" + str(index)
        self.equipment = Axe(self)

    def teleport(self):
        super(Chark, self).teleport()
        self.equipment.enhance()

    def askForMove(self):
        print("You are a Chark (C%d) using Axe. (Range: %d, Damage: %d)"
              % (self.index, self.equipment.getRange(), self.equipment.getEffect()))
        super(Chark, self).askForMove()
