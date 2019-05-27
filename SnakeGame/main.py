import tkinter as tk

from _movement import Movement
from _snakeFood import SnakeFood

"""
    main.py
    ~~~~~~~
    Håndterer alt design, tid, bindings og start/slut af spil
"""

class SnakeGame:
    def __init__(self, master, canvas):
        self._master = master
        self._c = canvas
        self._title = "The Real Snake Game"
        self.timer = None
        self._headRow = 0
        self._headCol = 0
        self._newHeadRow = None
        self._newHeadCol = None
        # BINDINGS
        self._master.bind('<Right>', lambda _: Movement.moveSnake(self, 0, 1))
        self._master.bind('<Left>', lambda _: Movement.moveSnake(self, 0, -1))
        self._master.bind('<Down>', lambda _: Movement.moveSnake(self, 1, 0))
        self._master.bind('<Up>', lambda _: Movement.moveSnake(self, -1, 0))
        self._master.bind('<r>', lambda _: self.load_game())
        self._master.bind('<q>', lambda _: window.destroy())

        self.load_game()

    def load_game(self):
        """ Sætter spillet op """
        self.rowSize = 10
        self.colSize = 10
        self._master.title(self._title)
        if self.timer:
            self._c.after_cancel(self.timer)
        self.load_board()
        self.re_draw()
        self.boardTimer()

    def re_draw(self):
        """ Opdaterer boardet """,
        self._c.delete("all")
        self.draw_board()

    def load_board(self):
        """ Starter boardet """
        self.ignoreNextTime = False
        self.isGameOver = False
        self.snakeBoard = []
        for row in range(int(self.rowSize)):
            self.snakeBoard += [[0] * self.colSize]
        self.snakeBoard[int(self.rowSize/2)][int(self.colSize/2)] = 1

        self.rows = len(self.snakeBoard)
        self.cols = len(self.snakeBoard[0])

        SnakeFood.placeFood(self)
        """ Finder hovedet og gemmer det"""
        self._headRow, self._headCol = Movement.findSnakeHead(self)
        self._snakeDRow = -1
        self._snakeDCol = 0

    def draw_board(self):
        """ Kalder draw_cells for hver celle """
        for self.row in range(self.rows):
            for self.col in range(self.cols):
                self.draw_cells(self.row, self.col, self.snakeBoard)

    def draw_cells(self, row, col, snakeBoard):
        """ Tegner seperat cellerne ud fra snakeBoardet """
        self.margen = 5
        self.cellsize = 30
        self.x1 = self.margen + self.col * self.cellsize  # x1
        self.x2 = self.x1 + self.cellsize  # x2
        self.y1 = self.margen + row * self.cellsize  # y1
        self.y2 = self.y1 + self.cellsize  # y2
        self._c.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="white", outline="black")

        if snakeBoard[row][col] > 0:
            self._c.create_oval(self.x1, self.y1, self.x2, self.y2, fill="blue")

        elif snakeBoard[row][col] < 0:
            self._c.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

    def boardTimer(self):
        """ Bestemmer hastighed og sværhedsgrad på spillet """
        self.delay = 150
        if not self.isGameOver:
            if not self.ignoreNextTime:
                Movement.moveSnake(self, self._snakeDRow, self._snakeDCol)
                self.re_draw()
        self.ignoreNextTime = False
        self.timer = self._c.after(self.delay, self.boardTimer)

    def gameOver(self):
        """ Slutter spillet og viser spilleren antal point opnået """
        self.text_gameOver = self._c.create_text(155, 155, text="Game Over!", font=("Helvetica", 32, "bold"))
        self.text_score = self._c.create_text(155, 200, text="score", font=("Helvetica", 20, "bold"))
        self.text_scoreNumber = self._c.create_text(155, 230, text=self.snakeBoard[self._headRow][self._headCol], font=("Helvetica", 20, "bold"))
        self.isGameOver = True

if __name__ == "__main__":
    """ Kører fra starten """
    window = tk.Tk()
    c = tk.Canvas(window, width=500, height=500)
    c.pack()
    game = SnakeGame(window, c)

    window.mainloop()
