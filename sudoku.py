#!/usr/bin/env python
# Four spaces as indentation [no tabs]

import sys
# Collections have the 'OrderedDict()' function
import collections
from common import *
from util import *
from ai_player import *

# ==========================================
# Sudoku
# ==========================================

numbers = [1,2,3,4,5,6,7,8,9
]
class Sudoku:

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, human=True):
        self.human = human
        self.generate_board()
        self.reset()

    # ------------------------------------------
    # Reset
    # ------------------------------------------

    def reset(self):

        # If board receives a number in string type it will create an error in 
        # find_collision() function, but I don't know if there will be another error with 
        # this approach (int type).
        self.new_board = [0, 0, 8, 2, 9, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 6, 0, 0, 9, 0, 0, 3, 0, 4, 0, 0, 6, 7, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1, 0, 9, 0, 0, 8, 0, 0, 9, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 3, 8, 9, 0, 0]

        for k in self.board:
            self.board[k] = self.new_board.pop(0)


    # ------------------------------------------
    # Generate rows, columns and blocks
    # ------------------------------------------

    def cross(self, A, B):

        return [a+b for a in A for b in B]


    def generate_board(self):

        digits = '123456789'
        cols = digits
        rows = 'ABCDEFGHI'

        # List of all cells:
        self.squares = self.cross(rows, cols)

        # List of units (columns, rows and blocks):
        self.unitlist = ([self.cross(rows, c) for c in cols] +
                    [self.cross(r, cols) for r in rows] +
                    [self.cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

        # -Dictionary with units
        # Conjunts where the cell is part of, counting itself.
        # Example: I6 = [[I1 - I9], [A6 - I6], [G4 - G6, H4 - H6, I4 - I6]]
        self.units = collections.OrderedDict((s, [u for u in self.unitlist if s in u]) for s in self.squares)

        # -Dictionary with peers:
        # List of every cell that is assigned in a unit with this cell, except itself.
        # Example: I6 = [A6, B6, C6, D6, E6, F6, G6, H6, I1, I2, I3, I4, I5, I7, I8, I9, G4, G5, H4, H5]
        self.peers = collections.OrderedDict((s, set(sum(self.units[s],[]))-set([s])) for s in self.squares)

        # Board with numbers played by player or given from the start
        self.board = collections.OrderedDict((s, None) for s in self.squares)


    # ------------------------------------------
    # Update
    # ------------------------------------------

    def update(self):

        # Board is an attribute, keep it safe sending a duplicate
        actual_board = self.board


        # If player is human:
        if self.human:
            print_board(actual_board)
            cell = str(raw_input("Cell name is made by letter from A to I and digit 1 to 9\n>> ")).upper()
            number = int(raw_input("Number between 1 and 9\n>> "))


            # Apply movement if there is one
            if (number != None) and (cell != None):

                # Validate number and cell
                if (1 <= number <= 9) and (cell in self.squares):

                    # Verifies if cell is clear
                    # IF retirado, para que seja possivel alterar o numero em qualquer momento
                    #if actual_board[cell] == 0:
                        actual_board[cell] = number

                        # Clear the CMD window
                        os.system('cls')

                        # Print actual board
                        print "\nPlayer chose to put number {} in cell {}.".format(number, cell)
                        #if self.debug:
                            #print_board(actual_board)

                        # Find collision
                        if find_collision(actual_board, self.peers, cell, number):
                            actual_board[cell] = 0
                            print "\nCollision found in cell {} by number played: {}.".format(cell, number)

                    # ELSE retirado, para que seja possivel alterar o numero em qualquer momento
                    #else:
                        #raise BlockedMovementException(actual_board, cell)
                else:
                    raise InvalidMovementException(actual_board, cell)
            else:
                raise NoMovementException(actual_board)


        # If player is not human, then it's the AI:
        else:
            
            ept_cells = find_empty_cells(self.board, self.squares)

            my_ai = AI_Player(actual_board, self.unitlist, self.peers, self.squares)
            my_ai.solve(ept_cells)
            
            print_board(actual_board)

            return 1

        return -1

# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="Execute sudoku.")
    parser.add_argument("--human", action="store_true", help="AI player")

    args = parser.parse_args()

    # Create game with chosen players
    game = Sudoku(human=not args.human)

    # Clear the CMD window
    os.system('cls')

    # Print welcome
    print "\nWelcome to AI-SUDOKU\n"

    while game.update() < 0:
        print "THE GAME IS NOT FINISHED"

    print "THE GAME IS FINISHED!!!"