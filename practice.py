import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

img = np.array([
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
])

# Flipping matrix (rows reversed)
flip_matrix_lr = np.array([
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
])

flip_matrix_hor = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
])

array = img @ flip_matrix_hor

# Setup figure and image
fig, ax = plt.subplots()
img = ax.imshow(array, cmap='gray', interpolation='nearest')
plt.axis('off')  # Optional: Hide axes
plt.show()