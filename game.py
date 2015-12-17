import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

FIELD_SIZE = 10
OFF_STATE = 0
ON_STATE = 255


def add_glider(grid, i, j):
    """Adds a glider to grid starting from (i, j) coords"""
    glider = np.array([
        [ON_STATE, OFF_STATE, OFF_STATE],
        [OFF_STATE, ON_STATE, ON_STATE],
        [ON_STATE, ON_STATE, OFF_STATE]])
    grid[i:i+3, j:j+3] = glider


x = np.array([[OFF_STATE, OFF_STATE, ON_STATE], [ON_STATE, ON_STATE, OFF_STATE], [OFF_STATE, ON_STATE, OFF_STATE]])


grid = np.random.choice([OFF_STATE, ON_STATE], 4*4, p=[0.1, 0.9]).reshape(4, 4)


def main():
    grid = np.zeros(FIELD_SIZE*FIELD_SIZE).reshape(FIELD_SIZE, FIELD_SIZE)
    add_glider(grid, 1, 1)
    plt.imshow(grid, interpolation='nearest')

    plt.show()

if __name__ == '__main__':
    main()
