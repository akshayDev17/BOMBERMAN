from player import bomberman
from board_setup import Replace
from time import *
import sys
import signal
import getchar
from BOMB import Bomb
import os
from addbricks import addbricks, nboard
from enemy import Enemy, addenemy
from random import randint

getch = getchar.Getch()


class AlarmException(Exception):
    pass

# place the bomberman
B = bomberman(4, 2, ['B' * 4, 'B' * 4])
nboard = Replace([4, 5, 6, 7], [2, 3], B.getlist(), nboard)
Score, lifes = 0, 5
# add enemies
l = addenemy(nboard)
nboard = l[0]
e1 = l[1]
d1 = True
l = addenemy(nboard)
nboard = l[0]
e2 = l[1]
d2 = True
l = addenemy(nboard)
nboard = l[0]
e3 = l[1]
d3 = True
# for colour printing


def Print(s):
    l = list(s)
    for i in range(len(l)):
        if l[i] == 'X':
            l[i] = "\033[1;30;48mX" + "\033[0m"
        if l[i] == '/':
            l[i] = "\033[0;37;43m/" + "\033[0m"
        if l[i] == 'B':
            l[i] = "\033[1;34;48mB" + "\033[0m"
        if l[i] == 'E':
            l[i] = "\033[1;31;48mE" + "\033[0m"
        if l[i] == '[' or l[i] == 'O' or l[i] == ']':
            l[i] = "\033[1;35;48m" + l[i] + "\033[0m"
        if l[i] == '^':
            l[i] = "\033[0;37;41m" + l[i] + "\033[0m"
    s = ''.join(l)
    print s


def printboard(board, score, lives):
    os.system('tput reset')
    for i in range(len(board)):
        Print(board[i])
    print "\n\033[0;32;48m%s%d\033[0m" % ("your score is: ", score)
    if lives < 3:
        print "\n\033[1;31;48m%s%d\033[0m" % ("Lifes Remaining: ", lives)
    else:
        print "\n\033[0;32;48m%s%d\033[0m" % ("Lifes Remaining: ", lives)


printboard(nboard, Score, lifes)
# reinitialize the board


def clearboard():
    board = []
    i, s1, s2 = 0, "X" * 4 + " " * 76 + "X" * 4, ""
    while i < 84:
        if i % 8 == 0:
            s2 = s2 + "X" * 4
        else:
            s2 = s2 + " " * 4
        i = i + 4
    i = 0
    while(i < 42):
        if i < 2 or i > 39:
            board.append("X" * 84)
        else:
            if i % 4 == 0 or (i - 1) % 4 == 0:
                board.append(s2)
            else:
                board.append(s1)
        i = i + 1
    board = addbricks(board)
    return board


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
        print "\n Prompt timeout, Continuing......"
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


deployed, sl = 1, []  # checks whether bomb is on the board
check, count = 0, 4  # count for timer of bomb
while check == 0:
    # enemy colliding with bomberman
    if ((B.getx() == e1.getx() and B.gety() == e1.gety() and
         nboard[e1.gety()][e1.getx()] == 'E') or
        (B.getx() == e2.getx() and B.gety() == e2.gety() and
         nboard[e2.gety()][e2.getx()] == 'E') or
        (B.getx() == e3.getx() and B.gety() == e3.gety() and
         nboard[e3.gety()][e3.getx()] == 'E')):
        Score = 0
        lifes -= 1
        nboard = clearboard()
        B = bomberman(4, 4, ['B' * 4, 'B' * 4])
        nboard = Replace([4, 5, 6, 7], [4, 5], B.getlist(), nboard)
        l = addenemy(nboard)
        nboard = l[0]
        e1 = l[1]
        d1 = True
        l = addenemy(nboard)
        nboard = l[0]
        e2 = l[1]
        d2 = True
        l = addenemy(nboard)
        nboard = l[0]
        e3 = l[1]
        d3 = True
        printboard(nboard, Score, lifes)
    # after the bomb has exploded
    if count == -1:
        nboard = bo.clearbomb(nboard, newl)
        printboard(nboard, Score, lifes)
        deployed = 1
        count = 4
    # after deploying the bomb
    if deployed == 0:
        if count > 0:
            count -= 1
            printboard(nboard, Score, lifes)
        elif count == 0:
            result = bo.explode(nboard, newl, B.getx(), B.gety())
            if e1.checkDeath(nboard):
                d1 = False
            if e2.checkDeath(nboard):
                d2 = False
            if e3.checkDeath(nboard):
                d3 = False
            if result[1] == 0:
                Score += result[0]
                nboard = result[2]
                printboard(nboard, Score, lifes)
                count -= 1
            else:
                # if bomberman gets caught in the explosion
                sl.append(Score)
                Score = 0
                lifes -= 1
                nboard = result[2]
                printboard(nboard, Score, lifes)
                nboard = clearboard()
                B = bomberman(4, 4, ['B' * 4, 'B' * 4])
                nboard = Replace([4, 5, 6, 7], [4, 5], B.getlist(), nboard)
                l = addenemy(nboard)
                nboard = l[0]
                e1 = l[1]
                l = addenemy(nboard)
                nboard = l[0]
                e2 = l[1]
                d2 = True
                l = addenemy(nboard)
                nboard = l[0]
                e3 = l[1]
                d3 = True
                printboard(nboard, Score, lifes)
    o = input_to()
    if o == 'q' or lifes == 0:
        check = 1  # end the infinite loop
        print "GAME OVER "
        print sl
        sys.exit(0)
    elif o == 'w':
        nboard = B.goup(nboard)
        printboard(nboard, Score, lifes)
    elif o == 'a':
        nboard = B.goleft(nboard)
        printboard(nboard, Score, lifes)
    elif o == 's':
        nboard = B.godown(nboard)
        printboard(nboard, Score, lifes)
    elif o == 'd':
        nboard = B.goright(nboard)
        printboard(nboard, Score, lifes)
    elif o == 'b':
        if deployed == 1:
            bo = Bomb(
                B.getx(), B.gety(), [
                    '[' + 'O' * 2 + ']', '[' + 'O' * 2 + ']'])
            x1 = bo.getx()
            y1 = bo.gety()
            X1 = [x1 + i for i in range(4)]
            Y1 = [y1, y1 + 1]
            nboard = Replace(X1, Y1, bo.getlist(), nboard)
            newl = bo.deploy(nboard)
            printboard(nboard, Score, lifes)
            deployed = 0
    if d1:
        ml = []
        if e1.checkLeft(nboard):
            ml.append(1)
        if e1.checkRight(nboard):
            ml.append(3)
        if e1.checkUp(nboard):
            ml.append(2)
        if e1.checkDown(nboard):
            ml.append(4)
        if len(ml):
            c = randint(0, len(ml) - 1)
            option = ml[c]
            if option == 1:
                nboard = e1.moveleft(nboard)
            if option == 2:
                nboard = e1.moveup(nboard)
            if option == 3:
                nboard = e1.moveright(nboard)
            if option == 4:
                nboard = e1.movedown(nboard)
    if d2:
        ml = []
        if e2.checkLeft(nboard):
            ml.append(1)
        if e2.checkRight(nboard):
            ml.append(3)
        if e2.checkUp(nboard):
            ml.append(2)
        if e2.checkDown(nboard):
            ml.append(4)
        if len(ml):
            c = randint(0, len(ml) - 1)
            option = ml[c]
            if option == 1:
                nboard = e2.moveleft(nboard)
            if option == 2:
                nboard = e2.moveup(nboard)
            if option == 3:
                nboard = e2.moveright(nboard)
            if option == 4:
                nboard = e2.movedown(nboard)
    if d3:
        ml = []
        if e3.checkLeft(nboard):
            ml.append(1)
        if e3.checkRight(nboard):
            ml.append(3)
        if e3.checkUp(nboard):
            ml.append(2)
        if e3.checkDown(nboard):
            ml.append(4)
        if len(ml):
            c = randint(0, len(ml) - 1)
            option = ml[c]
            if option == 1:
                nboard = e3.moveleft(nboard)
            if option == 2:
                nboard = e3.moveup(nboard)
            if option == 3:
                nboard = e3.moveright(nboard)
            if option == 4:
                nboard = e3.movedown(nboard)
