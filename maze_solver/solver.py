class MazeSolver():
    maze = None
    method = None

    def init(self, maze):
        """
        Accepts a maze as argument and sets the maze
        to be solved.
        """
        self.maze = maze

    def calculate_heuristics(self, method):
        """
        Calculate heuristics of the maze. Accepts
        an argument method for heuristic method.
        """
        # TODO
        pass

    def solve(self):
        """
        Solves the maze. Throws exception if maze
        is not set of if method is not set. Returns
        an array of paths from starting point to goal.
        """
        # TODO
        pass


class BaseHeuristic():

    def calculate_heuristic(self, maze):
        """
        Accepts a maze and calculates the heuristics
        of the maze.
        """
        pass

    class Meta:
        abstract = True


class ManhattanHeuristic(BaseHeuristic):
    pass


class StraightHeuristic(BaseHeuristic):
    pass
