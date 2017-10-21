#!/usr/bin/env python

import sys

from maze_solver.solver import (
    MazeSolver,
    ManhattanHeuristic,
    StraightHeuristic
)
from maze_solver.reader import read


def run(args):
    maze_paths = args
    maze_paths.pop(0)

    heuristic_method = ManhattanHeuristic()

    if '-' == maze_paths[0][0]:
        options = maze_paths.pop(0)
        if options == '-m':
            print("Uses Manhattan Heuristic")
            heuristic_method = ManhattanHeuristic()
        elif options == '-s':
            print("Uses Straight Heuristic")
            heuristic_method = StraightHeuristic()
        else:
            print(options, ": is not recognized.")
            return

    for path in maze_paths:
        maze = read(path)
        print("File Name: ", path)
        print(maze)

        solver = MazeSolver(maze, heuristic_method)
        solver.solve()
        print("=================================================")


run(sys.argv)
