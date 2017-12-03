"""import docstring"""
from board_setup import replace
from parent_class import General


# Bomberman class inherits from General class
class Bomberman(General):
    """class docstring"""
    def __init__(self, X, Y, lst):
        General.__init__(self, X, Y, lst)

    #goright checks whether the Bomberman can move right,
    #if so updates the board with the new position
    def goright(self, board):
        """method docstring"""
        xcoordinate = self.x
        ycoordinate = self.y
        if xcoordinate < 76:
            my_var = xcoordinate
            xcoordinate += 4
            xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
            ycoordinate_list = [ycoordinate, ycoordinate + 1]
            flag = 0
            for i in xcoordinate_list:
                for j in ycoordinate_list:
                    if board[j][i] != ' ':
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                oldlist = []
                for i in range(ycoordinate, ycoordinate + 2):
                    temp = ''
                    for j in range(my_var, my_var + 4):
                        temp += board[i][j]
                    oldlist.append(temp)
                board = replace(xcoordinate_list, ycoordinate_list, self.l, board)
                if oldlist == ['[' + 'O' * 2 + ']', '[' + 'O' * 2 + ']']:
                    board = replace([i - 4 for i in xcoordinate_list],
                                    [i for i in ycoordinate_list], oldlist, board)
                else:
                    board = replace([i - 4 for i in xcoordinate_list],
                                    [i for i in ycoordinate_list], [' ' * 4, ' ' * 4], board)
                self.x = xcoordinate
                self.y = ycoordinate
        return board

    #goleft checks whether the Bomberman can move left,
    #if so updates the board with the new position
    def goleft(self, board):
        """method docstring"""
        xcoordinate = self.x
        ycoordinate = self.y
        flag = 0
        if xcoordinate > 7:
            my_var = xcoordinate
            xcoordinate -= 4
            xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
            ycoordinate_list = [ycoordinate, ycoordinate + 1]
            flag = 0
            for i in xcoordinate_list:
                for j in ycoordinate_list:
                    if board[j][i] != ' ':
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                oldlist = []
                for i in range(ycoordinate, ycoordinate + 2):
                    temp = ''
                    for j in range(my_var, my_var + 4):
                        temp += board[i][j]
                    oldlist.append(temp)
                board = replace(xcoordinate_list, ycoordinate_list, self.l, board)
                if oldlist == ['[' + 'O' * 2 + ']', '[' + 'O' * 2 + ']']:
                    board = replace([i + 4 for i in xcoordinate_list],
                                    [i for i in ycoordinate_list], oldlist, board)
                else:
                    board = replace([i + 4 for i in xcoordinate_list],
                                    [i for i in ycoordinate_list], [' ' * 4, ' ' * 4], board)
                self.x = xcoordinate
                self.y = ycoordinate
        return board

    #goup checks whether the Bomberman can move up,
    #if so updates the board with the new position
    def goup(self, board):
        """method docstring"""
        xcoordinate = self.x
        ycoordinate = self.y
        flag = 0
        if ycoordinate > 3:
            my_var = ycoordinate
            ycoordinate -= 2
            xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
            ycoordinate_list = [ycoordinate, ycoordinate + 1]
            flag = 0
            for i in xcoordinate_list:
                for j in ycoordinate_list:
                    if board[j][i] != ' ':
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                oldlist = []
                for i in range(my_var, my_var + 2):
                    temp = ''
                    for j in range(xcoordinate, xcoordinate + 4):
                        temp += board[i][j]
                    oldlist.append(temp)
                board = replace(xcoordinate_list, ycoordinate_list, self.l, board)
                if oldlist == ['[' + 'O' * 2 + ']', '[' + 'O' * 2 + ']']:
                    board = replace([i for i in xcoordinate_list],
                                    [i + 2 for i in ycoordinate_list], oldlist, board)
                else:
                    board = replace([i for i in xcoordinate_list],
                                    [i + 2 for i in ycoordinate_list],
                                    [' ' * 4, ' ' * 4], board)
                self.x = xcoordinate
                self.y = ycoordinate
        return board

    #godown checks whether the Bomberman can move down,
    #if so updates the board with the new position
    def godown(self, board):
        """method docstring"""
        xcoordinate = self.x
        ycoordinate = self.y
        flag = 0
        if ycoordinate < 37:
            my_var = ycoordinate
            ycoordinate += 2
            xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
            ycoordinate_list = [ycoordinate, ycoordinate + 1]
            flag = 0
            for i in xcoordinate_list:
                for j in ycoordinate_list:
                    if board[j][i] != ' ':
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                oldlist = []
                for i in range(my_var, my_var + 2):
                    temp = ''
                    for j in range(xcoordinate, xcoordinate + 4):
                        temp += board[i][j]
                    oldlist.append(temp)
                board = replace(xcoordinate_list, ycoordinate_list, self.l, board)
                if oldlist == ['[' + 'O' * 2 + ']', '[' + 'O' * 2 + ']']:
                    board = replace([i for i in xcoordinate_list],
                                    [i - 2 for i in ycoordinate_list], oldlist, board)
                else:
                    board = replace([i for i in xcoordinate_list],
                                    [i - 2 for i in ycoordinate_list],
                                    [' ' * 4, ' ' * 4], board)
                self.x = xcoordinate
                self.y = ycoordinate
        return board
