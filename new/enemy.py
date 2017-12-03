"""import dosctring"""
from random import randint
from parent_class import General
from board_setup import replace



# enemy class inherits from general class
class Enemy(General):
    """class docstring"""
    def __init__(self, xcoordinate_list, ycoordinate_list, lst):
        General.__init__(self, xcoordinate_list, ycoordinate_list, lst)

    # checks if the enemy has died due to bomb explosion
    def checkdeath(self, board):
        """method docstring"""
        xcoordinate = self.x
        ycoordinate = self.y
        temp = board[ycoordinate][xcoordinate]
        condition = (temp == ' ' or temp == '^')
        return bool(condition)

    # checks if the enemy can move right
    def checkright(self, board):
        """method docstring"""
        xcoordinate = self.x + 4
        ycoordinate = self.y
        condition = (board[ycoordinate][xcoordinate] != '/' and
                     board[ycoordinate][xcoordinate] != 'X' and
                     xcoordinate < 80 and board[ycoordinate][xcoordinate] != '[' and
                     board[ycoordinate][xcoordinate] != 'E')
        return bool(condition)

    # checks if the enemy can move left
    def checkleft(self, board):
        """method docstring"""
        xcoordinate = self.x - 4
        ycoordinate = self.y
        condition = (board[ycoordinate][xcoordinate] != '/' and
                     board[ycoordinate][xcoordinate] != 'X' and xcoordinate > 0 and
                     board[ycoordinate][xcoordinate] != '[' and
                     board[ycoordinate][xcoordinate] != 'E')
        return bool(condition)

    # checks if the enemy can move up
    def checkup(self, board):
        """method docstring"""
        xcoordinate = self.x
        ycoordinate = self.y - 2
        condition = (board[ycoordinate][xcoordinate] != '/' and
                     board[ycoordinate][xcoordinate] != 'X'and ycoordinate > 0 and
                     board[ycoordinate][xcoordinate] != '[' and
                     board[ycoordinate][xcoordinate] != 'E')
        return bool(condition)

    # checks if the enemy can move down
    def checkdown(self, board):
        """method docstring"""
        xcoordinate = self.x
        ycoordinate = self.y + 2
        condition = (board[ycoordinate][xcoordinate] != '/' and
                     board[ycoordinate][xcoordinate] != 'X' and ycoordinate < 42 and
                     board[ycoordinate][xcoordinate] != '[' and
                     board[ycoordinate][xcoordinate] != 'E')
        return bool(condition)

    # makes the enemy moves right and returns the new configuration of board
    def moveright(self, board):
        """method docstring"""
        xcoordinate = self.x
        ycoordinate = self.y
        xcoordinate_list = [xcoordinate + 4, xcoordinate + 5, xcoordinate + 6, xcoordinate + 7]
        ycoordinate_list = [ycoordinate, ycoordinate + 1]
        board = replace(xcoordinate_list, ycoordinate_list, ['E' * 4, 'E' * 4], board)
        xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
        board = replace(xcoordinate_list, ycoordinate_list, [' ' * 4, ' ' * 4], board)
        self.x = xcoordinate + 4
        return board

    # makes the enemy moves left and returns the new configuration of board
    def moveleft(self, board):
        """method docstring"""
        xcoordinate = self.x
        ycoordinate = self.y
        xcoordinate_list = [xcoordinate - 4, xcoordinate - 3, xcoordinate - 2, xcoordinate - 1]
        ycoordinate_list = [ycoordinate, ycoordinate + 1]
        board = replace(xcoordinate_list, ycoordinate_list, ['E' * 4, 'E' * 4], board)
        xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
        board = replace(xcoordinate_list, ycoordinate_list, [' ' * 4, ' ' * 4], board)
        self.x = xcoordinate - 4
        return board

    # makes the enemy moves up and returns the new configuration of board
    def moveup(self, board):
        """method docstring"""
        xcoordinate = self.x
        ycoordinate = self.y
        xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
        ycoordinate_list = [ycoordinate - 2, ycoordinate - 1]
        board = replace(xcoordinate_list, ycoordinate_list, ['E' * 4, 'E' * 4], board)
        ycoordinate_list = [ycoordinate, ycoordinate + 1]
        board = replace(xcoordinate_list, ycoordinate_list, [' ' * 4, ' ' * 4], board)
        self.y = ycoordinate - 2
        return board

    # makes the enemy moves down and returns the new configuration of board
    def movedown(self, board):
        """method docstring"""
        xcoordinate = self.x
        ycoordinate = self.y
        xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
        ycoordinate_list = [ycoordinate + 2, ycoordinate + 3]
        board = replace(xcoordinate_list, ycoordinate_list, ['E' * 4, 'E' * 4], board)
        ycoordinate_list = [ycoordinate, ycoordinate + 1]
        board = replace(xcoordinate_list, ycoordinate_list, [' ' * 4, ' ' * 4], board)
        self.y = ycoordinate + 2
        return board

#adds an enemy to the board,returning the board's new configuration and the
#enemy created


def addenemy(board):
    """add enemy docstring"""
    count = 0
    while count < 1:
        xcoordinate = randint(1, 19) * 4
        ycoordinate = randint(1, 19) * 2
        xcoordinate_list = [xcoordinate, xcoordinate + 1, xcoordinate + 2, xcoordinate + 3]
        ycoordinate_list = [ycoordinate, ycoordinate + 1]
        flag = 0
        for i in xcoordinate_list:
            for j in ycoordinate_list:
                if board[j][i] != ' ':
                    flag = 1
                    break
        if flag == 0:
            new_enemy = Enemy(xcoordinate, ycoordinate, ['E' * 4, 'E' * 4])
            board = replace(xcoordinate_list, ycoordinate_list, ['E' * 4, 'E' * 4], board)
            count += 1
        else:
            continue
    return [board, new_enemy]
