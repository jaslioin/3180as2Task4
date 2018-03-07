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
class Wand(object):

    def __init__(self, owner):
        self.owner = owner
        self.WAND_RANGE = 5
        self.effect = 5

    def action(self, posx, posy):
        print "You are using wand healing " ,posx,"",posy,"."
        if self.owner.pos.distance(posx, posy) <= self.WAND_RANGE:
            player = self.owner.game.getPlayer(posx, posy)
            if player is not None:
                print "target race ",player.getName()
                print "owner race ",self.owner.getName()
                if player.getName()[0] == self.owner.getName()[0]:
                    if int(player.getName()[1]) in [0,1,2,3,4,5,6,7,8,9]:
                        player.increaseHealth(self.effect)
                elif player.getName()[1] == self.owner.getName()[0]:
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
