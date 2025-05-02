# Conway's game of life-emergent behavior, on tkinter.
#ChatGPT generated
import tkinter as tk
import random

# Settings
CELL_SIZE = 15
ROWS = 40
COLS = 40
ALIVE_COLOR = "#ffffff"
DEAD_COLOR = "#000000"
DELAY = 100  # in milliseconds

class GameOfLife:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg=DEAD_COLOR)
        self.canvas.pack()
        self.grid = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]
        self.rects = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.draw_initial_grid()
        self.running = True
        self.update()

    def draw_initial_grid(self):
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                color = ALIVE_COLOR if self.grid[row][col] else DEAD_COLOR
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                self.rects[row][col] = rect

    def update(self):
        if self.running:
            new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
            for row in range(ROWS):
                for col in range(COLS):
                    neighbors = self.count_neighbors(row, col)
                    if self.grid[row][col] == 1:
                        new_grid[row][col] = 1 if neighbors in [2, 3] else 0
                    else:
                        new_grid[row][col] = 1 if neighbors == 3 else 0
            self.grid = new_grid
            self.draw()
            self.master.after(DELAY, self.update)

    def count_neighbors(self, row, col):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                r, c = row + i, col + j
                if 0 <= r < ROWS and 0 <= c < COLS:
                    count += self.grid[r][c]
        return count

    def draw(self):
        for row in range(ROWS):
            for col in range(COLS):
                color = ALIVE_COLOR if self.grid[row][col] else DEAD_COLOR
                self.canvas.itemconfig(self.rects[row][col], fill=color)

# Run it
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Conway's Game of Life")
    game = GameOfLife(root)
    root.mainloop()
