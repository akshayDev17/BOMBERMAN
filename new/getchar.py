"""import docstring"""
from __future__ import print_function
# simulate a getchar() for python

class Getch(object):
    """class docstring"""
    def __init__(self):
        import tty

    def __call__(self):
        import sys
        import tty
        import termios
        # file-descriptor
        file_descriptor = sys.stdin.fileno()
        old_settings = termios.tcgetattr(file_descriptor)
        try:
            tty.setraw(sys.stdin.fileno())
            new_character = sys.stdin.read(1)
        finally:
            termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)
        return new_character
