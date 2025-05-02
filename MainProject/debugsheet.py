import numpy as np
import matplotlib.pyplot as plt

theta_deg = 30
theta = np.radians(theta_deg)

image = np.array([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 100, 180, 255, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
])

#  Rotate an array-based image.
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])
coords = []
rot_coords = []

# Extract coords.
# Calculate for inconsistencies-row,col starts count with 0 & the center of rotation is top left an should be changed to bottom left.
for row, col in np.ndindex(image.shape):
    val = image[row, col]
    if image[row, col] != 0:
        coords.append(((col + 1, image.shape[0] - row), val))

for (raw_xy, val) in coords:
    arr_raw_xy = np.array(raw_xy).reshape(2, 1)
    arr_rot_xy = rotation_matrix @ arr_raw_xy 
    arr_rot_nat_xy = np.round(arr_rot_xy).astype(int)
    rot_coords.append((tuple(arr_rot_nat_xy.flatten()), val))

# Turn coords back into an array.
rot_image = np.zeros((image.shape[0], image.shape[1]), dtype=int)
for (x, y), value in rot_coords:
    # The image should be shown only in the given 'window' with no wraparound.
    if image.shape[1] >= x >= 1 and image.shape[0] >= y >= 1:
        rot_image[image.shape[0] - y, x - 1] = value

"""Displays the array in matplotlib"""
fig, ax = plt.subplots()
img = ax.imshow(rot_image, cmap='gray_r', interpolation='nearest')
plt.axis('on')  # Optional: Hide axes
plt.show()