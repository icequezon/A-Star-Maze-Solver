#!/usr/bin/env python

import sys

from maze_solver.solver import MazeSolver
from maze_solver.reader import read


def run(args):
    maze_paths = args

    for path in maze_paths:
        maze = read(path)

        solver = MazeSolver(maze)
        solver.solve()


run(sys.argv)
