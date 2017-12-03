from parent_class import general
from board_setup import Replace
from random import randint


# enemy class inherits from general class
class Enemy(general):
    def __init__(self, X, Y, lst):
        general.__init__(self, X, Y, lst)
        self.alive = True

    # checks if the enemy has died due to bomb explosion
    def checkDeath(self, board):
        x1 = self.x
        y1 = self.y
        if board[y1][x1] == ' ':
            return True
        else:
            return False

    # checks if the enemy can move right
    def checkRight(self, board):
        x1 = self.x + 4
        y1 = self.y
        if (board[y1][x1] != '/' and board[y1][x1] != 'X' and
                x1 < 80 and board[y1][x1] != '[' and board[y1][x1] != 'E'):
            return True
        else:
            return False

    # checks if the enemy can move left
    def checkLeft(self, board):
        x1 = self.x - 4
        y1 = self.y
        if (board[y1][x1] != '/' and
                board[y1][x1] != 'X'and x1 > 0 and board[y1][x1] != '[' and
                board[y1][x1] != 'E'):
            return True
        else:
            return False

    # checks if the enemy can move up
    def checkUp(self, board):
        x1 = self.x
        y1 = self.y - 2
        if (board[y1][x1] != '/' and board[y1][x1] != 'X'and y1 > 0 and
                board[y1][x1] != '[' and board[y1][x1] != 'E'):
            return True
        else:
            return False

    # checks if the enemy can move down
    def checkDown(self, board):
        x1 = self.x
        y1 = self.y + 2
        if (board[y1][x1] != '/' and board[y1][x1] != 'X'and y1 < 42 and
                board[y1][x1] != '[' and board[y1][x1] != 'E'):
            return True
        else:
            return False

    # makes the enemy moves right and returns the new configuration of board
    def moveright(self, board):
        x1 = self.x
        y1 = self.y
        X1 = [x1 + 4, x1 + 5, x1 + 6, x1 + 7]
        Y1 = [y1, y1 + 1]
        board = Replace(X1, Y1, ['E' * 4, 'E' * 4], board)
        X1 = [x1, x1 + 1, x1 + 2, x1 + 3]
        board = Replace(X1, Y1, [' ' * 4, ' ' * 4], board)
        self.x = x1 + 4
        return board

    # makes the enemy moves left and returns the new configuration of board
    def moveleft(self, board):
        x1 = self.x
        y1 = self.y
        X1 = [x1 - 4, x1 - 3, x1 - 2, x1 - 1]
        Y1 = [y1, y1 + 1]
        board = Replace(X1, Y1, ['E' * 4, 'E' * 4], board)
        X1 = [x1, x1 + 1, x1 + 2, x1 + 3]
        board = Replace(X1, Y1, [' ' * 4, ' ' * 4], board)
        self.x = x1 - 4
        return board

    # makes the enemy moves up and returns the new configuration of board
    def moveup(self, board):
        x1 = self.x
        y1 = self.y
        X1 = [x1, x1 + 1, x1 + 2, x1 + 3]
        Y1 = [y1 - 2, y1 - 1]
        board = Replace(X1, Y1, ['E' * 4, 'E' * 4], board)
        Y1 = [y1, y1 + 1]
        board = Replace(X1, Y1, [' ' * 4, ' ' * 4], board)
        self.y = y1 - 2
        return board

    # makes the enemy moves down and returns the new configuration of board
    def movedown(self, board):
        x1 = self.x
        y1 = self.y
        X1 = [x1, x1 + 1, x1 + 2, x1 + 3]
        Y1 = [y1 + 2, y1 + 3]
        board = Replace(X1, Y1, ['E' * 4, 'E' * 4], board)
        Y1 = [y1, y1 + 1]
        board = Replace(X1, Y1, [' ' * 4, ' ' * 4], board)
        self.y = y1 + 2
        return board

''' adds an enemy to the board,returning the board's new configuration and the
enemy created '''


def addenemy(board):
    count = 0
    while count < 1:
        x1 = randint(1, 19) * 4
        y1 = randint(1, 19) * 2
        X = [x1, x1 + 1, x1 + 2, x1 + 3]
        Y = [y1, y1 + 1]
        flag = 0
        for i in X:
            for j in Y:
                if board[j][i] != ' ':
                    flag = 1
                    break
        if flag == 0:
            E = Enemy(x1, y1, ['E' * 4, 'E' * 4])
            board = Replace(X, Y, ['E' * 4, 'E' * 4], board)
            count += 1
        else:
            continue
    return [board, E]
