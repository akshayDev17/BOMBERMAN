from parent_class import general
from board_setup import Replace
from time import sleep


class Bomb(general):
    def __init__(self, X, Y, lst):
        general.__init__(self, X, Y, lst)
        self.enabled = 1

    def deploy(self, board):
        self.enabled = 0
        x1 = self.x
        y1 = self.y
        Xi = [x1, x1 + 1, x1 + 2, x1 + 3]
        Yi = [y1, y1 + 1]
        X1l = [x1 - 1, x1 - 2, x1 - 3, x1 - 4]
        X1r = [x1 + 4, x1 + 5, x1 + 6, x1 + 7]
        Y1a = [y1 - 1, y1 - 2]
        Y1b = [y1 + 2, y1 + 3]
        set_flag = 0
        for i in Y1a:
            if board[i][x1] == 'X':
                set_flag = 1
                break
        if set_flag == 0:
            y1a = y1 - 2
        else:
            y1a = i + 1
        set_flag = 0
        for i in Y1b:
            if board[i][x1] == 'X':
                set_flag = 1
                break
        if set_flag == 0:
            y1b = y1 + 3
        else:
            y1b = i - 1
        set_flag = 0
        for i in X1l:
            if board[y1][i] == 'X':
                set_flag = 1
                break
        if set_flag == 0:
            x1l = x1 - 4
        else:
            x1l = i + 1
        set_flag = 0
        for i in X1r:
            if board[y1][i] == 'X':
                set_flag = 1
                break
        if set_flag == 0:
            x1r = x1 + 7
        else:
            x1r = i - 1
        return [x1l, y1a, x1r, y1b]

    def explode(self, board, loc,xbm,ybm):
        r = []
        x1 = self.x
        X1 = [x1, x1 + 1, x1 + 2, x1 + 3]
        y1 = self.y
        Y1 = [y1, y1 + 1]
        for i in range(loc[0], loc[2] + 1):
            r.append(i)
        c, nY = [], []
        for i in range(loc[1], loc[3] + 1):
            c.append(i)
            nY.append('^' * 4)
        this_round, life_gone = 0, 0
        if board[y1][loc[0]] == '/':
            this_round += 20
        if board[y1][loc[2] - 3] == '/':
            this_round += 20
        if board[loc[1]][x1] == '/':
            this_round += 20
        if board[loc[3] - 1][x1] == '/':
            this_round += 20
        if board[y1][loc[0]] == 'E':
            this_round += 100
        if board[y1][loc[2] - 3] == 'E':
            this_round += 100
        if board[loc[1]][x1] == 'E':
            this_round += 100
        if board[loc[3] - 1][x1] == 'E':
            this_round += 100
        if board[y1][loc[0]] == 'B' or board[y1][loc[2] - 3] == 'B' or board[loc[1]][x1] == 'B' or board[loc[3] - 1][x1] == 'B' or (x1 == xbm and y1 == ybm):
            this_round = 0
            life_gone = 1
        board = Replace(r, Y1, ['^' * (loc[2] - loc[0] + 1), '^' * (loc[2] - loc[0] + 1)], board)
        board = Replace(X1, c, nY, board)
        return [this_round, life_gone, board]

    def clearbomb(self, board, loc):
        r = []
        x1 = self.x
        X1 = [x1, x1 + 1, x1 + 2, x1 + 3]
        y1 = self.y
        Y1 = [y1, y1 + 1]
        for i in range(loc[0], loc[2] + 1):
            r.append(i)
        c, nY = [], []
        for i in range(loc[1], loc[3] + 1):
            c.append(i)
            nY.append(' ' * 4)
        board = Replace(r, Y1, [' ' * (loc[2] - loc[0] + 1), ' ' * (loc[2] - loc[0] + 1)], board)
        board = Replace(X1, c, nY, board)
        return board
