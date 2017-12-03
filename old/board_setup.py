# create_board gives us a new board having inside walls(2*4) and wall-boundary
def create_board():
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
    return board


''' Replace takes the column list and row list(both are index lists) ,
 the list of strings to be added onto the board,and gives us
 a new board where the list 'ls' has been added '''


def Replace(cols, rows, ls, board):
    rp, cp = 0, 0
    for i in rows:
        new = list(board[i])
        cp = 0
        for j in cols:
            new[j] = ls[rp][cp]
            cp += 1
        rp += 1
        board[i] = ''.join(new)
    return board
nboard = create_board()
