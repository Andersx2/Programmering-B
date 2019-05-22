
from class_in_other_file._snakeFood import SnakeFood

# from class_in_other_file.main import SnakeGame


class Movement:
    def __init__(self):
        self.rows = None
        self.cols = None

    def findSnakeHead(self):
        """ Finder hovedet af slangen via den maksimale værdi """
        self.rows = len(self.snakeBoard)
        self.cols = len(self.snakeBoard[0])

        for self.row in range(self.rows-1):
            for self.col in range(self.cols-1):
                if self.snakeBoard[self.row][self.col] > self.snakeBoard[self._headRow][self._headCol]:
                    self._headRow1 = self.row
                    self._headCol1 = self.col
        return self._headRow1, self._headCol1


    def removeTail(self):
        """ Subtraherer alle tal < 0 i hele talrækken og gentegner. """
        self.rows = len(self.snakeBoard)
        self.cols = len(self.snakeBoard[0])

        for self.row in range(self.rows):
            for self.col in range(self.cols):
                if self.snakeBoard[self.row][self.col] > 0:
                    self.snakeBoard[self.row][self.col] -= 1


    def moveSnake(self, drow, dcol):
        """ Flytter Snake i en ny retning. Tager en ny tillagt row/col værdi"""
        self._newHeadRow = self._headRow + drow
        self._newHeadCol = self._headCol + dcol
        self._snakeDRow = drow
        self._snakeDCol = dcol

        if ((self._newHeadRow < 0) or (self._newHeadRow >= self.rows) or
                (self._newHeadCol < 0) or (self._newHeadCol >= self.cols)):
            # Løb ind i en væg
            self.gameOver()

            # Løb ind i sig selv
        elif self.snakeBoard[self._newHeadRow][self._newHeadCol] > 0:
            self.gameOver()

        elif self.snakeBoard[self._newHeadRow][self._newHeadCol] < 0:
            self.snakeBoard[self._newHeadRow][self._newHeadCol] = self.snakeBoard[self._headRow][self._headCol] + 1

            SnakeFood.placeFood(self)
            self.re_draw()

        else:
            print("fejl")
            self.snakeBoard[self._newHeadRow][self._newHeadCol] = self.snakeBoard[self._headRow][self._headCol] + 1


            Movement.removeTail(self)
            self.re_draw()
        self._headRow = self._newHeadRow
        self._headCol = self._newHeadCol
