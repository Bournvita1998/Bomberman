from __future__ import print_function
import signal
import copy
import sys
import time
from random import randint


class Gameplay():

    def __init__(self):
        self._me = 0

    def __printboard(
        self,
        w,
     h,
     Matrix,
     x,
     y,
     x1,
     x2,
     x3,
     y1,
     y2,
     y3,
     w1,
     w2,
     w3,
     e1,
     e2,
     e3,
     lives,
     score):

        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
#		self.w1 = w1
#		self.w2 = w2
#		self.w3 = w3


#		print(Matrix[2][4],Matrix[2][5],Matrix[2][6],Matrix[2][7])
#		print(Matrix[3][4],Matrix[3][5],Matrix[3][6],Matrix[3][7])

        for i in range(42):
            for j in range(84):
                if(Matrix[i][j] == "#"):
                    pass
                elif(i == 0 or i == 1 or i == 41 or i == 40):
                    Matrix[i][j] = "X"
# print("#",end="")
                elif(j == 0 or j == 1 or j == 2 or j == 3 or j == 80 or j == 81 or j == 82 or j == 83):
                    Matrix[i][j] = "X"
# print("#",end="")
                elif((j % 8 == 0 or j % 8 == 1 or j % 8 == 2 or j % 8 == 3) and (i % 4 == 0 or i % 4 == 1) and (Matrix[i][j] != 0 and Matrix[i][j] != 1 and Matrix[i][j] != 2 and Matrix[i][j] != 3)):
                    Matrix[i][j] = "X"
# print("#",end="")
                elif((i == x or i == x + 1) and (j == y or j == y + 1 or j == y + 2 or j == y + 3) and (Matrix[i][j] != 0 and Matrix[i][j] != 1 and Matrix[i][j] != 2 and Matrix[i][j] != 3)):
                    Matrix[i][j] = "B"
                elif(Matrix[i][j] != 0 and Matrix[i][j] != 1 and Matrix[i][j] != 2 and Matrix[i][j] != 3):
                    Matrix[i][j] = " "

#					print(" ",end="")
#			print("")
#		print(Matrix[2][4],Matrix[2][5],Matrix[2][6],Matrix[2][7])
#		print(Matrix[3][4],Matrix[3][5],Matrix[3][6],Matrix[3][7])


#		print("1w1=",w1)

        if(Matrix[8][44] != "#" and w1 == 0):
            Matrix[8][44] = "/"
            Matrix[8][45] = "/"
            Matrix[8][46] = "/"
            Matrix[8][47] = "/"
            Matrix[9][44] = "/"
            Matrix[9][45] = "/"
            Matrix[9][46] = "/"
            Matrix[9][47] = "/"

        else:
            w1 = -1
#			print("2w1=",w1)

#		print("3w1=",w1)

        if(Matrix[28][44] != "#" and w2 == 0):
            Matrix[28][44] = "/"
            Matrix[28][45] = "/"
            Matrix[28][46] = "/"
            Matrix[28][47] = "/"
            Matrix[29][44] = "/"
            Matrix[29][45] = "/"
            Matrix[29][46] = "/"
            Matrix[29][47] = "/"
            w2 = -1

#		print("4w1=",w1)

        if(Matrix[12][36] != "#" and w3 == 0):
            Matrix[12][36] = "/"
            Matrix[12][37] = "/"
            Matrix[12][38] = "/"
            Matrix[12][39] = "/"
            Matrix[13][36] = "/"
            Matrix[13][37] = "/"
            Matrix[13][38] = "/"
            Matrix[13][39] = "/"
            w3 = -1

#		print("5w1=",w1)
# ENEMY SPAWN ##########################################################
        if(x1 != 0 and y1 != 0 and e1 == 0):
#			 and x2!=0 and y2!=0 and x3!=0 and y3!=0):
#			print(x1,y1,"----")
            Matrix[x1][y1] = "["
            Matrix[x1][y1 + 1] = "^"
            Matrix[x1][y1 + 2] = "^"
            Matrix[x1][y1 + 3] = "]"
            Matrix[x1 + 1][y1] = "_"
            Matrix[x1 + 1][y1 + 1] = "]"
            Matrix[x1 + 1][y1 + 2] = "["
            Matrix[x1 + 1][y1 + 3] = "_"

#			print(x2,y2,"++++++")
        if(x2 != 0 and y2 != 0 and e2 == 0):
            Matrix[x2][y2] = "["
            Matrix[x2][y2 + 1] = "^"
            Matrix[x2][y2 + 2] = "^"
            Matrix[x2][y2 + 3] = "]"
            Matrix[x2 + 1][y2] = "_"
            Matrix[x2 + 1][y2 + 1] = "]"
            Matrix[x2 + 1][y2 + 2] = "["
            Matrix[x2 + 1][y2 + 3] = "_"

        if(x3 != 0 and y3 != 0 and e3 == 0):
            Matrix[x3][y3] = "["
            Matrix[x3][y3 + 1] = "^"
            Matrix[x3][y3 + 2] = "^"
            Matrix[x3][y3 + 3] = "]"
            Matrix[x3 + 1][y3] = "_"
            Matrix[x3 + 1][y3 + 1] = "]"
            Matrix[x3 + 1][y3 + 2] = "["
            Matrix[x3 + 1][y3 + 3] = "_"

#

#		print("lw1=",w1)

        for i in range(42):
            for j in range(84):
                print(Matrix[i][j], end="")
            print("")

        print(
            "lives=",
            lives,
            "                                                   score=",
            score)

        for i in range(42):
            for j in range(84):
                if(Matrix[i][j] == "#"):
                    Matrix[i][j] = " "
