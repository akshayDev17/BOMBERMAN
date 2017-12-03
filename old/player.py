from board_setup import Replace
from parent_class import general


# bomberman class inherits from general class
class bomberman(general):
    def __init__(self, X, Y, lst):
        general.__init__(self, X, Y, lst)

    ''' goright checks whether the bomberman can move right,
    if so updates the board with the new position '''
    def goright(self, board):
        x1 = self.x
        y1 = self.y
        if x1 < 76:
            m = x1
            x1 += 4
            X1 = [x1, x1 + 1, x1 + 2, x1 + 3]
            Y1 = [y1, y1 + 1]
            flag = 0
            for i in X1:
                for j in Y1:
                    if board[j][i] != ' ':
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                oldlist = []
                for i in range(y1, y1 + 2):
                    s = ''
                    for j in range(m, m + 4):
                        s += board[i][j]
                    oldlist.append(s)
                board = Replace(X1, Y1, self.l, board)
                if oldlist == ['[' + 'O' * 2 + ']', '[' + 'O' * 2 + ']']:
                    board = Replace([i - 4 for i in X1],
                                    [i for i in Y1], oldlist, board)
                else:
                    board = Replace([i - 4 for i in X1],
                                    [i for i in Y1], [' ' * 4, ' ' * 4], board)
                self.x = x1
                self.y = y1
        return board

    ''' goleft checks whether the bomberman can move left,
    if so updates the board with the new position '''
    def goleft(self, board):
        x1 = self.x
        y1 = self.y
        flag = 0
        if x1 > 7:
            m = x1
            x1 -= 4
            X1 = [x1, x1 + 1, x1 + 2, x1 + 3]
            Y1 = [y1, y1 + 1]
            flag = 0
            for i in X1:
                for j in Y1:
                    if board[j][i] != ' ':
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                oldlist = []
                for i in range(y1, y1 + 2):
                    s = ''
                    for j in range(m, m + 4):
                        s += board[i][j]
                    oldlist.append(s)
                board = Replace(X1, Y1, self.l, board)
                if oldlist == ['[' + 'O' * 2 + ']', '[' + 'O' * 2 + ']']:
                    board = Replace([i + 4 for i in X1],
                                    [i for i in Y1], oldlist, board)
                else:
                    board = Replace([i + 4 for i in X1],
                                    [i for i in Y1], [' ' * 4, ' ' * 4], board)
                self.x = x1
                self.y = y1
        return board

    ''' goup checks whether the bomberman can move up,
    if so updates the board with the new position '''
    def goup(self, board):
        x1 = self.x
        y1 = self.y
        flag = 0
        if y1 > 3:
            m = y1
            y1 -= 2
            X1 = [x1, x1 + 1, x1 + 2, x1 + 3]
            Y1 = [y1, y1 + 1]
            flag = 0
            for i in X1:
                for j in Y1:
                    if board[j][i] != ' ':
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                oldlist = []
                for i in range(m, m + 2):
                    s = ''
                    for j in range(x1, x1 + 4):
                        s += board[i][j]
                    oldlist.append(s)
                board = Replace(X1, Y1, self.l, board)
                if oldlist == ['[' + 'O' * 2 + ']', '[' + 'O' * 2 + ']']:
                    board = Replace([i for i in X1],
                                    [i + 2 for i in Y1], oldlist, board)
                else:
                    board = Replace([i for i in X1],
                                    [i + 2 for i in Y1],
                                    [' ' * 4, ' ' * 4], board)
                self.x = x1
                self.y = y1
        return board

    ''' godown checks whether the bomberman can move down,
    if so updates the board with the new position '''
    def godown(self, board):
        x1 = self.x
        y1 = self.y
        flag = 0
        if y1 < 37:
            m = y1
            y1 += 2
            X1 = [x1, x1 + 1, x1 + 2, x1 + 3]
            Y1 = [y1, y1 + 1]
            flag = 0
            for i in X1:
                for j in Y1:
                    if board[j][i] != ' ':
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                oldlist = []
                for i in range(m, m + 2):
                    s = ''
                    for j in range(x1, x1 + 4):
                        s += board[i][j]
                    oldlist.append(s)
                board = Replace(X1, Y1, self.l, board)
                if oldlist == ['[' + 'O' * 2 + ']', '[' + 'O' * 2 + ']']:
                    board = Replace([i for i in X1],
                                    [i - 2 for i in Y1], oldlist, board)
                else:
                    board = Replace([i for i in X1],
                                    [i - 2 for i in Y1],
                                    [' ' * 4, ' ' * 4], board)
                self.x = x1
                self.y = y1
        return board
