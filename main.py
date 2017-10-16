#!/usr/bin/env python

import sys

from maze_solver.solver import MazeSolver
from maze_solver.reader import read


def run(args):
    maze_paths = args
    maze_paths.pop(0)

    for path in maze_paths:
        maze = read(path)
        print("File Name: ", path)
        print(maze)

        solver = MazeSolver(maze)
        solver.solve()
        print("=================================================")


run(sys.argv)
