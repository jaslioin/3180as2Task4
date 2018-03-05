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
from Weapon import Weapon



class Player(object):

    def __init__(self, healthCap, mob, posx, posy, index, game):
        self.MOBILITY = mob
        self.health = healthCap
        self.HEALTH_CAP = healthCap
        self.pos = Pos(posx, posy)
        self.index = index
        self.game = game
        self.equipment = None
        self.myString = ''
        self.HEALTH_CAP = 0
    def getPos(self):
        return self.pos

    def teleport(self):

        randx = random.randint(0, self.game.D-1)

        randy = random.randint(0, self.game.D-1)
        print "Player teleported to ",randx," ",randy
        while self.game.positionOccupied(randx,randy):
            randx = random.randint(0, self.game.D-1)
            randy = random.randint(0, self.game.D-1)
        self.pos.setPos(randx,randy)

    def increaseHealth(self,h):
        self.health += h
        if self.health > self.HEALTH_CAP:
            print "reached health cap!"
            self.health = self.HEALTH_CAP
    def decreaseHealth(self,h):
        self.health -= h
        if self.health <= 0 :
            self.myString = "C" + self.myString[0]

    def getName(self):
        return self.myString

    def askForMove(self):
        print("Your health is %d Your position is (%d,%d). Your mobility is %d." %
         (self.health,self.pos.getX(), self.pos.getY(), self.MOBILITY))
        print("You now have following options: ")
        print("1. Move")
        print("2. Action")
        print("3. End tne turn")

        a = int(raw_input())

        if a == 1:
            print "Specify your target position (Input 'x y')."
            posx, posy = map(int, raw_input().split())
            if self.pos.distance(posx,posy) > self.MOBILITY:
                print "Beyond your reach. Staying still."
            elif self.game.positionOccupied(posx,posy):
                print "Position occupied. Cannot move there."
            else:
                self.pos.setPos(posx,posy)
                self.game.printBoard()
                print "You can now \n1.Action\n2.End the turn"
                if int(raw_input()) == 1:
                    print "Input position to act. (Input 'x y')"
                    attx, atty = map(int, raw_input().split())
                    self.equipment.action(attx,atty)
        elif a == 2:
            print "Input position to act."
            attx, atty = map(int, raw_input().split())
            self.equipment.action(attx,atty)
        elif a == 3:
            return





