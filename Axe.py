from Weapon import Weapon


class Axe(Weapon):
    AXE_RANGE = 1
    AXE_INIT_DAMAGE = 40

    def __init__(self, owner):
        Weapon.__init__(self, self.AXE_RANGE, self.AXE_INIT_DAMAGE, owner)

    def enhance(self):
        self.effect += 10

    #	override
    def action(self, posx, posy):
        print "You are using axe attacking", posx, posy, "."

        if self.owner.pos.distance(posx, posy) <= self.range:
            player = self.owner.game.getPlayer(posx, posy)

            if player is not None:
                print "target race ",player.getName()
                print "owner race ",self.owner.getName()
                if player.getName()[0] == self.owner.getName()[0]:
                    print "You cannot attack your same race"
                else:
                    player.decreaseHealth(self.effect)
            else:
                print "Nothing there"

        else:
            print "Out of reach."
