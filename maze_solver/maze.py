
class Maze():
    """
    This is a representation of a maze
    """
    # Maze representation
    maze = []

    # Maze tile values
    TILE_TYPES = [
        '%',
        ' ',
        '.',
        'P'
    ]

    def __init__(self):
        """
        Initialize variables in class.
        """
        self.maze = []

    def set_maze_size(self, length, width):
        """
        Accepts length and width and initializes maze
        to given size.
        """
        for x in range(0, width):
            self.maze.append(['' for x in range(0, length)])

    def get_tile(self, x, y):
        """
        Accepts coordinates and returns the specified
        tile in the maze.
        """
        return self.maze[y][x]

    def set_tile(self, x, y, value):
        """
        Accepts coordinates and a value and sets
        the value of the tile in the maze. Returns the
        value of the tile if set is successful. Throws
        an exception if value in invalid.
        """
        if self.value_is_valid(value):
            self.maze[y][x] = value
        else:
            # Throw error
            # TODO
            return None

        return self.maze[y][x]

    def value_is_valid(self, value):
        """
        Accepts a value and checks if value is a valid
        maze value.
        """
        return value in self.TILE_TYPES

    def is_traversable(self, x, y):
        """
        Accepts coordinates and return if tile can
        be traversed or not.
        """
        # TODO
        pass

    def __str__(self):
        maze_string = ''
        for x in self.maze:
            for y in x:
                maze_string = maze_string + y
            maze_string = maze_string + '\n'

        return maze_string


class WeightedMaze(Maze):
    weights = [[]]

    def get_weight(self, x, y):
        """
        Accepts coordinates and returns weight
        the tile in the maze.
        """
        return self.weights[x][y]

    def set_weight(self, x, y, value):
        """
        Accepts coordinates and a value and sets tile
        to weight value. Returns the value of the tile
        if set is successful.
        """
        self.weights[x][y] = value

        return self.weights[x][y]
