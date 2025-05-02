import cupy as cp
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Of those following 'def's those that concern PIL, they were generated using ChatGPT, 
# and since I had no time to study PIL or image processing in python at all, 
# I have no idea what those do and will not touch them throughout the development of this entire project.
class MatrixImgEdit():
    def __init__(self, path=None):
        """Initialize the editor with an optional image path."""
        self.original = None
        self.image = None

        if path:
            self.load_grayscale(path)

    def load_grayscale(self, path):
        """Load an image as grayscale and store it."""
        img = Image.open(path).convert('RGBA').convert('L')
        self.original = cp.array(img)
        self.image = self.original.copy()

    def show(self):
        """Displays the array in matplotlib"""
        fig, ax = plt.subplots()
        img = ax.imshow(self.image.get(), cmap='gray_r', interpolation='nearest')
        plt.axis('on')  # Optional: Hide axes
        plt.show()

    def save_image(self, path):
        """Save the current working image to a file."""
        if self.image is not None:
            Image.fromarray(self.image).save(path)
        else:
            raise ValueError("No image loaded.")

    def reset(self):
        """Reset the working image to the original."""
        if self.original is not None:
            self.image = self.original.copy()

    def right_shift(self, shift=1):
        """Shifts img right by the given amount."""
        right_shift_matrix_instance = self.right_shift_matrix()
        for i in range(shift):
            M = self.image @ right_shift_matrix_instance
            self.image = M

    def left_shift(self, shift=1):
        """Shifts img left by the given amount."""
        left_shift_matrix_instance = self.left_shift_matrix()
        for i in range(shift):
            M = self.image @ left_shift_matrix_instance
            self.image = M

    def up_shift(self, shift=1):
        """Shifts img up by the given amount."""
        up_shift_matrix_instance = self.up_shift_matrix()
        for i in range(shift):
            M = up_shift_matrix_instance @ self.image
            self.image = M

    def down_shift(self, shift=1):
        """Shifts img down by the given amount."""
        down_shift_matrix_instance = self.down_shift_matrix()
        for i in range(shift):
            M = down_shift_matrix_instance @ self.image
            self.image = M

    def y_flip(self):
        """Flips image by the y-axis."""
        self.image = self.image @ self.yflip_matrix()

    def x_flip(self):
        """Flips image by the x-axis."""
        self.image = self.xflip_matrix() @ self.image

    def right_shift_matrix(self):
        """Create a right-shift matrix of size (width × width)."""
        M = cp.zeros((self.image.shape[1], self.image.shape[1]), dtype=int) #create blank array
        #create matrix [0, 1, 0, 0, ...],[0, 0, 1, 0, ...],[0, 0, 0, 1, ...]....[0, ..., 0, 0, 1], [0, 0, ...0, 0]
        for i in range(self.image.shape[1]):
            j = (i + 1)
            if j < self.image.shape[1]:
                M[i, j] = 1
        return M
    
    def left_shift_matrix(self):
        """Create a left-shift matrix of size (width × width)."""
        M = cp.zeros((self.image.shape[1], self.image.shape[1]), dtype=int) #create blank array
        #create matrix [0, 0, 0, 0, ...],[1, 0, 0, 0, ...],[0, 1, 0, 0, ...]....[0, ..., 1, 0, 0], [0, 0, ...1, 0]
        for i in range(self.image.shape[1]):
            j = (i - 1)
            if 0 <= j:
                M[i, j] = 1
        return M
    
    def up_shift_matrix(self):
        """Create a up-shift matrix of size (height × height)."""
        M = cp.zeros((self.image.shape[0], self.image.shape[0]), dtype=int) #create blank array
        #create matrix [0, 1, 0, 0, ...],[0, 0, 1, 0, ...],[0, 0, 0, 1, ...]....[0, ..., 0, 0, 1], [0, 0, ...0, 0]
        for i in range(self.image.shape[0]):
            j = (i + 1)
            if j < self.image.shape[0]:
                M[i, j] = 1
        return M
    
    def down_shift_matrix(self):
        """Create a down-shift matrix of size (height × height)."""
        M = cp.zeros((self.image.shape[0], self.image.shape[0]), dtype=int) #create blank array
        #create matrix [0, 0, 0, 0, ...],[1, 0, 0, 0, ...],[0, 1, 0, 0, ...]....[0, ..., 1, 0, 0], [0, 0, ...1, 0]
        for i in range(self.image.shape[0]):
            j = (i - 1)
            if 0 <= j:
                M[i, j] = 1
        return M
    
    
    def yflip_matrix(self):
        """Create a Yaxis-flip matrix of size (width × width)."""
        M = cp.zeros((self.image.shape[1], self.image.shape[1]), dtype=int) #create blank array
        #create matrix [..., 0, 0, 0, 1],[..., 0, 0, 1, 0],[..., 0, 1, 0, 0]....[0, 1, 0, 0, ...], [1, 0, 0, 0, ..]
        for i in range(self.image.shape[1]):
            j = self.image.shape[1] - i - 1
            M[i, j] = 1
        return M
    
    def xflip_matrix(self):
        """Create a Yaxis-flip matrix of size (height × height)."""
        M = cp.zeros((self.image.shape[0], self.image.shape[0]), dtype=int) #create blank array
        #create matrix [..., 0, 0, 0, 1],[..., 0, 0, 1, 0],[..., 0, 1, 0, 0]....[0, 1, 0, 0, ...], [1, 0, 0, 0, ..]
        for i in range(self.image.shape[0]):
            j = self.image.shape[0] - i - 1
            M[i, j] = 1
        return M
    
    def rotate(self, theta_deg):
        """Rotate an array-based image."""
        coords = []
        height = self.image.shape[0]
        theta_deg = 30

        # Time consuming even on GPU but workaround is too complicated for current level.
        for row, col in cp.ndindex(self.image.shape):
            val = self.image[row, col]
            if val != 0:
                # original logic: ((col + 1, height - row), val)
                coords.append(((col + 1, height - row), val))

        # vectorize it
        xy = cp.array([c[0] for c in coords])      # shape (N, 2)
        vals = cp.array([c[1] for c in coords])

        theta = cp.radians(theta_deg)
        rotation_matrix = cp.array([
            [cp.cos(theta), -cp.sin(theta)],
            [cp.sin(theta),  cp.cos(theta)]
        ])

        # rotate (x, y)
        rotated_xy = xy @ rotation_matrix.T
        rotated_xy = cp.rint(rotated_xy).astype(cp.int32)

        # undo the coordinate transformation: back to (row, col)
        new_coords = cp.stack([
            height - rotated_xy[:, 1],
            rotated_xy[:, 0] - 1
        ], axis=1)

        # filter valid
        valid = (new_coords[:, 0] >= 0) & (new_coords[:, 0] < height) & \
                (new_coords[:, 1] >= 0) & (new_coords[:, 1] < self.image.shape[1])

        output = cp.zeros_like(self.image)
        output[new_coords[valid, 0], new_coords[valid, 1]] = vals[valid]

        self.image = output

