"""imports"""
from parent_class import General
from board_setup import replace

class Bomb(General):
    """Bomb class"""
    def __init__(self, X, Y, lst):
        General.__init__(self, X, Y, lst)

    def deploy(self, board):
        """deploy"""
        xcoordinate = self.x
        ycoordinate = self.y
        xcoordinate_left_list = [xcoordinate - 1, xcoordinate - 2, xcoordinate - 3, xcoordinate - 4]
        xcoordinate_right_list = [
            xcoordinate + 4,
            xcoordinate + 5,
            xcoordinate + 6,
            xcoordinate + 7]
        ycoordinate_above_list = [ycoordinate - 1, ycoordinate - 2]
        ycoordinate_below_list = [ycoordinate + 2, ycoordinate + 3]
        set_flag = 0
        i = 0
        for i in ycoordinate_above_list:
            if board[i][xcoordinate] == 'X':
                set_flag = 1
                break
        if set_flag == 0:
            y1a = ycoordinate - 2
        else:
            y1a = i + 1
        set_flag = 0
        for i in ycoordinate_below_list:
            if board[i][xcoordinate] == 'X':
                set_flag = 1
                break
        if set_flag == 0:
            y1b = ycoordinate + 3
        else:
            y1b = i - 1
        set_flag = 0
        for i in xcoordinate_left_list:
            if board[ycoordinate][i] == 'X':
                set_flag = 1
                break
        if set_flag == 0:
            x1l = xcoordinate - 4
        else:
            x1l = i + 1
        set_flag = 0
        for i in xcoordinate_right_list:
            if board[ycoordinate][i] == 'X':
                set_flag = 1
                break
        if set_flag == 0:
            x1r = xcoordinate + 7
        else:
            x1r = i - 1
        return [x1l, y1a, x1r, y1b]

    def explode(self, board, loc, xbm, ybm):
        """after explosion"""
        row_list = []
        xcoordinate = self.x
        xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
        ycoordinate = self.y
        ycoordinate_list = [ycoordinate, ycoordinate + 1]
        for i in range(loc[0], loc[2] + 1):
            row_list.append(i)
        column_list, new_list = [], []
        for i in range(loc[1], loc[3] + 1):
            column_list.append(i)
            new_list.append('^' * 4)
        this_round, life_gone = 0, 0
        if board[ycoordinate][loc[0]] == '/':
            this_round += 20
        if board[ycoordinate][loc[2] - 3] == '/':
            this_round += 20
        if board[loc[1]][xcoordinate] == '/':
            this_round += 20
        if board[loc[3] - 1][xcoordinate] == '/':
            this_round += 20
        if board[ycoordinate][loc[0]] == 'E':
            this_round += 100
        if board[ycoordinate][loc[2] - 3] == 'E':
            this_round += 100
        if board[loc[1]][xcoordinate] == 'E':
            this_round += 100
        if board[loc[3] - 1][xcoordinate] == 'E':
            this_round += 100
        if(board[ycoordinate][loc[0]] == 'B' or
           board[ycoordinate][loc[2] - 3] == 'B' or
           board[loc[1]][xcoordinate] == 'B' or board[loc[3] - 1][xcoordinate] == 'B' or
           (xcoordinate == xbm and ycoordinate == ybm)):
            this_round = 0
            life_gone = 1
        board = replace(row_list,
                        ycoordinate_list,
                        ['^' * (loc[2] - loc[0] + 1), '^' * (loc[2] - loc[0] + 1)],
                        board)
        board = replace(xcoordinate_list, column_list, new_list, board)
        return [this_round, life_gone, board]

    def clearbomb(self, board, loc):
        """aftermath of explosion"""
        row_list = []
        xcoordinate = self.x
        xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
        ycoordinate = self.y
        ycoordinate_list = [ycoordinate, ycoordinate + 1]
        for i in range(loc[0], loc[2] + 1):
            row_list.append(i)
        column_list, new_list = [], []
        for i in range(loc[1], loc[3] + 1):
            column_list.append(i)
            new_list.append(' ' * 4)
        board = replace(row_list,
                        ycoordinate_list,
                        [' ' * (loc[2] - loc[0] + 1), ' ' * (loc[2] - loc[0] + 1)], board)
        board = replace(xcoordinate_list, column_list, new_list, board)
        return board
