#!/usr/bin/env python
# Four spaces as indentation [no tabs]

import os, sys, inspect
import threading

PATH          = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Interface
WAIT          = 1
ZOOM          = 6
TILE_WIDTH    = 16 * ZOOM
TILE_HEIGHT   = 16 * ZOOM

# ------------------------------------------
# Movements Exceptions
# ------------------------------------------

class BlockedMovementException(Exception):
    def __init__(self, board, cell):
        self.board = list(board)
        self.cell = cell
    def __str__(self):
        return "Blocked cell: {}.".format(self.cell)

class InvalidMovementException(Exception):
    def __init__(self, board, cell):
        self.board = list(board)
        self.cell = cell
    def __str__(self):
        return "Invalid cell: {}.".format(self.cell)

class NoMovementException(Exception):
    def __init__(self, board):
        self.board = list(board)
    def __str__(self):
        return "Board has no other possible movement."

class TimeoutError(Exception): pass

def timelimit(timeout):
    def internal(function):
        def internal2(*args, **kw):
            class Calculator(threading.Thread):
                def __init__(self):
                    threading.Thread.__init__(self)
                    self.result = None
                    self.error = None

                def run(self):
                    try:
                        self.result = function(*args, **kw)
                    except:
                        self.error = sys.exc_info()[0]

            c = Calculator()
            c.start()
            if timeout > 0:
                c.join(timeout)
            else:
                c.join()
            if c.isAlive():
                raise TimeoutError
            if c.error:
                raise c.error
            return c.result
        return internal2
    return internal