"""all imports used below"""
from random import randint
from board_setup import NBOARD, replace
from parent_class import General

class Bricks(General):
    """brick class representing each brick"""
    def __init__(self, X, Y, lst):
        General.__init__(self, X, Y, lst)

def addbricks(board):
    """as the name suggests,it adds 20 bricks to the board"""
    count = 0
    while count < 20:
        brick1 = Bricks(randint(1, 19) * 4, randint(1, 19) * 2, ['/' * 4, '/' * 4])
        flag = 0
        xcoordinate = brick1.getx()
        ycoordinate = brick1.gety()
        xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
        ycoordinate_list = [ycoordinate, ycoordinate + 1]
        for i in xcoordinate_list:
            for j in ycoordinate_list:
                if board[j][i] != ' ':
                    flag = 1
                    break
        if flag == 0:
            board = replace(xcoordinate_list, ycoordinate_list, brick1.getlist(), board)
            count += 1
        else:
            continue
    return board

NBOARD = addbricks(NBOARD)
