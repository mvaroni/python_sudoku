#!/usr/bin/env python
# Four spaces as indentation [no tabs]

class Count_Test:

    def __init__(self):
        pass

    def cross(self, A, B):

        return [a+b for a in A for b in B]


    def printable(self):

        cols = '123456789'
        rows = 'ABCDEFGHI'
        squares = self.cross(rows, cols)
        unitlist = ([self.cross(rows, c) for c in cols] +
                    [self.cross(r, cols) for r in rows] +
                    [self.cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
        units = dict((s, [u for u in unitlist if s in u]) for s in squares)
        peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

        print units, "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
        print peers, "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
# ==========================================
# Main
# ==========================================

if __name__ == "__main__":
    test = Count_Test()
    test.printable()