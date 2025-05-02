import cupy as cp

theta_deg = 30
theta = cp.radians(theta_deg)

image = cp.array([
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
])

coords = []
rot_coords = []

# Extract coords.
# Calculate for inconsistencies-row,col starts count with 0 & the center of rotation is top left an should be changed to bottom left.
for row, col in cp.ndindex(image.shape):
    val = image[row, col]
    if image[row, col] != 0:
        coords.append(((col + 1, image.shape[0] - row), val))

# coords = list of ((x, y), value)
xy = cp.array([c[0] for c in coords])        # shape: (N, 2)
vals = cp.array([c[1] for c in coords])      # shape: (N,)

rotation_matrix = cp.array([
    [cp.cos(theta), -cp.sin(theta)],
    [cp.sin(theta),  cp.cos(theta)]
])
# Apply matrix multiplication: shape (N, 2) @ (2, 2).T => (N, 2)
rotated_xy = xy @ rotation_matrix.T

# Round to nearest pixel grid
rotated_xy = cp.rint(rotated_xy).astype(cp.int32)
