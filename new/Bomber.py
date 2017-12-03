"""import docstring"""
import sys
import os
import signal
import time
from random import randint
from player import Bomberman
from board_setup import replace
import getchar
from BOMB import Bomb
from addbricks import addbricks, NBOARD
from enemy import addenemy

GETCH = getchar.Getch()


class AlarmException(Exception):
    """class docstring"""
    pass

# place the Bomberman
B = Bomberman(4, 2, ['B' * 4, 'B' * 4])
NBOARD = replace([4, 5, 6, 7], [2, 3], B.getlist(), NBOARD)
SCORE, LIFES = 0, 5
# add enemies
L = addenemy(NBOARD)
NBOARD = L[0]
FIRST = L[1]
DEATH_1 = True
L = addenemy(NBOARD)
NBOARD = L[0]
SECOND = L[1]
DEATH_2 = True
L = addenemy(NBOARD)
NBOARD = L[0]
THIRD = L[1]
DEATH_3 = True
# for colour printing
NEW_LIST = []

def new_print(string):
    """method docstring"""
    new_list = list(string)
    for i in range(len(new_list)):
        if new_list[i] == 'X':
            new_list[i] = "\033[1;30;48mX" + "\033[0m"
        if new_list[i] == '/':
            new_list[i] = "\033[0;37;43m/" + "\033[0m"
        if new_list[i] == 'B':
            new_list[i] = "\033[1;34;48mB" + "\033[0m"
        if new_list[i] == 'E':
            new_list[i] = "\033[1;31;48mE" + "\033[0m"
        if new_list[i] == '[' or new_list[i] == 'O' or new_list[i] == ']':
            new_list[i] = "\033[1;35;48m" + new_list[i] + "\033[0m"
        if new_list[i] == '^':
            new_list[i] = "\033[0;37;41m" + new_list[i] + "\033[0m"
    string = ''.join(new_list)
    print string


def printboard(board, score, lives):
    """method docstring"""
    os.system('tput reset')
    for i in range(len(board)):
        new_print(board[i])
    print "\n\033[0;32;48m%s%d\033[0m" % ("your score is: ", score)
    if lives < 3:
        print "\n\033[1;31;48m%s%d\033[0m" % ("Lifes Remaining: ", lives)
    else:
        print "\n\033[0;32;48m%s%d\033[0m" % ("Lifes Remaining: ", lives)


printboard(NBOARD, SCORE, LIFES)
# reinitialize the board


def clearboard():
    """method docstring"""
    board = []
    i, string1, string2 = 0, "X" * 4 + " " * 76 + "X" * 4, ""
    while i < 84:
        if i % 8 == 0:
            string2 = string2 + "X" * 4
        else:
            string2 = string2 + " " * 4
        i = i + 4
    i = 0
    while i < 42:
        if i < 2 or i > 39:
            board.append("X" * 84)
        else:
            if i % 4 == 0 or (i - 1) % 4 == 0:
                board.append(string2)
            else:
                board.append(string1)
        i = i + 1
    board = addbricks(board)
    return board

def print_score(score_list):
    """prints score of current round"""
    i = 0
    for i in range(len(score_list)):
        print "\n\033[0;32;48m%s%d\033[0m" % ("Round "+str(i)+" score is: ", score_list[i])

def alarmhandler(signum, frame):
    """method docstring"""
    raise AlarmException


def input_to(timeout=1):
    """method docstring"""
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.alarm(timeout)
    try:
        text = GETCH()
        signal.alarm(0)
        return text
    except AlarmException:
        print "\n Prompt timeout, Continuing......"
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


DEPLOYED, SL, BO = 1, [], Bomb(4, 2, ['O'*4, 'O'*4])  # checks whether bomb is on the board
CHECK, COUNT = 0, 4  # COUNT for timer of bomb
while CHECK == 0:
    # enemy colliding with Bomberman
    if ((B.getx() == FIRST.getx() and B.gety() == FIRST.gety() and
         NBOARD[FIRST.gety()][FIRST.getx()] == 'E') or
            (B.getx() == SECOND.getx() and B.gety() == SECOND.gety() and
             NBOARD[SECOND.gety()][SECOND.getx()] == 'E') or
            (B.getx() == THIRD.getx() and B.gety() == THIRD.gety() and
             NBOARD[THIRD.gety()][THIRD.getx()] == 'E')):
        SL.append(SCORE)
        SCORE = 0
        LIFES -= 1
        NBOARD = clearboard()
        B = Bomberman(4, 4, ['B' * 4, 'B' * 4])
        NBOARD = replace([4, 5, 6, 7], [4, 5], B.getlist(), NBOARD)
        L = addenemy(NBOARD)
        NBOARD = L[0]
        FIRST = L[1]
        DEATH_1 = True
        L = addenemy(NBOARD)
        NBOARD = L[0]
        SECOND = L[1]
        DEATH_2 = True
        L = addenemy(NBOARD)
        NBOARD = L[0]
        THIRD = L[1]
        DEATH_3 = True
        printboard(NBOARD, SCORE, LIFES)
    # after the bomb has exploded
    if COUNT == -1:
        NBOARD = BO.clearbomb(NBOARD, NEW_LIST)
        printboard(NBOARD, SCORE, LIFES)
        DEPLOYED = 1
        COUNT = 4
    # after deploying the bomb
    if DEPLOYED == 0:
        if COUNT > 0:
            COUNT -= 1
            printboard(NBOARD, SCORE, LIFES)
        elif COUNT == 0:
            RESULT = BO.explode(NBOARD, NEW_LIST, B.getx(), B.gety())
            if FIRST.checkdeath(NBOARD):
                DEATH_1 = False
            if SECOND.checkdeath(NBOARD):
                DEATH_2 = False
            if THIRD.checkdeath(NBOARD):
                DEATH_3 = False
            if RESULT[1] == 0:
                SCORE += RESULT[0]
                NBOARD = RESULT[2]
                printboard(NBOARD, SCORE, LIFES)
                COUNT -= 1
            elif RESULT[1] != 0:
                # if Bomberman gets caught in the explosion
                SL.append(SCORE)
                SCORE = 0
                LIFES -= 1
                NBOARD = RESULT[2]
                printboard(NBOARD, SCORE, LIFES)
                time.sleep(0.5)
                NBOARD = BO.clearbomb(NBOARD, NEW_LIST)
                printboard(NBOARD, SCORE, LIFES)
                NBOARD = clearboard()
                B = Bomberman(4, 4, ['B' * 4, 'B' * 4])
                NBOARD = replace([4, 5, 6, 7], [4, 5], B.getlist(), NBOARD)
                L = addenemy(NBOARD)
                NBOARD = L[0]
                FIRST = L[1]
                L = addenemy(NBOARD)
                NBOARD = L[0]
                SECOND = L[1]
                DEATH_2 = True
                L = addenemy(NBOARD)
                NBOARD = L[0]
                THIRD = L[1]
                DEATH_3 = True
                DEPLOYED = 1
                COUNT = 4
                printboard(NBOARD, SCORE, LIFES)

    O = input_to()
    if O == 'q' or LIFES == 0:
        CHECK = 1  # end the infinite loop
        SL.append(SCORE)
        print "GAME OVER "
        print_score(SL)
        sys.exit(0)
    elif O == 'w':
        NBOARD = B.goup(NBOARD)
        printboard(NBOARD, SCORE, LIFES)
    elif O == 'a':
        NBOARD = B.goleft(NBOARD)
        printboard(NBOARD, SCORE, LIFES)
    elif O == 's':
        NBOARD = B.godown(NBOARD)
        printboard(NBOARD, SCORE, LIFES)
    elif O == 'd':
        NBOARD = B.goright(NBOARD)
        printboard(NBOARD, SCORE, LIFES)
    elif O == 'b':
        if DEPLOYED == 1:
            BO = Bomb(
                B.getx(), B.gety(), [
                    '[' + 'O' * 2 + ']', '[' + 'O' * 2 + ']'])
            X = BO.getx()
            Y = BO.gety()
            X1 = [X + j for j in range(4)]
            Y1 = [Y, Y + 1]
            NBOARD = replace(X1, Y1, BO.getlist(), NBOARD)
            NEW_LIST = BO.deploy(NBOARD)
            printboard(NBOARD, SCORE, LIFES)
            DEPLOYED = 0
    if DEATH_1:
        ML = []
        if FIRST.checkleft(NBOARD):
            ML.append(1)
        if FIRST.checkright(NBOARD):
            ML.append(3)
        if FIRST.checkup(NBOARD):
            ML.append(2)
        if FIRST.checkdown(NBOARD):
            ML.append(4)
        if len(ML):
            C = randint(0, len(ML) - 1)
            OPTION = ML[C]
            if OPTION == 1:
                NBOARD = FIRST.moveleft(NBOARD)
            if OPTION == 2:
                NBOARD = FIRST.moveup(NBOARD)
            if OPTION == 3:
                NBOARD = FIRST.moveright(NBOARD)
            if OPTION == 4:
                NBOARD = FIRST.movedown(NBOARD)
    if DEATH_2:
        ML = []
        if SECOND.checkleft(NBOARD):
            ML.append(1)
        if SECOND.checkright(NBOARD):
            ML.append(3)
        if SECOND.checkup(NBOARD):
            ML.append(2)
        if SECOND.checkdown(NBOARD):
            ML.append(4)
        if len(ML):
            C = randint(0, len(ML) - 1)
            OPTION = ML[C]
            if OPTION == 1:
                NBOARD = SECOND.moveleft(NBOARD)
            if OPTION == 2:
                NBOARD = SECOND.moveup(NBOARD)
            if OPTION == 3:
                NBOARD = SECOND.moveright(NBOARD)
            if OPTION == 4:
                NBOARD = SECOND.movedown(NBOARD)
    if DEATH_3:
        ML = []
        if THIRD.checkleft(NBOARD):
            ML.append(1)
        if THIRD.checkright(NBOARD):
            ML.append(3)
        if THIRD.checkup(NBOARD):
            ML.append(2)
        if THIRD.checkdown(NBOARD):
            ML.append(4)
        if len(ML):
            C = randint(0, len(ML) - 1)
            OPTION = ML[C]
            if OPTION == 1:
                NBOARD = THIRD.moveleft(NBOARD)
            if OPTION == 2:
                NBOARD = THIRD.moveup(NBOARD)
            if OPTION == 3:
                NBOARD = THIRD.moveright(NBOARD)
            if OPTION == 4:
                NBOARD = THIRD.movedown(NBOARD)
