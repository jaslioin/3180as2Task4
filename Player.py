import random
from Pos import Pos
from Weapon import Weapon
#from SurvivalGame import SurvivalGame


class Player(object):
    MOBILITY = 0
    pos = None
    health = 0
    equipment = None
    index = 0
    myString = ''
    game = None
    def __init__(self):
        pass
    def __init__(self, healthCap, mob, posx, posy, index, game):
        self.MOBILITY = mob
        self.health = healthCap
        self.pos = Pos(posx, posy)
        self.index = index
        self.game = game

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
        print("2. Attack")
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
                print "You can now \n1.attack\n2.End the turn"
                if int(raw_input()) == 1:
                    print "Input position to attack. (Input 'x y')"
                    attx, atty = map(int, raw_input().split())
                    self.equipment.action(attx,atty)
        elif a == 2:
            print "Input position to attack."
            attx, atty = map(int, raw_input().split())
            self.equipment.action(attx,atty)
        elif a == 3:
            return





