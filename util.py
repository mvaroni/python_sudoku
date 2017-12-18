#!/usr/bin/env python
# Four spaces as indentation [no tabs]

# ------------------------------------------
# Find collision
# ------------------------------------------

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_collision(board, peers, cell, number):

    # -Dictionary with peers:
    # List of every cell that is assigned in a unit with this cell, except itself.
    # Example: I6 = [A6, B6, C6, D6, E6, F6, G6, H6, I1, I2, I3, I4, I5, I7, I8, I9, G4, G5, H4, H5]
    # Code: self.peers = collections.OrderedDict((s, set(sum(self.units[s],[]))-set([s])) for s in self.squares)

    #Check if a dict of peers have collision of numbers
    #for n in numbers:
    for p in list(peers[cell]):
        if board[p] == number:
            return True

    return False


# ------------------------------------------
# Find empty cells
# ------------------------------------------

def find_empty_cells(board, squares):

    return [ept_cl for ept_cl in squares if board[ept_cl] is 0]


# ------------------------------------------
# Find empty neighbors
# ------------------------------------------

def find_empty_peers(board, peers, cell):

    empty_peers = []

    #return [p for p in peers if peers[cell] is 0]
    for p in list(peers[cell]):
        if board[p] == 0:
            empty_peers.append(board[p])

    return empty_peers

# ------------------------------------------
# Format the print_board function output
# ------------------------------------------

def __format__(self, format):

    if (format == '0'):
        return '.'


# ------------------------------------------
# Print board
# ------------------------------------------

def print_board(board):

    # .format() -> format string using the board cells
    # .replace() -> format string changing '0' into '.' 

    print """
    1 2 3   4 5 6   7 8 9
    ---------------------
 A| {b[A1]} {b[A2]} {b[A3]} | {b[A4]} {b[A5]} {b[A6]} | {b[A7]} {b[A8]} {b[A9]} |
 B| {b[B1]} {b[B2]} {b[B3]} | {b[B4]} {b[B5]} {b[B6]} | {b[B7]} {b[B8]} {b[B9]} |
 C| {b[C1]} {b[C2]} {b[C3]} | {b[C4]} {b[C5]} {b[C6]} | {b[C7]} {b[C8]} {b[C9]} |
  | ------+-------+------ |
 D| {b[D1]} {b[D2]} {b[D3]} | {b[D4]} {b[D5]} {b[D6]} | {b[D7]} {b[D8]} {b[D9]} |
 E| {b[E1]} {b[E2]} {b[E3]} | {b[E4]} {b[E5]} {b[E6]} | {b[E7]} {b[E8]} {b[E9]} |
 F| {b[F1]} {b[F2]} {b[F3]} | {b[F4]} {b[F5]} {b[F6]} | {b[F7]} {b[F8]} {b[F9]} |
  | ------+-------+------ |
 G| {b[G1]} {b[G2]} {b[G3]} | {b[G4]} {b[G5]} {b[G6]} | {b[G7]} {b[G8]} {b[G9]} |
 H| {b[H1]} {b[H2]} {b[H3]} | {b[H4]} {b[H5]} {b[H6]} | {b[H7]} {b[H8]} {b[H9]} |
 I| {b[I1]} {b[I2]} {b[I3]} | {b[I4]} {b[I5]} {b[I6]} | {b[I7]} {b[I8]} {b[I9]} |
    ---------------------
""".format(b=board).replace('0', '.')