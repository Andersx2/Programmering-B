import random

class SnakeFood:
    def __init__(self, master, canvas):
        self._master = master
        self._c = canvas
        self.rows = None
        self.cols = None
        self.randomCol = 0
        self.randomRow = 0
        self.noFood = None

    def placeFood(self):
        self.noFood = True
        self.rows = len(self.snakeBoard)
        self.cols = len(self.snakeBoard[0])

        while True:
            self.randomRow = random.randint(0, self.rows-1)
            self.randomCol = random.randint(0, self.cols-1)
            if self.snakeBoard[self.randomRow][self.randomCol] == 0:
                self.snakeBoard[self.randomRow][self.randomCol] = -1
                print(self.snakeBoard[self.randomRow][self.randomCol])
                break
