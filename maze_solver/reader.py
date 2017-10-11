from .maze import Maze


def read(file_location):
    """
    Read .txt file that has a maze inside and
    parses .txt file and returns a maze.
    """
    f = open(file_location, "r")
    new_maze = Maze()

    x = 0
    y = 0

    # Find dimensions of maze
    for line in f:
        x = len(line)
        y = y + 1

    # Set maze size
    new_maze.set_maze_size(x, y)

    f.close()
    f = open(file_location, "r")

    x = 0
    y = 0
    for line in f:
        x = 0
        for symbol in line:
            # Set tile in maze
            new_maze.set_tile(x, y, symbol)
            x = x + 1
        y = y + 1

    f.close()

    return new_maze
