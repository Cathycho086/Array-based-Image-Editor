import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Create initial grid.
grid = np.array([
    [255, 255, 0, 0],
    [255, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
])

rshift = np.array([
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    ])

lshift = np.array([
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    ])

flip = np.array([
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
])

wrap_shift = np.array([
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0]
])


display_grid = grid @ flip
# Setup figure and image
fig, ax = plt.subplots()
img = ax.imshow(display_grid, cmap='gray_r', interpolation='nearest')
plt.axis('on')  # Optional: Hide axes
plt.show()
