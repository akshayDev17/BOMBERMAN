""" the parent class from which all classes will inherit the following attributes
and methods"""
# X = x-coordinate/column number of the 2*4 list inside the gameboard
# Y = y-coordinate/row number of the 2*4 list inside the gameboard
# lst = what the object looks like on the board i.e.,list of strings
# pylint: disable = invalid-name

class General(object):
    """class docstring"""
    def __init__(self, X, Y, lst):
        """method docstring"""
        self.x = X
        self.y = Y
        self.l = lst

    def getx(self):
        """method docstring"""
        return self.x

    def gety(self):
        """method docstring"""
        return self.y

    def getlist(self):
        """method docstring"""
        return self.l

    def setx(self, new_xcoordinate):
        """method docstring"""
        self.x = new_xcoordinate

    def sety(self, new_ycoordinate):
        """method docstring"""
        self.y = new_ycoordinate

    def setlist(self, new_list):
        """method docstring"""
        self.l = new_list
