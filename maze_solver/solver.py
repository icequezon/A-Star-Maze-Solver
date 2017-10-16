import math

from .maze import WeightedMaze


class MazeSolver():

    def __init__(self, maze):
        """
        Accepts a maze as argument and sets the maze
        to be solved.
        """
        self.maze = maze
        self.open_list = []
        self.closed_list = []
        self.parent_list = []

    def find_goal(self):
        """
        Finds the goal inside the maze. Returns a
        pair of coordinates.
        """
        return self.maze.find_tile('.')

    def find_start(self):
        """
        Finds the goal inside the maze. Returns a
        pair of coordinates.
        """
        return self.maze.find_tile('P')

    def calculate_heuristics(self, method, goal):
        """
        Calculate heuristics of the maze. Accepts
        an argument method for heuristic method.
        """
        self.maze = method.calculate(self.maze, goal)

    def can_be_visited(self, coordinates):
        x = coordinates[0]
        y = coordinates[1]

        return (
            self.maze.is_traversable(x, y) and
            not self.in_closed_list(coordinates)
        )

    def in_closed_list(self, coordinates):
        for item in self.closed_list:
            if item[0] == coordinates:
                return True
        return False

    def get_smallest(self):
        smallest = self.open_list[0]

        for item in self.open_list:
            if item[3] < smallest[3]:
                smallest = item

        return smallest

    def solve(self):
        """
        Solves the maze. Throws exception if maze is not set of if method
        is not set. Returns an array of paths from starting point to goal.
        """
        self.maze = WeightedMaze(self.maze)

        goal = self.find_goal()
        start = self.find_start()

        # Use Manhattan Heuristics
        method = ManhattanHeuristic()
        self.calculate_heuristics(method, goal)

        cur_loc = (start[0], start[1])

        # coordinates, cost, heuristics, total
        cur_node = (cur_loc, 0, 0, 0)
        while cur_loc != goal:
            self.closed_list.append(cur_node)

            # Get adjacent nodes
            possible_visits = self.maze.get_adjacent(cur_loc[0], cur_loc[1])
            filtered = filter(self.can_be_visited, possible_visits)
            accepted_visits = list(filtered)

            for node in accepted_visits:
                cost = cur_node[1] + 1
                heuristics = self.maze.get_weight(node[0], node[1])
                total = cost + heuristics
                if not self.in_closed_list(node):
                    # coordinates, cost, heuristics, total
                    self.open_list.append((node, cost, heuristics, total))
                    self.parent_list.append((cur_loc, node))

            cur_node = self.get_smallest()
            cur_loc = cur_node[0]
            self.open_list.remove(cur_node)

        path = []
        path.append(cur_loc)

        while cur_loc != start:
            self.maze.set_tile(cur_loc[0], cur_loc[1], '.')
            for item in self.parent_list:
                if item[1] == cur_loc:
                    path.append(item[0])
                    cur_loc = item[0]
                    break

        print("\n Path: ", path, "\n")
        print(self.maze)


class BaseHeuristic():

    def calculate(self, maze):
        """
        Accepts a maze and calculates the heuristics
        of the maze.
        """
        pass

    class Meta:
        abtract = True


class ManhattanHeuristic(BaseHeuristic):

    def calculate(self, maze, goal):
        self.maze = maze

        goal_x = goal[0]
        goal_y = goal[1]

        y = 0
        for row in maze.maze:
            x = 0
            for item in row:
                weight = math.fabs(goal_x - x) + math.fabs(goal_y - y)
                maze.set_weight(x, y, weight)
                x = x + 1

            y = y + 1

        return maze


class StraightHeuristic(BaseHeuristic):
    pass
