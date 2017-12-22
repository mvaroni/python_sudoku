#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from util import *


# ==========================================
# Artificial Intelligence Player
# ==========================================

true_empty_cells = []

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
    # Check movement
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
    # Insert 1 in the cell
    # ------------------------------------------

    def solve(self, ept_cells):

        number = 1

        while not bool(ept_cells):

            next_move = ept_cells.pop(0)

            self.board[next_move] = number

            

            self.next_number(number)

        return 1


    # ------------------------------------------
    # Generate leafs of the previous movement, testing the next number
    # ------------------------------------------

    def next_number(self, number):
     
        true_empty_cells = ept_cells
        keep_solving = True

        #while(ept_cells != []):
        # Traded this line to check the implicit boleaness bool(keep_solving)
        while(keep_solving):

            if ept_cells:
                next_move = ept_cells.pop(0)
                print "Next move: {}".format(next_move)
                
                self.board[next_move] = number
                print "Board in {}: {}\n".format(next_move, self.board[next_move])

                while check_solving() < 0:
                    self.board[next_move]

                #print self.peers[next_move]
            else:
                keep_solving = False