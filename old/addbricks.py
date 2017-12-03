from board_setup import nboard, Replace
from parent_class import general
from random import randint

class Bricks(general):
    def __init__(self, X, Y, lst):
        general.__init__(self, X, Y, lst)

    def Death(self, board):
        if nboard[self.y][self.x] == ' ':
            return True


def addbricks(board):
    count = 0
    while count < 20:
        b1 = Bricks(randint(1, 19) * 4, randint(1, 19) * 2, ['/' * 4, '/' * 4])
        flag = 0
        x1 = b1.getx()
        y1 = b1.gety()
        X = [x1, x1 + 1, x1 + 2, x1 + 3]
        Y = [y1, y1 + 1]
        for i in X:
            for j in Y:
                if board[j][i] != ' ':
                    flag = 1
                    break
        if flag == 0:
            board = Replace(X, Y, b1.getlist(), board)
            count += 1
        else:
            continue
    return board

nboard = addbricks(nboard)
