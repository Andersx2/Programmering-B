import random

"""
    _snakeFood.py
    ~~~~~~~~~~
    Håndterer alt med mad at gøre
"""

class SnakeFood:
    def __init__(self, master, canvas):
        self._master = master

    def placeFood(self):
        """ Placerer mad på en tilfældig tom plads """
        self.noFood = True

        while True:
            self.randomRow = random.randint(0, self.rows-1)
            self.randomCol = random.randint(0, self.cols-1)
            if (self.randomRow <= self.rows) and (self.randomCol <= self.cols):
                if self.snakeBoard[self.randomRow][self.randomCol] == 0:
                    self.snakeBoard[self.randomRow][self.randomCol] = -1
                    break
