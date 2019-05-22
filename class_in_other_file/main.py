import tkinter as tk

from class_in_other_file._movement import Movement
from class_in_other_file._snakeFood import SnakeFood


"""
Main
"""


class SnakeGame:
    def __init__(self, master, canvas):
        self._master = master
        self._c = canvas
        self._title = "The Real Snake Game"

        self._headRow = 0
        self._headCol = 0

        self._newHeadRow = None
        self._newHeadCol = None
        # photo = tk.PhotoImage("/cross.gif")

        # BINDINGS
        self._master.bind('<Right>', lambda _: Movement.moveSnake(self, 0, 1))
        self._master.bind('<Left>', lambda _: Movement.moveSnake(self, 0, -1))
        self._master.bind('<Down>', lambda _: Movement.moveSnake(self, 1, 0))
        self._master.bind('<Up>', lambda _: Movement.moveSnake(self, -1, 0))
        self._master.bind('<r>', lambda _: self.load_game())
        self._master.bind('<q>', lambda _: window.destroy())

        # LOADER GAME
        self.load_game()


    def load_game(self):
        """ Sætter spillet op """
        self._master.title(self._title)
        self.load_board()
        self.re_draw()
        self.boardTimer()

    def re_draw(self):
        """ Opdaterer boardet """
        self._c.delete()
        self.draw_board()

    def load_board(self):
        """ starter boardet """
        self.isGameOver = False
        self.snakeBoard = \
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 2, 3, 4, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             ]

        SnakeFood.placeFood(self)
        """ Finder hovedet og gemmer det"""
        self._headRow, self._headCol = Movement.findSnakeHead(self)
        self._snakeDRow = -1
        self._snakeDCol = 0


    def draw_board(self):
        """ Kalder draw_cells for hver celle """
        self.rows = len(self.snakeBoard)
        self.cols = len(self.snakeBoard[0])

        for self.row in range(self.rows):
            for self.col in range(self.cols):
                self.draw_cells(self.row, self.col, self.snakeBoard)
                # print(str(self.row) + " " + str(self.col))

    def draw_cells(self, row, col, snakeBoard):
        """ Tegner seperat cellerne ud fra snakeBoardet """
        self.margen = 5
        self.cellsize = 30
        self.x1 = self.margen + col * self.cellsize  # x1
        self.x2 = self.x1 + self.cellsize  # x2
        self.y1 = self.margen + row * self.cellsize  # y1
        self.y2 = self.y1 + self.cellsize  # y2

        self._c.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="white", outline="black")

        if snakeBoard[row][col] > 0:
            self._c.create_oval(self.x1, self.y1, self.x2, self.y2, fill="blue")

        elif snakeBoard[row][col] < 0:
            self._c.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

    def boardTimer(self):
        self.delay = 200
        print("Før " + str(self.isGameOver))
        if not self.isGameOver:
            print("efter " + str(self.isGameOver))
            Movement.moveSnake(self, self._snakeDRow, self._snakeDCol)
            print(self._snakeDRow, self._snakeDCol)
            self.re_draw()
        self._c.after(self.delay, self.boardTimer)



    def gameOver(self):
        """ Slutter spillet og viser spilleren antal point opnået """
        # self._master.MessageBox.showinfo("Game Over")
        print("gameover")
        self.isGameOver = True
        self._c.create_text(155, 155, text="Game Over!", font=("Helvetica", 32, "bold"))


if __name__ == "__main__":
    """ Kører fra starten af """
    window = tk.Tk()
    c = tk.Canvas(window, width=310, height=310)
    c.pack()
    game = SnakeGame(window, c)

    window.mainloop()