class Wand(object):
    WAND_RANGE = 5
    effect = 10
    owner = None

    def __init__(self, owner):
        self.owner = owner

    def action(self, posx, posy):
        print "You are using wand healing " ,posx,"",posy,"."
        if self.owner.pos.distance(posx, posy) <= self.WAND_RANGE:
            player = self.owner.game.getPlayer(posx, posy)
            if player is not None:
                print "target race ",player.getName()
                print "owner race ",self.owner.getName()
                if player.getName()[0] == self.owner.getName()[0]:
                    player.increaseHealth(self.effect)
                else:
                    print "Not the same race"
        else:
            print "Out of reach."

    def enhance(self):
        self.effect += 5

    def getEffect(self):
        return self.effect

    def getRange(self):
        return self.WAND_RANGE