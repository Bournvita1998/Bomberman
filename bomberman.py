from __future__ import print_function
import signal
import copy
import sys
import time
from random import randint
from gameplay import *
from alarmexception import *
from getchunix import *
from movement import *
import os

g = Gameplay()

getch = GetchUnix()
mv = Movement()


def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


Matrix = [[' ' for x in range(84)] for y in range(42)]

lol = 3
x1, x2, y1, y2, x3, y3 = 0, 0, 0, 0, 0, 0
ix, iy = 2, 4
w, h = 100, 100
w1, w2, w3 = 0, 0, 0
e1, e2, e3 = 0, 0, 0
lives = 3
score = 0

flag1, flag2, flag3 = 1, 1, 1
g._Gameplay__printboard(
    42,
     84,
     Matrix,
     ix,
     iy,
     0,
     0,
     0,
     0,
     0,
     0,
     w1,
     w2,
     w3,
     e1,
     e2,
     e3,
     lives,
     score)
while (1):

    if(flag1 == 0 and flag2 == 0 and flag3 == 0):
        break

    if(flag1 == 1):
        x1 = randint(1, 20)
        y1 = randint(1, 20)
    if(flag2 == 1):
        x2 = randint(1, 20)
        y2 = randint(1, 20)
    if(flag3 == 1):
        x3 = randint(1, 20)
        y3 = randint(1, 20)

    if(Matrix[2 * x1][4 * y1] == " "):
        flag1 = 0

    if(Matrix[2 * x2][4 * y2] == " "):
        flag2 = 0

    if(Matrix[2 * x3][4 * y3] == " "):
        flag3 = 0

# print(2*x1,2*x2,2*x3,4*y1,4*y2,4*y3)

flg = 0
bx = 0
by = 0
if(lol == 0 or lol == -1):
    lol = 3

while (1):
    c = input_to()
    if (c == 'q'):
        print("GOOD BYEE")
        sys.exit(0)
    elif(c == 'w'):
        ix = mv.UpsideCheck(ix, iy, Matrix, x1, x2, x3, y1, y2, y3, lives)
    elif(c == 'd'):
        iy = mv.RightCheck(ix, iy, Matrix, x1, x2, x3, y1, y2, y3, lives)

    elif(c == 'a'):
        iy = mv.LeftCheck(ix, iy, Matrix, x1, x2, x3, y1, y2, y3, lives)

    elif(c == 's'):
        ix = mv.DownsideCheck(ix, iy, Matrix, x1, x2, x3, y1, y2, y3, lives)

    elif(c == 'b'):
        lol = 3
        flg = -1
        bx = ix
        by = iy

    if(flg == -1 and (lol != 0 or lol != -1)):
        Matrix[bx][by] = lol
        Matrix[bx][by + 1] = lol
        Matrix[bx][by + 3] = lol
        Matrix[bx][by + 2] = lol
        Matrix[bx + 1][by] = lol
        Matrix[bx + 1][by + 1] = lol
        Matrix[bx + 1][by + 2] = lol
        Matrix[bx + 1][by + 3] = lol

        lol = lol - 1

        if(lol == -1):
            if(Matrix[bx - 2][by] != "X" or Matrix[bx - 2][by] == "["):
                if((bx - 2) == 8 and (by) == 44):
                    w1 = -1
                    score = score + 20
                if((bx - 2) == 28 and (by) == 44):
                    score = score + 20
                    w2 = -1
                if((bx - 2) == 12 and (by) == 36):
                    score = score + 20
                    w3 = -1

                if((bx - 2) == 2 * x1 and (by) == 4 * y1):
                    e1 = -1
                if((bx - 2) == 2 * x2 and (by) == 4 * y2):
                    e2 = -1
                if((bx - 2) == 2 * x3 and (by) == 4 * y3):
                    e3 = -1

                if((bx - 2) == ix and by == iy):
                    lives = lives - 1
                    ix = 2
                    iy = 4

                Matrix[bx - 2][by] = "#"
                Matrix[bx - 2][by + 1] = "#"
                Matrix[bx - 2][by + 2] = "#"
                Matrix[bx - 2][by + 3] = "#"
                Matrix[bx - 1][by] = "#"
                Matrix[bx - 1][by + 1] = "#"
                Matrix[bx - 1][by + 2] = "#"
                Matrix[bx - 1][by + 3] = "#"

            if((bx) == ix and by == iy):
                lives = lives - 1
                ix = 2
                iy = 4

            Matrix[bx][by] = "#"
            Matrix[bx][by + 1] = "#"
            Matrix[bx][by + 2] = "#"
            Matrix[bx][by + 3] = "#"
            Matrix[bx + 1][by] = "#"
            Matrix[bx + 1][by + 1] = "#"
            Matrix[bx + 1][by + 2] = "#"
            Matrix[bx + 1][by + 3] = "#"

            if(Matrix[bx + 2][by] != "X" or Matrix[bx + 2][by] == "["):
                if((bx + 2) == 8 and (by) == 44):
                    score = score + 20
                    w1 = -1
                if((bx + 2) == 28 and (by) == 44):
                    score = score + 20
                    w2 = -1
                if((bx + 2) == 12 and (by) == 36):
                    score = score + 20
                    w3 = -1

                if((bx + 2) == 2 * x1 and (by) == 4 * y1):
                    score = score + 100
                    e1 = -1
                if((bx + 2) == 2 * x2 and (by) == 4 * y2):
                    score = score + 100
                    e2 = -1
                if((bx + 2) == 2 * x3 and (by) == 4 * y3):
                    score = score + 100
                    e3 = -1

                if((bx + 2) == ix and by == iy):
                    lives = lives - 1
                    ix = 2
                    iy = 4

                Matrix[bx + 2][by] = "#"
                Matrix[bx + 2][by + 1] = "#"
                Matrix[bx + 2][by + 2] = "#"
                Matrix[bx + 2][by + 3] = "#"
                Matrix[bx + 3][by] = "#"
                Matrix[bx + 3][by + 1] = "#"
                Matrix[bx + 3][by + 2] = "#"
                Matrix[bx + 3][by + 3] = "#"

            if(Matrix[bx][by - 4] != "X" or Matrix[bx][by - 4] == "["):
                if((bx) == 8 and (by - 4) == 44):
                    score = score + 20
                    w1 = -1
                if((bx) == 28 and (by - 4) == 44):
                    score = score + 20
                    w2 = -1
                if((bx) == 12 and (by - 4) == 36):
                    score = score + 20
                    w3 = -1

                if((bx) == 2 * x1 and (by - 4) == 4 * y1):
                    score = score + 100
                    e1 = -1
                if((bx) == 2 * x2 and (by - 4) == 4 * y2):
                    score = score + 100
                    e2 = -1
                if((bx) == 2 * x3 and (by - 4) == 4 * y3):
                    score = score + 100
                    e3 = -1

                if((bx) == ix and (by - 4) == iy):
                    lives = lives - 1
                    ix = 2
                    iy = 4

                Matrix[bx][by - 4] = "#"
                Matrix[bx][by - 3] = "#"
                Matrix[bx][by - 2] = "#"
                Matrix[bx][by - 1] = "#"
                Matrix[bx + 1][by - 4] = "#"
                Matrix[bx + 1][by - 3] = "#"
                Matrix[bx + 1][by - 2] = "#"
                Matrix[bx + 1][by - 1] = "#"

            if(Matrix[bx][by + 4] != "X" or Matrix[bx][by + 4] == "["):
                if((bx) == 8 and (by + 4) == 44):
                    score = score + 20
                    w1 = -1
                if((bx) == 28 and (by + 4) == 44):
                    score = score + 20
                    w2 = -1
                if((bx) == 12 and (by + 4) == 36):
                    score = score + 20
                    w3 = -1

                if((bx) == 2 * x1 and (by + 4) == 4 * y1):
                    score = score + 100
                    e1 = -1
                if((bx) == 2 * x2 and (by + 4) == 4 * y2):
                    score = score + 100
                    e2 = -1
                if((bx) == 2 * x3 and (by + 4) == 4 * y3):
                    score = score + 100
                    e3 = -1

                if((bx) == ix and (by + 4) == iy):
                    lives = lives - 1
                    ix = 2
                    iy = 4

                Matrix[bx][by + 4] = "#"
                Matrix[bx][by + 5] = "#"
                Matrix[bx][by + 6] = "#"
                Matrix[bx][by + 7] = "#"
                Matrix[bx + 1][by + 4] = "#"
                Matrix[bx + 1][by + 5] = "#"
                Matrix[bx + 1][by + 6] = "#"
                Matrix[bx + 1][by + 7] = "#"

#			if((bx-2)==2*x1 and by==4*y1):
#				x1=0
#				y1=0

    else:
        lol = 3
        flg = 0

    x1 = 2 * x1
    x2 = 2 * x2
    x3 = 2 * x3
    y1 = 4 * y1
    y2 = 4 * y2
    y3 = 4 * y3

#	print("loopw1=",w1)
    os.system('tput reset')
    g._Gameplay__printboard(
        42,
        84,
     Matrix,
     ix,
     iy,
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
     score)
    if(lives == 0 or score == 360):
        print("GAME OVER")
        break

    x1 = x1 / 2
    x2 = x2 / 2
    x3 = x3 / 2
    y1 = y1 / 4
    y2 = y2 / 4
    y3 = y3 / 4

#	print(x1,y1,"before sending to looop")
    flag = 0
    while (1):
        flag = randint(1, 4)
        w = x1
        z = y1
        if(flag == 1):
            if((2 * x1 - 2) == ix and (4 * y1) == iy):
                ix = 2
                iy = 4
                lives = lives - 1
                Matrix[2 * x1 - 2][4 * y1] = "["
                Matrix[2 * x1 - 2][4 * y1 + 1] = "^"
                Matrix[2 * x1 - 2][4 * y1 + 2] = "^"
                Matrix[2 * x1 - 2][4 * y1 + 3] = "]"
                Matrix[2 * x1 - 1][4 * y1] = "_"
                Matrix[2 * x1 - 1][4 * y1 + 1] = "]"
                Matrix[2 * x1 - 1][4 * y1 + 2] = "["
                Matrix[2 * x1 - 1][4 * y1 + 3] = "_"

                Matrix[2 * x1][2 * y1] = " "
                Matrix[2 * x1][2 * y1 + 1] = " "
                Matrix[2 * x1][2 * y1 + 2] = " "
                Matrix[2 * x1][2 * y1 + 3] = " "
                Matrix[2 * x1 + 1][2 * y1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 2] = " "
                Matrix[2 * x1 + 1][2 * y1 + 3] = " "

                x1 = x1 - 1
            else:
                x1 = x1

            if(Matrix[2 * x1 - 2][4 * y1] == " "):
                Matrix[2 * x1 - 2][4 * y1] = "["
                Matrix[2 * x1 - 2][4 * y1 + 1] = "^"
                Matrix[2 * x1 - 2][4 * y1 + 2] = "^"
                Matrix[2 * x1 - 2][4 * y1 + 3] = "]"
                Matrix[2 * x1 - 1][4 * y1] = "_"
                Matrix[2 * x1 - 1][4 * y1 + 1] = "]"
                Matrix[2 * x1 - 1][4 * y1 + 2] = "["
                Matrix[2 * x1 - 1][4 * y1 + 3] = "_"

                Matrix[2 * x1][2 * y1] = " "
                Matrix[2 * x1][2 * y1 + 1] = " "
                Matrix[2 * x1][2 * y1 + 2] = " "
                Matrix[2 * x1][2 * y1 + 3] = " "
                Matrix[2 * x1 + 1][2 * y1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 2] = " "
                Matrix[2 * x1 + 1][2 * y1 + 3] = " "

                x1 = x1 - 1
            else:
                x1 = x1

#			x1=mv.EnemyUpsideCheck(x1,y1,Matrix)
#			print("up-movement")
            if(x1 != w):
#				print("loop breaked")
                break
        elif(flag == 2):

            if(2 * x1 == ix and (4 * y1 + 4) == iy):
                Matrix[2 * x1][4 * y1 + 4] = "["
                Matrix[2 * x1][4 * y1 + 5] = "^"
                Matrix[2 * x1][4 * y1 + 6] = "^"
                Matrix[2 * x1][4 * y1 + 7] = "]"
                Matrix[2 * x1 + 1][4 * y1 + 4] = "_"
                Matrix[2 * x1 + 1][4 * y1 + 5] = "]"
                Matrix[2 * x1 + 1][4 * y1 + 6] = "["
                ix = 2
                iy = 4
                Matrix[2 * x1][2 * y1] = " "
                Matrix[2 * x1][2 * y1 + 1] = " "
                Matrix[2 * x1][2 * y1 + 2] = " "
                Matrix[2 * x1][2 * y1 + 3] = " "
                Matrix[2 * x1 + 1][2 * y1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 2] = " "
                Matrix[2 * x1 + 1][2 * y1 + 3] = " "

                y1 = y1 + 1
            else:
                y1 = y1

            if(Matrix[2 * x1][4 * y1 + 4] == " "):
                Matrix[2 * x1][4 * y1 + 4] = "["
                Matrix[2 * x1][4 * y1 + 5] = "^"
                Matrix[2 * x1][4 * y1 + 6] = "^"
                Matrix[2 * x1][4 * y1 + 7] = "]"
                Matrix[2 * x1 + 1][4 * y1 + 4] = "_"
                Matrix[2 * x1 + 1][4 * y1 + 5] = "]"
                Matrix[2 * x1 + 1][4 * y1 + 6] = "["
                Matrix[2 * x1 + 1][4 * y1 + 7] = "_"

                Matrix[2 * x1][2 * y1] = " "
                Matrix[2 * x1][2 * y1 + 1] = " "
                Matrix[2 * x1][2 * y1 + 2] = " "
                Matrix[2 * x1][2 * y1 + 3] = " "
                Matrix[2 * x1 + 1][2 * y1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 2] = " "
                Matrix[2 * x1 + 1][2 * y1 + 3] = " "

                y1 = y1 + 1
            else:
                y1 = y1

#			y1=mv.EnemyRightsideCheck(x1,y1,Matrix)
#			print("right-movement")
            if(y1 != z):
#				print("loop breaked")
                break
        elif(flag == 3):
            if((2 * x1 + 2) == ix and (4 * y1) == iy):
                ix = 2
                iy = 4
                lives = lives - 1
                Matrix[2 * x1 + 2][4 * y1] = "["
                Matrix[2 * x1 + 2][4 * y1 + 1] = "^"
                Matrix[2 * x1 + 2][4 * y1 + 2] = "^"
                Matrix[2 * x1 + 2][4 * y1 + 3] = "]"
                Matrix[2 * x1 + 3][4 * y1] = "_"
                Matrix[2 * x1 + 3][4 * y1 + 1] = "]"
                Matrix[2 * x1 + 3][4 * y1 + 2] = "["
                Matrix[2 * x1 + 3][4 * y1 + 3] = "_"

                Matrix[2 * x1][2 * y1] = " "
                Matrix[2 * x1][2 * y1 + 1] = " "
                Matrix[2 * x1][2 * y1 + 2] = " "
                Matrix[2 * x1][2 * y1 + 3] = " "
                Matrix[2 * x1 + 1][2 * y1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 2] = " "
                Matrix[2 * x1 + 1][2 * y1 + 3] = " "

                x1 = x1 + 1
            else:
                x1 = x1

            if(Matrix[2 * x1 + 2][4 * y1] == " "):
                Matrix[2 * x1 + 2][4 * y1] = "["
                Matrix[2 * x1 + 2][4 * y1 + 1] = "^"
                Matrix[2 * x1 + 2][4 * y1 + 2] = "^"
                Matrix[2 * x1 + 2][4 * y1 + 3] = "]"
                Matrix[2 * x1 + 3][4 * y1] = "_"
                Matrix[2 * x1 + 3][4 * y1 + 1] = "]"
                Matrix[2 * x1 + 3][4 * y1 + 2] = "["
                Matrix[2 * x1 + 3][4 * y1 + 3] = "_"

                Matrix[2 * x1][2 * y1] = " "
                Matrix[2 * x1][2 * y1 + 1] = " "
                Matrix[2 * x1][2 * y1 + 2] = " "
                Matrix[2 * x1][2 * y1 + 3] = " "
                Matrix[2 * x1 + 1][2 * y1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 2] = " "
                Matrix[2 * x1 + 1][2 * y1 + 3] = " "

                x1 = x1 + 1
            else:
                x1 = x1


#			x1=mv.EnemyDownsideCheck(x1,y1,Matrix)
            # print("down-movement")
            if(x1 != w):
        #		print("loop breaked")
                break
        elif(flag == 4):
            if((2 * x1) == ix and (4 * y1 - 4) == iy):
                ix = 2
                iy = 4
                lives = lives - 1
                Matrix[2 * x1][4 * y1 - 4] = "["
                Matrix[2 * x1][4 * y1 - 3] = "^"
                Matrix[2 * x1][4 * y1 - 2] = "^"
                Matrix[2 * x1][4 * y1 - 1] = "]"
                Matrix[2 * x1 + 1][4 * y1 - 4] = "_"
                Matrix[2 * x1 + 1][4 * y1 - 3] = "]"
                Matrix[2 * x1 + 1][4 * y1 - 2] = "["
                Matrix[2 * x1 + 1][4 * y1 - 1] = "_"

                Matrix[2 * x1][2 * y1] = " "
                Matrix[2 * x1][2 * y1 + 1] = " "
                Matrix[2 * x1][2 * y1 + 2] = " "
                Matrix[2 * x1][2 * y1 + 3] = " "
                Matrix[2 * x1 + 1][2 * y1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 2] = " "
                Matrix[2 * x1 + 1][2 * y1 + 3] = " "

                y1 = y1 - 1
            else:
                y1 = y1

            if(Matrix[2 * x1][4 * y1 - 4] == " "):
                Matrix[2 * x1][4 * y1 - 4] = "["
                Matrix[2 * x1][4 * y1 - 3] = "^"
                Matrix[2 * x1][4 * y1 - 2] = "^"
                Matrix[2 * x1][4 * y1 - 1] = "]"
                Matrix[2 * x1 + 1][4 * y1 - 4] = "_"
                Matrix[2 * x1 + 1][4 * y1 - 3] = "]"
                Matrix[2 * x1 + 1][4 * y1 - 2] = "["
                Matrix[2 * x1 + 1][4 * y1 - 1] = "_"

                Matrix[2 * x1][2 * y1] = " "
                Matrix[2 * x1][2 * y1 + 1] = " "
                Matrix[2 * x1][2 * y1 + 2] = " "
                Matrix[2 * x1][2 * y1 + 3] = " "
                Matrix[2 * x1 + 1][2 * y1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 1] = " "
                Matrix[2 * x1 + 1][2 * y1 + 2] = " "
                Matrix[2 * x1 + 1][2 * y1 + 3] = " "

                y1 = y1 - 1
            else:
                y1 = y1

#			y1=mv.EnemyLeftsideCheck(x1/2,y1/2,Matrix)
    #		print("left-movement")
            if(y1 != z):
#				print("loop breaked")
                break


# 2nd enemy #########################################################

    flag = 0
    while (1):
        flag = randint(1, 4)
        w = x2
        z = y2
        if(flag == 1):
            if((2 * x2 - 2) == ix and (4 * y2) == iy):
                ix = 2
                iy = 4
                lives = lives - 1
                Matrix[2 * x2 - 2][4 * y2] = "["
                Matrix[2 * x2 - 2][4 * y2 + 1] = "^"
                Matrix[2 * x2 - 2][4 * y2 + 2] = "^"
                Matrix[2 * x2 - 2][4 * y2 + 3] = "]"
                Matrix[2 * x2 - 1][4 * y2] = "_"
                Matrix[2 * x2 - 1][4 * y2 + 1] = "]"
                Matrix[2 * x2 - 1][4 * y2 + 2] = "["
                Matrix[2 * x2 - 1][4 * y2 + 3] = "_"

                Matrix[2 * x2][2 * y2] = " "
                Matrix[2 * x2][2 * y2 + 1] = " "
                Matrix[2 * x2][2 * y2 + 2] = " "
                Matrix[2 * x2][2 * y2 + 3] = " "
                Matrix[2 * x2 + 1][2 * y2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 1] = " "
                Matrix[2 * x2 + 1][2 * y2 + 2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 3] = " "

                x2 = x2 - 1
            else:
                x2 = x2

            if(Matrix[2 * x2 - 2][4 * y2] == " "):
                Matrix[2 * x2 - 2][4 * y2] = "["
                Matrix[2 * x2 - 2][4 * y2 + 1] = "^"
                Matrix[2 * x2 - 2][4 * y2 + 2] = "^"
                Matrix[2 * x2 - 2][4 * y2 + 3] = "]"
                Matrix[2 * x2 - 1][4 * y2] = "_"
                Matrix[2 * x2 - 1][4 * y2 + 1] = "]"
                Matrix[2 * x2 - 1][4 * y2 + 2] = "["
                Matrix[2 * x2 - 1][4 * y2 + 3] = "_"

                Matrix[2 * x2][2 * y2] = " "
                Matrix[2 * x2][2 * y2 + 1] = " "
                Matrix[2 * x2][2 * y2 + 2] = " "
                Matrix[2 * x2][2 * y2 + 3] = " "
                Matrix[2 * x2 + 1][2 * y2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 1] = " "
                Matrix[2 * x2 + 1][2 * y2 + 2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 3] = " "

                x2 = x2 - 1
            else:
                x2 = x2

#			x1=mv.EnemyUpsideCheck(x1,y1,Matrix)
#			print("up-movement")
            if(x2 != w):
#				print("loop breaked")
                break
        elif(flag == 2):
            if((2 * x2) == ix and (4 * y2 + 4) == iy):
                ix = 2
                lives = lives - 1
                iy = 4
                Matrix[2 * x2][4 * y2 + 4] = "["
                Matrix[2 * x2][4 * y2 + 5] = "^"
                Matrix[2 * x2][4 * y2 + 6] = "^"
                Matrix[2 * x2][4 * y2 + 7] = "]"
                Matrix[2 * x2 + 1][4 * y2 + 4] = "_"
                Matrix[2 * x2 + 1][4 * y2 + 5] = "]"
                Matrix[2 * x2 + 1][4 * y2 + 6] = "["
                Matrix[2 * x2 + 1][4 * y2 + 7] = "_"

                Matrix[2 * x2][2 * y2] = " "
                Matrix[2 * x2][2 * y2 + 1] = " "
                Matrix[2 * x2][2 * y2 + 2] = " "
                Matrix[2 * x2][2 * y2 + 3] = " "
                Matrix[2 * x2 + 1][2 * y2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 1] = " "
                Matrix[2 * x2 + 1][2 * y2 + 2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 3] = " "

                y2 = y2 + 1
            else:
                y2 = y2

            if(Matrix[2 * x2][4 * y2 + 4] == " "):
                Matrix[2 * x2][4 * y2 + 4] = "["
                Matrix[2 * x2][4 * y2 + 5] = "^"
                Matrix[2 * x2][4 * y2 + 6] = "^"
                Matrix[2 * x2][4 * y2 + 7] = "]"
                Matrix[2 * x2 + 1][4 * y2 + 4] = "_"
                Matrix[2 * x2 + 1][4 * y2 + 5] = "]"
                Matrix[2 * x2 + 1][4 * y2 + 6] = "["
                Matrix[2 * x2 + 1][4 * y2 + 7] = "_"

                Matrix[2 * x2][2 * y2] = " "
                Matrix[2 * x2][2 * y2 + 1] = " "
                Matrix[2 * x2][2 * y2 + 2] = " "
                Matrix[2 * x2][2 * y2 + 3] = " "
                Matrix[2 * x2 + 1][2 * y2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 1] = " "
                Matrix[2 * x2 + 1][2 * y2 + 2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 3] = " "

                y2 = y2 + 1
            else:
                y2 = y2

#			y1=mv.EnemyRightsideCheck(x1,y1,Matrix)
#			print("right-movement")
            if(y2 != z):
#				print("loop breaked")
                break
        elif(flag == 3):
            if((2 * x2 + 2) == ix and (4 * y2) == iy):
                ix = 2
                iy = 4
                lives = lives - 1
                Matrix[2 * x2 + 2][4 * y2] = "["
                Matrix[2 * x2 + 2][4 * y2 + 1] = "^"
                Matrix[2 * x2 + 2][4 * y2 + 2] = "^"
                Matrix[2 * x2 + 2][4 * y2 + 3] = "]"
                Matrix[2 * x2 + 3][4 * y2] = "_"
                Matrix[2 * x2 + 3][4 * y2 + 1] = "]"
                Matrix[2 * x2 + 3][4 * y2 + 2] = "["
                Matrix[2 * x2 + 3][4 * y2 + 3] = "_"

                Matrix[2 * x2][2 * y2] = " "
                Matrix[2 * x2][2 * y2 + 1] = " "
                Matrix[2 * x2][2 * y2 + 2] = " "
                Matrix[2 * x2][2 * y2 + 3] = " "
                Matrix[2 * x2 + 1][2 * y2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 1] = " "
                Matrix[2 * x2 + 1][2 * y2 + 2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 3] = " "

                x2 = x2 + 1
            else:
                x2 = x2

            if(Matrix[2 * x2 + 2][4 * y2] == " "):
                Matrix[2 * x2 + 2][4 * y2] = "["
                Matrix[2 * x2 + 2][4 * y2 + 1] = "^"
                Matrix[2 * x2 + 2][4 * y2 + 2] = "^"
                Matrix[2 * x2 + 2][4 * y2 + 3] = "]"
                Matrix[2 * x2 + 3][4 * y2] = "_"
                Matrix[2 * x2 + 3][4 * y2 + 1] = "]"
                Matrix[2 * x2 + 3][4 * y2 + 2] = "["
                Matrix[2 * x2 + 3][4 * y2 + 3] = "_"

                Matrix[2 * x2][2 * y2] = " "
                Matrix[2 * x2][2 * y2 + 1] = " "
                Matrix[2 * x2][2 * y2 + 2] = " "
                Matrix[2 * x2][2 * y2 + 3] = " "
                Matrix[2 * x2 + 1][2 * y2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 1] = " "
                Matrix[2 * x2 + 1][2 * y2 + 2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 3] = " "

                x2 = x2 + 1
            else:
                x2 = x2


#			x1=mv.EnemyDownsideCheck(x1,y1,Matrix)
            # print("down-movement")
            if(x2 != w):
        #		print("loop breaked")
                break
        elif(flag == 4):
            if((2 * x2) == ix and (4 * y2 - 4) == iy):
                ix = 2
                iy = 4
                lives = lives - 1
                Matrix[2 * x2][4 * y2 - 4] = "["
                Matrix[2 * x2][4 * y2 - 3] = "^"
                Matrix[2 * x2][4 * y2 - 2] = "^"
                Matrix[2 * x2][4 * y2 - 1] = "]"
                Matrix[2 * x2 + 1][4 * y2 - 4] = "_"
                Matrix[2 * x2 + 1][4 * y2 - 3] = "]"
                Matrix[2 * x2 + 1][4 * y2 - 2] = "["
                Matrix[2 * x2 + 1][4 * y2 - 1] = "_"

                Matrix[2 * x2][2 * y2] = " "
                Matrix[2 * x2][2 * y2 + 1] = " "
                Matrix[2 * x2][2 * y2 + 2] = " "
                Matrix[2 * x2][2 * y2 + 3] = " "
                Matrix[2 * x2 + 1][2 * y2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 1] = " "
                Matrix[2 * x2 + 1][2 * y2 + 2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 3] = " "

                y2 = y2 - 1
            else:
                y2 = y2

            if(Matrix[2 * x2][4 * y2 - 4] == " "):
                Matrix[2 * x2][4 * y2 - 4] = "["
                Matrix[2 * x2][4 * y2 - 3] = "^"
                Matrix[2 * x2][4 * y2 - 2] = "^"
                Matrix[2 * x2][4 * y2 - 1] = "]"
                Matrix[2 * x2 + 1][4 * y2 - 4] = "_"
                Matrix[2 * x2 + 1][4 * y2 - 3] = "]"
                Matrix[2 * x2 + 1][4 * y2 - 2] = "["
                Matrix[2 * x2 + 1][4 * y2 - 1] = "_"

                Matrix[2 * x2][2 * y2] = " "
                Matrix[2 * x2][2 * y2 + 1] = " "
                Matrix[2 * x2][2 * y2 + 2] = " "
                Matrix[2 * x2][2 * y2 + 3] = " "
                Matrix[2 * x2 + 1][2 * y2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 1] = " "
                Matrix[2 * x2 + 1][2 * y2 + 2] = " "
                Matrix[2 * x2 + 1][2 * y2 + 3] = " "

                y2 = y2 - 1
            else:
                y2 = y2

#			y1=mv.EnemyLeftsideCheck(x1/2,y1/2,Matrix)
    #		print("left-movement")
            if(y2 != z):
#				print("loop breaked")
                break


# 3rd enemy #########################################################

    flag = 0
    while (1):
        flag = randint(1, 4)
        w = x3
        z = y3
        if(flag == 1):
            if((2 * x3 - 2) == ix and (4 * y3) == iy):
                ix = 2
                iy = 4
                lives = lives - 1
                Matrix[2 * x3 - 2][4 * y3] = "["
                Matrix[2 * x3 - 2][4 * y3 + 1] = "^"
                Matrix[2 * x3 - 2][4 * y3 + 2] = "^"
                Matrix[2 * x3 - 2][4 * y3 + 3] = "]"
                Matrix[2 * x3 - 1][4 * y3] = "_"
                Matrix[2 * x3 - 1][4 * y3 + 1] = "]"
                Matrix[2 * x3 - 1][4 * y3 + 2] = "["
                Matrix[2 * x3 - 1][4 * y3 + 3] = "_"

                Matrix[2 * x3][2 * y3] = " "
                Matrix[2 * x3][2 * y3 + 1] = " "
                Matrix[2 * x3][2 * y3 + 2] = " "
                Matrix[2 * x3][2 * y3 + 3] = " "
                Matrix[2 * x3 + 1][2 * y3] = " "
                Matrix[2 * x3 + 1][2 * y3 + 1] = " "
                Matrix[2 * x3 + 1][2 * y3 + 2] = " "
                Matrix[2 * x3 + 1][2 * y3 + 3] = " "

                x3 = x3 - 1
            else:
                x3 = x3

            if(Matrix[2 * x3 - 2][4 * y3] == " "):
                Matrix[2 * x3 - 2][4 * y3] = "["
                Matrix[2 * x3 - 2][4 * y3 + 1] = "^"
                Matrix[2 * x3 - 2][4 * y3 + 2] = "^"
                Matrix[2 * x3 - 2][4 * y3 + 3] = "]"
                Matrix[2 * x3 - 1][4 * y3] = "_"
                Matrix[2 * x3 - 1][4 * y3 + 1] = "]"
                Matrix[2 * x3 - 1][4 * y3 + 2] = "["
                Matrix[2 * x3 - 1][4 * y3 + 3] = "_"

                Matrix[2 * x3][2 * y3] = " "
                Matrix[2 * x3][2 * y3 + 1] = " "
                Matrix[2 * x3][2 * y3 + 2] = " "
                Matrix[2 * x3][2 * y3 + 3] = " "
                Matrix[2 * x3 + 1][2 * y3] = " "
                Matrix[2 * x3 + 1][2 * y3 + 1] = " "
                Matrix[2 * x3 + 1][2 * y3 + 2] = " "
                Matrix[2 * x3 + 1][2 * y3 + 3] = " "

                x3 = x3 - 1
            else:
                x3 = x3

#			x1=mv.EnemyUpsideCheck(x1,y1,Matrix)
#			print("up-movement")
            if(x3 != w):
#				print("loop breaked")
                break
        elif(flag == 2):
            if((2 * x3) == ix and (4 * y3 + 4) == iy):
                ix = 2
                iy = 4
                lives = lives - 1
                Matrix[2 * x3][4 * y3 + 4] = "["
                Matrix[2 * x3][4 * y3 + 5] = "^"
                Matrix[2 * x3][4 * y3 + 6] = "^"
                Matrix[2 * x3][4 * y3 + 7] = "]"
                Matrix[2 * x3 + 1][4 * y3 + 4] = "_"
                Matrix[2 * x3 + 1][4 * y3 + 5] = "]"
                Matrix[2 * x3 + 1][4 * y3 + 6] = "["
                Matrix[2 * x3 + 1][4 * y3 + 7] = "_"
                Matrix[2 * x3][2 * y3] = " "
                Matrix[2 * x3][2 * y3 + 1] = " "
                Matrix[2 * x3][2 * y3 + 2] = " "
                Matrix[2 * x3][2 * y3 + 3] = " "
                Matrix[2 * x3 + 1][2 * y3] = " "
                Matrix[2 * x3 + 1][2 * y3 + 1] = " "
                Matrix[2 * x3 + 1][2 * y3 + 2] = " "
                Matrix[2 * x3 + 1][2 * y3 + 3] = " "

                y3 = y3 + 1
            else:
                y3 = y3

            if(Matrix[2 * x3][4 * y3 + 4] == " "):
                Matrix[2 * x3][4 * y3 + 4] = "["
                Matrix[2 * x3][4 * y3 + 5] = "^"
                Matrix[2 * x3][4 * y3 + 6] = "^"
                Matrix[2 * x3][4 * y3 + 7] = "]"
                Matrix[2 * x3 + 1][4 * y3 + 4] = "_"
                Matrix[2 * x3 + 1][4 * y3 + 5] = "]"
                Matrix[2 * x3 + 1][4 * y3 + 6] = "["
                Matrix[2 * x3 + 1][4 * y3 + 7] = "_"

                Matrix[2 * x3][2 * y3] = " "
                Matrix[2 * x3][2 * y3 + 1] = " "
                Matrix[2 * x3][2 * y3 + 2] = " "
                Matrix[2 * x3][2 * y3 + 3] = " "
                Matrix[2 * x3 + 1][2 * y3] = " "
                Matrix[2 * x3 + 1][2 * y3 + 1] = " "
                Matrix[2 * x3 + 1][2 * y3 + 2] = " "
                Matrix[2 * x3 + 1][2 * y3 + 3] = " "

                y3 = y3 + 1
            else:
                y3 = y3

#			y1=mv.EnemyRightsideCheck(x1,y1,Matrix)
#			print("right-movement")
            if(y3 != z):
#				print("loop breaked")
                break
        elif(flag == 3):
            if((2 * x3 + 2) == ix and (4 * y3) == iy):
                ix = 2
                iy = 4
                lives = lives - 1
                Matrix[2 * x3 + 2][4 * y3] = "["
                Matrix[2 * x3 + 2][4 * y3 + 1] = "^"
                Matrix[2 * x3 + 2][4 * y3 + 2] = "^"
                Matrix[2 * x3 + 2][4 * y3 + 3] = "]"
                Matrix[2 * x3 + 3][4 * y3] = "_"
                Matrix[2 * x3 + 3][4 * y3 + 1] = "]"
                Matrix[2 * x3 + 3][4 * y3 + 2] = "["
                Matrix[2 * x3 + 3][4 * y3 + 3] = "_"
                Matrix[2 * x3][2 * y3] = " "
                Matrix[2 * x3][2 * y3 + 1] = " "
                Matrix[2 * x3][2 * y3 + 2] = " "
                Matrix[2 * x3][2 * y3 + 3] = " "
                Matrix[2 * x3 + 1][2 * y3] = " "
                Matrix[2 * x3 + 1][2 * y3 + 1] = " "
                Matrix[2 * x3 + 1][2 * y3 + 2] = " "
                Matrix[2 * x3 + 1][2 * y3 + 3] = " "

                x3 = x3 + 1
            else:
                x3 = x3

            if(Matrix[2 * x3 + 2][4 * y3] == " "):
                Matrix[2 * x3 + 2][4 * y3] = "["
                Matrix[2 * x3 + 2][4 * y3 + 1] = "^"
                Matrix[2 * x3 + 2][4 * y3 + 2] = "^"
                Matrix[2 * x3 + 2][4 * y3 + 3] = "]"
                Matrix[2 * x3 + 3][4 * y3] = "_"
                Matrix[2 * x3 + 3][4 * y3 + 1] = "]"
                Matrix[2 * x3 + 3][4 * y3 + 2] = "["
                Matrix[2 * x3 + 3][4 * y3 + 3] = "_"

                Matrix[2 * x3][2 * y3] = " "
                Matrix[2 * x3][2 * y3 + 1] = " "
                Matrix[2 * x3][2 * y3 + 2] = " "
                Matrix[2 * x3][2 * y3 + 3] = " "
                Matrix[2 * x3 + 1][2 * y3] = " "
                Matrix[2 * x3 + 1][2 * y3 + 1] = " "
                Matrix[2 * x3 + 1][2 * y3 + 2] = " "
                Matrix[2 * x3 + 1][2 * y3 + 3] = " "

                x3 = x3 + 1
            else:
                x3 = x3


#			x1=mv.EnemyDownsideCheck(x1,y1,Matrix)
            # print("down-movement")
            if(x3 != w):
        #		print("loop breaked")
                break
        elif(flag == 4):
            if((2 * x3) == ix and (4 * y3 - 4) == iy):
                ix = 2
                iy = 4
                lives = lives - 1
                Matrix[2 * x3][4 * y3 - 4] = "["
                Matrix[2 * x3][4 * y3 - 3] = "^"
                Matrix[2 * x3][4 * y3 - 2] = "^"
                Matrix[2 * x3][4 * y3 - 1] = "]"
                Matrix[2 * x3 + 1][4 * y3 - 4] = "_"
                Matrix[2 * x3 + 1][4 * y3 - 3] = "]"
                Matrix[2 * x3 + 1][4 * y3 - 2] = "["
                Matrix[2 * x3 + 1][4 * y3 - 1] = "_"
                Matrix[2 * x3][2 * y3] = " "
                Matrix[2 * x3][2 * y3 + 1] = " "
                Matrix[2 * x3][2 * y3 + 2] = " "
                Matrix[2 * x3][2 * y3 + 3] = " "
                Matrix[2 * x3 + 1][2 * y3] = " "
                Matrix[2 * x3 + 1][2 * y3 + 1] = " "
                Matrix[2 * x3 + 1][2 * y3 + 2] = " "
                Matrix[2 * x3 + 1][2 * y3 + 3] = " "

                y3 = y3 - 1
            else:
                y3 = y3

            if(Matrix[2 * x3][4 * y3 - 4] == " "):
                Matrix[2 * x3][4 * y3 - 4] = "["
                Matrix[2 * x3][4 * y3 - 3] = "^"
                Matrix[2 * x3][4 * y3 - 2] = "^"
                Matrix[2 * x3][4 * y3 - 1] = "]"
                Matrix[2 * x3 + 1][4 * y3 - 4] = "_"
                Matrix[2 * x3 + 1][4 * y3 - 3] = "]"
                Matrix[2 * x3 + 1][4 * y3 - 2] = "["
                Matrix[2 * x3 + 1][4 * y3 - 1] = "_"

                Matrix[2 * x3][2 * y3] = " "
                Matrix[2 * x3][2 * y3 + 1] = " "
                Matrix[2 * x3][2 * y3 + 2] = " "
                Matrix[2 * x3][2 * y3 + 3] = " "
                Matrix[2 * x3 + 1][2 * y3] = " "
                Matrix[2 * x3 + 1][2 * y3 + 1] = " "
                Matrix[2 * x3 + 1][2 * y3 + 2] = " "
                Matrix[2 * x3 + 1][2 * y3 + 3] = " "

                y3 = y3 - 1
            else:
                y3 = y3

#			y1=mv.EnemyLeftsideCheck(x1/2,y1/2,Matrix)
    #		print("left-movement")
            if(y3 != z):
#				print("loop breaked")
                break


#		print(x1,y1,"after comming from looop")
#		print(x1,y1,"before sending to gp")
#		g.printboard(42,84,Matrix,ix,iy,x1,x2,x3,y1,y2,y3)
'''	flag = 0
	while (1):
		flag = randint(1,4)
		w = 2*x2
		z = 4*y2
		if(flag==1):
			x2=mv.EnemyUpsideCheck(2*x2,4*y2,Matrix)
			if( x2 != w):
				break
		elif(flag==2):
			y1=mv.EnemyRightsideCheck(2*x2,4*y2,Matrix)
			if( y2 != z):
				break
		elif(flag==3):
			x2=mv.EnemyDownsideCheck(2*x2,4*y2,Matrix)
			if( x2 != w):
				break
		elif(flag==4):
			y2=mv.EnemyLeftsideCheck(2*x2,4*y2,Matrix)
			if( y2 != z):
				break

	flag = 0
	while (1):
		flag = randint(1,4)
		w = 2*x3
		z = 4*y3
		if(flag==1):
			x3=mv.EnemyUpsideCheck(2*x3,4*y3,Matrix)
			if( x3 != w):
				break
		elif(flag==2):
			y3=mv.EnemyRightsideCheck(2*x3,4*y3,Matrix)
			if( y3 != z):
				break
		elif(flag==3):
			x3=mv.EnemyDownsideCheck(2*x3,4*y3,Matrix)
			if( x3 != w):
				break
		elif(flag==4):
			y3=mv.EnemyLeftsideCheck(x3,y3,Matrix)
			if( y3 != z):
				break
'''
