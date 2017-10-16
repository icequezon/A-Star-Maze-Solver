
class Maze():
    """
    This is a representation of a maze
    """
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
            return None

        return self.maze[y][x]

    def find_tile(self, character):
        """
        Finds the goal inside the maze. Returns a
        pair of coordinates.
        """
        x = 0
        y = 0

        tile_x = 0
        tile_y = 0

        for row in self.maze:
            x = 0
            for item in row:
                if item == character:
                    tile_x = x
                    tile_y = y
                x = x + 1
            y = y + 1

        return (tile_x, tile_y)

    def get_adjacent(self, node_x, node_y):
        nodes = []
        start_x = node_x - 1
        start_y = node_y - 1

        for x in range(start_x, start_x + 3):
            for y in range(start_y, start_y + 3):
                if (x, y) != (node_x, node_y):
                    nodes.append((x, y))

        return nodes

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
        return self.maze[y][x] != '%'

    def __str__(self):
        """
        String representation of maze
        """
        maze_string = ''
        for x in self.maze:
            for y in x:
                maze_string = maze_string + y
            maze_string = maze_string + '\n'

        return maze_string


class WeightedMaze(Maze):

    def __init__(self, maze):
        """
        Initialize WeightedMaze.
        """
        self.maze = maze.maze
        self.weights = []
        for row in self.maze:
            length = len(row)
            self.weights.append(['' for x in range(0, length)])

    def get_weight(self, x, y):
        """
        Accepts coordinates and returns weight
        the tile in the maze.
        """
        return self.weights[y][x]

    def set_weight(self, x, y, value):
        """
        Accepts coordinates and a value and sets tile
        to weight value. Returns the value of the tile
        if set is successful.
        """
        self.weights[y][x] = value

        return self.weights[y][x]
