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


class Axe(Weapon):


    def __init__(self, owner):
        self.AXE_RANGE = 1
        self.AXE_INIT_DAMAGE = 40
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
            print "Out of reach."
