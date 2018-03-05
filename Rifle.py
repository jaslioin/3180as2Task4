from Weapon import Weapon


class Rifle(Weapon):
    RIFLE_RANGE = 4
    RIFLE_INIT_DAMAGE = 10
    AMMO_LIMIT = 6
    AMMO_RECHARGE = 3
    ammo = 0

    def __init__(self, owner):
        Weapon.__init__(self,self.RIFLE_RANGE, self.RIFLE_INIT_DAMAGE, owner)
        self.ammo = self.AMMO_LIMIT

    def enhance(self):
        self.ammo = min(self.AMMO_LIMIT, self.ammo + self.AMMO_RECHARGE)

    def action(self, posx, posy):
        print "You are using rifle attacking " ,posx,"",posy,"."
        print "Type how many ammos you want to use."
        ammoToUse = int(raw_input())

        if ammoToUse > self.ammo:
            print "You don't have that ammos."
            return
        if self.owner.pos.distance(posx, posy) <= self.range:
            player = self.owner.game.getPlayer(posx, posy)
            if player is not None:
                player.decreaseHealth(self.effect * ammoToUse)
                self.ammo -= ammoToUse
        else:
            print "Out of reach."

    def getAmmo(self):
        return self.ammo
