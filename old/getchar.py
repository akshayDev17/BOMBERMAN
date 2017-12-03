from __future__ import print_function
import signal
import sys

# simulate a getchar() for python


class Getch:
    def __init__(self):
        import tty

    def __call__(self):
        import sys
        import tty
        import termios
        # file-descriptor
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
