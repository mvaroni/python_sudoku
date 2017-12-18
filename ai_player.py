#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from util import *


# ==========================================
# Artificial Intelligence Player
# ==========================================

class AI_Player():

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, board, unitlist, peers, squares):
        self.board = board
        self.unitlist = unitlist
        self.peers = peers
        self.squares = squares


    # ------------------------------------------
    # Generate leafs of the previous movement
    # ------------------------------------------

    def next_number(self, number):

        ept_cells = find_empty_cells(self.board, self.squares)
        while(ept_cells != []):

            print "\nLista de squares vazios: ", ept_cells
            next_move = ept_cells.pop(0)
            print "Next move: {} \n".format(next_move)

            print self.peers[next_move]

    # ------------------------------------------
    # Check movement?
    # ------------------------------------------

    def check_solving(self):
        collided = find_collision(self.board) != ([], 0)
        print "COLIDIU?", collided, "FIND_COLLISION:", find_collision(self.board)
        if collided:
            return (-1)
        else:
            print "WIBIDIBOBIDI DU"
            return (1)


    # ------------------------------------------
    # Try to solve the Sudoku
    # ------------------------------------------

    def solve(self):

        return self.next_number(1)