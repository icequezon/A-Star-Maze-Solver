#!/usr/bin/env python

import sys

from maze_solver.solver import MazeSolver
from maze_solver.reader import MazeReader


def run(args):
    maze_paths = args

    for path in maze_paths:
        reader = MazeReader()
        maze = reader.read(path)

        solver = MazeSolver()
        solver.solve(maze)


run(sys.argv)
