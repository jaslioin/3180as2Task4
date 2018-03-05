#from Player import Player


class Weapon(object):
    range = 0
    effect = 0
    #   NOT SURE
    owner = None

    def __init__(self, range, damage, owner):
        self.range = range
        self.effect = damage
        self.owner = owner

    def action(self, posx, posy):
        pass

    def enhance(self):
        pass

    def getEffect(self):
        return self.effect

    def getRange(self):
        return self.range
