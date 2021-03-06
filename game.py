import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


FIELD_SIZE = 100
OFF_STATE = 0
ON_STATE = 255
MINIMUM_FIELD_SIZE = 8
UPDATE_INTERVAL = 50


def add_glider(grid, i, j):
    """Adds a glider to grid starting from (i, j) coords"""
    glider = np.array([
        [ON_STATE, OFF_STATE, OFF_STATE],
        [OFF_STATE, ON_STATE, ON_STATE],
        [ON_STATE, ON_STATE, OFF_STATE]])
    grid[i:i+3, j:j+3] = glider


def add_loaf(grid, i, j):
    """Adds a loaf to grid starting from (i, j) coords"""
    loaf = np.array([
        [OFF_STATE, ON_STATE, ON_STATE, OFF_STATE],
        [ON_STATE, OFF_STATE, OFF_STATE, ON_STATE],
        [OFF_STATE, ON_STATE, OFF_STATE, ON_STATE],
        [OFF_STATE, OFF_STATE, ON_STATE, OFF_STATE]])
    grid[i:i+4, j:j+4] = loaf


def add_blinker(grid, i, j):
    """Adds a blinker to grid starting from (i, j) coords"""
    blinker = np.array([
        [OFF_STATE, ON_STATE, OFF_STATE],
        [OFF_STATE, ON_STATE, OFF_STATE],
        [OFF_STATE, ON_STATE, OFF_STATE]])
    grid[i:i+3, j:j+3] = blinker


def add_custom_pattern(grid, i, j, pattern):
    h = len(pattern)
    w = len(pattern[0])
    grid[i:i+h, j:j+w] = blinker


def generate_random_grid(size=FIELD_SIZE):
    return np.random.choice([OFF_STATE, ON_STATE], size*size, p=[0.5, 0.5]).reshape(size, size)


def update_field(frame_number, grid, field_size, img):
    new_grid = grid.copy()
    for i in range(field_size):
        for j in range(field_size):
            sum_around = int((
                grid[i, (j-1) % field_size] + grid[i, (j+1) % field_size] +
                grid[(i-1) % field_size, j] + grid[(i + 1) % field_size, j] +
                grid[(i-1) % field_size, (j-1) % field_size] + grid[(i-1) % field_size, (j+1) % field_size] +
                grid[(i+1) % field_size, (j-1) % field_size] + grid[(i+1) % field_size, (j+1) % field_size]) / 255)
            if grid[i, j] == ON_STATE:
                if (sum_around < 2) or (sum_around > 3):
                    new_grid[i, j] = OFF_STATE
            else:
                if sum_around == 3:
                    new_grid[i, j] = ON_STATE
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,


def main():
    parser = argparse.ArgumentParser(description="Conway's game of life demo")
    parser.add_argument('--size', dest='FIELD_SIZE', required=False)
    parser.add_argument('--interval', dest='update_interval', help='Grid update time in milliseconds', required=False)
    parser.add_argument('--glider', action='store_true', help="Whether to start animation with glider pattern.", required=False)

    args = parser.parse_args()

    global FIELD_SIZE, MINIMUM_FIELD_SIZE, UPDATE_INTERVAL

    if args.FIELD_SIZE and int(args.FIELD_SIZE) > MINIMUM_FIELD_SIZE:
        FIELD_SIZE = int(args.FIELD_SIZE)

    if args.update_interval:
        # TODO: upper case vars are misleading, they are not constants
        UPDATE_INTERVAL = int(args.update_interval)

    if args.glider:
        grid = np.zeros(FIELD_SIZE*FIELD_SIZE).reshape(FIELD_SIZE, FIELD_SIZE)
        # add_glider(grid, 1, 1)
        add_blinker(grid, 1, 1)
    else:
        grid = generate_random_grid(FIELD_SIZE)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    anim = animation.FuncAnimation(fig, update_field, fargs=(grid, FIELD_SIZE, img, ),
                            frames=200, interval=UPDATE_INTERVAL, save_count=50)
    # anim.save('conway_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()

if __name__ == '__main__':
    main()
