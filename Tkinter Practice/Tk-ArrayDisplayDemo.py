# ChatGPT generated.
from tkinter import *
from tkinter import ttk

grid_map = [
    [0, 1, 0],
    [1, 1, 1],
    [1, 0, 1],
]

CELL_SIZE = 40

color_map = {
    0:'white',
    1:'black'
}

root = Tk()
root.title("grid_sample")

canvas = Canvas(root, width=400, height=400)
canvas.pack()

for row in range(len(grid_map)):
    for col in range(len(grid_map[0])):
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        value = grid_map[row][col]
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_map.get(value, "gray"), outline="gray")

root.mainloop()