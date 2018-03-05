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
import random
from Pos import Pos


class Obstacle(object):

    def __init__(self, posx, posy, index, game):
        self.pos = Pos(posx, posy)
        self.index = index
        self.game = game

    def getPos(self):
        return self.pos

    def teleport(self):
        randx = random.randint(0, self.game.D - 1)
        randy = self.game.D - randx - 1
        print "Obstacle teleported to ",randx," ",randy
        while self.game.positionOccupied(randx, randy):
            randx = random.randint(0, self.game.D - 1)
            randy = self.game.D - randx - 1
        self.pos.setPos(randx, randy)
