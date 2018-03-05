from Human import Human
from Chark import Chark
from Player import Player
from Pos import Pos
#from Axe import Axe
from Obstacle import Obstacle
#from Rifle import Rifle
from Weapon import Weapon


class SurvivalGame(object):
    n = 0
    D = 10
    O = 2

    #   NOT SURE
    teleportObjects = None

    def __init__(self):
        pass

    def printBoard(self):
        printObject = [["  " for x in range(self.D)] for y in range(self.D)]

        i=0
        while(i<self.n):
            if isinstance(self.teleportObjects[i],Player):
                pos = self.teleportObjects[i].getPos()
                printObject[pos.getX()][pos.getY()] = \
                    self.teleportObjects[i].getName()
                print "player ",pos.getX(),pos.getY()
            i += 1

        i=self.n
        while i<self.n+self.O :
            #self.teleportObjects[i] = Obstacle(1,1,i,self)

            if isinstance(self.teleportObjects[i],Obstacle):

                pos = self.teleportObjects[i].getPos()
                tmp = i+1-self.n
                printObject[pos.getX()][pos.getY()] = 'O'+str(tmp)
                print "Obstacle ",pos.getX(),pos.getY()
            i += 1

        #print
        print " ",
        i=0
        while i<self.D:
            print("|  %d " % i),
            i += 1
        print("|")
        i=0
        while i < self.D*3.2 :
            print "-",
            i += 1
        print ""
        row=0
        while row < self.D:
            print row,
            col=0
            while col < self.D:
                print("| %s " %printObject[row][col]),
                col+=1
            print "|"
            i=0
            while i<self.D*3.2 :
                print "-",
                i+=1
            print ""
            row+=1

    def positionOccupied(self, randx, randy):
        for o in self.teleportObjects:
            if isinstance(o,Player):
                pos = o.getPos()
                if pos.getX() == randx and pos.getY() == randy:
                    return True
            else:
                pos = o.getPos()
                if pos.getX() == randx and pos.getY() == randy:
                    return True
        return False

    def getPlayer(self, randx, randy):
        for o in self.teleportObjects:
            if isinstance(o,Player):
                pos = o.getPos()
                if pos.getX() == randx and pos.getY() == randy:
                    return o
        return None

    def init(self):
        print "Welcome to Kafustrok. Light blesses you. \n" \
              "Input number of players: (a even number)"
        self.n = int(raw_input())
        self.teleportObjects = [object() for x in range(self.n+self.O)]
        for i in range(0,self.n/2):
            print "created ",i+1," entity"
            self.teleportObjects[i] = Human(0,0,i,self)
            self.teleportObjects[i+self.n/2] = Chark(0,0,i,self)
        i= 0
        while(i<self.O):
            print "created ",i," Obstacle"
            self.teleportObjects[i+self.n] = Obstacle(0,0,i,self)
            i += 1


    def gameStart(self):
        turn = 0
        numOfAlivePlayers = self.n
        print "num of alive player ",numOfAlivePlayers
        while numOfAlivePlayers > 1:
            if turn == 0:
                for obj in self.teleportObjects :
                    obj.teleport()
                print "Everything gets teleported.."

            self.printBoard()

            if isinstance(self.teleportObjects[turn],Player):
                t = self.teleportObjects[turn]
                if t.health > 0:
                    t.askForMove()
                    print ""

            turn = (turn + 1) % self.n
            print "turn ",turn
            numOfAlivePlayers = 0
            for i in range(0,self.n):
                if isinstance(self.teleportObjects[i],Player):
                    if self.teleportObjects[i].health > 0:
                        numOfAlivePlayers += 1
        for i in range(0,self.n):
            if isinstance(self.teleportObjects[i],Player):
                print "player health",self.teleportObjects[i].health
        print "Game over."
        self.printBoard()





game = SurvivalGame()
game.init()
game.gameStart()
