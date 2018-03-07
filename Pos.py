# CSCI3180 Principles of Programming Languages
# --- Declaration ---
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
# Assignment 2
# Name : Li Ho Yin
# Student ID : 1155077785
# Email Addr : hyli6@cse.cuhk.edu.hk
class Pos:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x1, y1):
        return abs(self.x - x1) + abs(self.y - y1)

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
