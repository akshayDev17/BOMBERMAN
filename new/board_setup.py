"""no imports, yay!!!"""
# create_board gives us a new board having inside walls(2*4) and wall-boundary
def create_board():
    """as the name suggests, gives us a new board"""
    board = []
    i, string, string2 = 0, "X" * 4 + " " * 76 + "X" * 4, ""
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
                board.append(string)
        i = i + 1
    return board


#Replace takes the column list and row list(both are index lists) ,
#the list of strings to be added onto the board,and gives us
#a new board where the list 'ls' has been added '''


def replace(cols, rows, my_list, board):
    """Replace a tile in the board with some other tile"""
    row_pointer, column_pointer = 0, 0
    for i in rows:
        new = list(board[i])
        column_pointer = 0
        for j in cols:
            new[j] = my_list[row_pointer][column_pointer]
            column_pointer += 1
        row_pointer += 1
        board[i] = ''.join(new)
    return board
NBOARD = create_board()
