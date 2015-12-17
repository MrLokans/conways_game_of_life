import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

FIELD_SIZE = 10
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


def generate_random_grid(size=FIELD_SIZE):
    return np.random.choice([OFF_STATE, ON_STATE], size*size, p=[0.1, 0.9]).reshape(size, size)


def main():
    parser = argparse.ArgumentParser(description="Conway's game of life demo")
    parser.add_argument('--size', dest='FIELD_SIZE', required=False)
    parser.add_argument('--interval', dest='update_interval', help='Grid update time in milliseconds', required=False)
    parser.add_argument('--glider', action='store_true', help="Whether to start animation with glider pattern.", required=False)

    args = parser.parse_args()

    if args.FIELD_SIZE and int(args.FIELD_SIZE) > MINIMUM_FIELD_SIZE:
        FIELD_SIZE = int(args.FIELD_SIZE)

    if args.update_interval:
        UPDATE_INTERVAL = int(args.update_interval)

    if args.glider:
        grid = np.zeros(FIELD_SIZE*FIELD_SIZE).reshape(FIELD_SIZE, FIELD_SIZE)
    else:
        grid = generate_random_grid(FIELD_SIZE)


if __name__ == '__main__':
    main()
