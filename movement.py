from __future__ import print_function
import signal
import copy
import sys
import time
from random import randint
from gameplay import *


class Movement():

    def UpsideCheck(self, x, y, Matrix, x1, x2, x3, y1, y2, y3, lives):
        if(((x - 1) == x1 and y == y1) or ((x - 1) == x2 and y == y2) or ((x - 1) == x3 and y == y3)):
            lives = lives - 1
            x = 2
            y = 4

        elif(Matrix[x - 1][y] == " "):
            Matrix[x][y] == " "
            Matrix[x][y + 1] == " "
            Matrix[x][y + 2] == " "
            Matrix[x][y + 3] == " "
            Matrix[x + 1][y] == " "
            Matrix[x + 1][y + 1] == " "
            Matrix[x + 1][y + 2] == " "
            Matrix[x + 1][y + 3] == " "

            Matrix[x - 1][y] == "B"
            Matrix[x - 1][y + 1] == "B"
            Matrix[x - 1][y + 2] == "B"
            Matrix[x - 1][y + 3] == "B"
            Matrix[x - 2][y] == "B"
            Matrix[x - 2][y + 1] == "B"
            Matrix[x - 2][y + 2] == "B"
            Matrix[x - 2][y + 3] == "B"

            x = x - 2
            return x

        else:
            return x

    def RightCheck(self, x, y, Matrix, x1, x2, x3, y1, y2, y3, lives):
        if(((x) == x1 and y + 4 == y1) or ((x) == x2 and (y + 4) == y2) or ((x) == x3 and (y + 4) == y3)):
            lives = lives - 1
            x = 2
            y = 4

        elif(Matrix[x][y + 4] == " "):

            Matrix[x][y] == " "
            Matrix[x][y + 1] == " "
            Matrix[x][y + 2] == " "
            Matrix[x][y + 3] == " "
            Matrix[x + 1][y] == " "
            Matrix[x + 1][y + 1] == " "
            Matrix[x + 1][y + 2] == " "
            Matrix[x + 1][y + 3] == " "

            Matrix[x][y + 4] == "B"
            Matrix[x][y + 5] == "B"
            Matrix[x][y + 6] == "B"
            Matrix[x][y + 7] == "B"
            Matrix[x + 1][y + 4] == "B"
            Matrix[x + 1][y + 5] == "B"
            Matrix[x + 1][y + 6] == "B"
            Matrix[x + 1][y + 7] == "B"

            y = y + 4
            return y

        else:
            return y

    def LeftCheck(self, x, y, Matrix, x1, x2, x3, y1, y2, y3, lives):
        if(((x) == x1 and (y - 4) == y1) or ((x) == x2 and (y - 4) == y2) or ((x) == x3 and (y - 4) == y3)):
            lives = lives - 1
            x = 2
            y = 4

        elif(Matrix[x][y - 4] == " "):

            Matrix[x][y] == " "
            Matrix[x][y + 1] == " "
            Matrix[x][y + 2] == " "
            Matrix[x][y + 3] == " "
            Matrix[x + 1][y] == " "
            Matrix[x + 1][y + 1] == " "
            Matrix[x + 1][y + 2] == " "
            Matrix[x + 1][y + 3] == " "

            Matrix[x][y - 1] == "B"
            Matrix[x][y - 2] == "B"
            Matrix[x][y - 3] == "B"
            Matrix[x][y - 4] == "B"
            Matrix[x + 1][y - 1] == "B"
            Matrix[x + 1][y - 2] == "B"
            Matrix[x + 1][y - 3] == "B"
            Matrix[x + 1][y - 4] == "B"

            y = y - 4
            return y

        else:
            return y

    def DownsideCheck(self, x, y, Matrix, x1, x2, x3, y1, y2, y3, lives):
        if(((x + 2) == x1 and y == y1) or ((x + 2) == x2 and y == y2) or ((x + 2) == x3 and y == y3)):
            lives = lives - 1
            x = 2
            y = 4

        elif(Matrix[x + 2][y] == " "):
            Matrix[x + 2][y] == "B"
            Matrix[x + 2][y + 1] == "B"
            Matrix[x + 2][y + 2] == "B"
            Matrix[x + 2][y + 3] == "B"
            Matrix[x + 3][y] == "B"
            Matrix[x + 3][y + 1] == "B"
            Matrix[x + 3][y + 2] == "B"
            Matrix[x + 3][y + 3] == "B"

            Matrix[x + 1][y] == " "
            Matrix[x + 1][y + 1] == " "
            Matrix[x + 1][y + 2] == " "
            Matrix[x + 1][y + 3] == " "
            Matrix[x][y] == " "
            Matrix[x][y + 1] == " "
            Matrix[x][y + 2] == " "
            Matrix[x][y + 3] == " "

            x = x + 2
            return x

        else:
            return x
'''
    def EnemyUpsideCheck(self,x,y,Matrix):
        if(Matrix[x-2][y]==" "):
            Matrix[x][y]==" "
            Matrix[x][y+1]==" "
            Matrix[x][y+2]==" "
            Matrix[x][y+3]==" "
            Matrix[x+1][y]==" "
            Matrix[x+1][y+1]==" "
            Matrix[x+1][y+2]==" "
            Matrix[x+1][y+3]==" "

            Matrix[x-1][y]==" "
            Matrix[x-1][y+1]=="]"
            Matrix[x-1][y+2]=="["
            Matrix[x-1][y+3]==" "
            Matrix[x-2][y]=="["
            Matrix[x-2][y+1]=="^"
            Matrix[x-2][y+2]=="^"
            Matrix[x-2][y+3]=="]"

            x=x-2

            return x

        else:
            return x

    def EnemyDownsideCheck(self,x,y,Matrix):
        if(Matrix[x+2][y]==" "):
            Matrix[x+2][y]=="["
            Matrix[x+2][y+1]=="^"
            Matrix[x+2][y+2]=="^"
            Matrix[x+2][y+3]=="]"
            Matrix[x+3][y]==" "
            Matrix[x+3][y+1]=="]"
            Matrix[x+3][y+2]=="["
            Matrix[x+3][y+3]==" "

            Matrix[x+1][y]==" "
            Matrix[x+1][y+1]==" "
            Matrix[x+1][y+2]==" "
            Matrix[x+1][y+3]==" "
            Matrix[x][y]==" "
            Matrix[x][y+1]==" "
            Matrix[x][y+2]==" "
            Matrix[x][y+3]==" "

            x=x+2
            return x

        else:
            return x

    def EnemyRightsideCheck(self,x,y,Matrix):
        if(Matrix[x][y+4]==" "):

            Matrix[x][y]==" "
            Matrix[x][y+1]==" "
            Matrix[x][y+2]==" "
            Matrix[x][y+3]==" "
            Matrix[x+1][y]==" "
            Matrix[x+1][y+1]==" "
            Matrix[x+1][y+2]==" "
            Matrix[x+1][y+3]==" "

            Matrix[x][y+4]=="["
            Matrix[x][y+5]=="^"
            Matrix[x][y+6]=="^"
            Matrix[x][y+7]=="]"
            Matrix[x+1][y+4]==" "
            Matrix[x+1][y+5]=="]"
            Matrix[x+1][y+6]=="["
            Matrix[x+1][y+7]==" "

            y=y+4
            return y

        else:
            return y

    def EnemyLeftsideCheck(self,x,y,Matrix):
        if(Matrix[x][y-4]==" "):

            Matrix[x][y]==" "
            Matrix[x][y+1]==" "
            Matrix[x][y+2]==" "
            Matrix[x][y+3]==" "
            Matrix[x+1][y]==" "
            Matrix[x+1][y+1]==" "
            Matrix[x+1][y+2]==" "
            Matrix[x+1][y+3]==" "

            Matrix[x][y-1]=="["
            Matrix[x][y-2]=="^"
            Matrix[x][y-3]=="^"
            Matrix[x][y-4]=="]"
            Matrix[x+1][y-1]==" "
            Matrix[x+1][y-2]=="]"
            Matrix[x+1][y-3]=="["
            Matrix[x+1][y-4]==" "

            y=y-4
            return y

        else:
            return y
            '''
