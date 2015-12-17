import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

FIELD_SIZE = 10


def add_glider(grid, i, j):
    """Adds a glider to grid starting from (i, j) coords"""
    glider = np.array([
        [255, 0, 0],
        [0, 255, 255],
        [255, 255, 0]])
    grid[i:i+3, j:j+3] = glider


x = np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]])


grid = np.random.choice([0, 255], 4*4, p=[0.1, 0.9]).reshape(4, 4)


def main():
    grid = np.zeros(FIELD_SIZE*FIELD_SIZE).reshape(FIELD_SIZE, FIELD_SIZE)
    add_glider(grid, 1, 1)
    plt.imshow(grid, interpolation='nearest')

    plt.show()

if __name__ == '__main__':
    main()
