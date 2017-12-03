

''' the parent class from which all classes will inherit the following attributes
and methods'''
# X = x-coordinate/column number of the 2*4 list inside the gameboard
# Y = y-coordinate/row number of the 2*4 list inside the gameboard
# lst = what the object looks like on the board i.e.,list of strings


class general(object):
    def __init__(self, X, Y, lst):
        self.x = X
        self.y = Y
        self.l = lst

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getlist(self):
        return self.l

    def setx(nx):
        self.x = nx

    def sety(ny):
        self.y = ny

    def setlist(nl):
        self.l = nl
