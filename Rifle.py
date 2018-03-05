# CSCI3180 Principles of Programming Languages
# --- Declaration ---
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
# Assignment 2
# Name : Li Ho Yin
#Student ID : 1155077785
#Email Addr : hyli6@cse.cuhk.edu.hk
from Weapon import Weapon


class Rifle(Weapon):

    def __init__(self, owner):
        self.RIFLE_RANGE = 4
        self.RIFLE_INIT_DAMAGE = 10
        self.AMMO_LIMIT = 6
        self.AMMO_RECHARGE = 3
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
                print "target race ",player.getName()
                print "owner race ",self.owner.getName()
                if player.getName()[0] == self.owner.getName()[0]:
                    print "You cannot attack your same race"
                else:
                    player.decreaseHealth(self.effect * ammoToUse)
                    self.ammo -= ammoToUse
        else:
            print "Out of reach."

    def getAmmo(self):
        return self.ammo
