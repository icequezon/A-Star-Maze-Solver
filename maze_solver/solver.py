import math

from maze_solver.maze import WeightedMaze


class MazeSolver():

    def __init__(self, maze, heuristic_method):
        """
        Accepts a maze and heuristic method as
        argument and sets the maze to be solved.
        """
        self.maze = maze
        self.heuristic_method = heuristic_method
        self.open_list = []
        self.closed_list = []
        self.parent_list = []

    def find_goal(self):
        """
        Finds the goal inside the maze. Returns a
        pair of coordinates.
        """
        return self.maze.find_tiles('.')

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
        """
        Check if coordinates can be traversed and
        not in closed_list.
        """
        x = coordinates[0]
        y = coordinates[1]

        return (
            self.maze.is_traversable(x, y) and
            not self.in_closed_list(coordinates)
        )

    def in_closed_list(self, coordinates):
        """
        Checks if coordinates is in closed_list.
        """
        for item in self.closed_list:
            if item[0] == coordinates:
                return True
        return False

    def in_open_list(self, coordinates):
        """
        Checks if coordinate is in open_list.
        """
        for item in self.open_list:
            if item[0] == coordinates:
                return True
        return False

    def update_open_list(self, coordinates, cost, heuristics, total):
        """
        Updates the value of a node in the open_list.
        If new total is smaller, update node else just
        maintain old value.
        """
        for item in self.open_list:
            if item[0] == coordinates and item[3] > total:
                item = (coordinates, cost, heuristics, total)

    def get_smallest(self):
        """
        Return the smallest value total in open_list.
        """
        smallest = self.open_list[0]

        for item in self.open_list:
            if item[3] < smallest[3]:
                smallest = item
        return smallest

    def get_nearest_goal(self, start, goals):
        """
        Returns a sorted list of goals based on
        how near they are to start.
        """
        # Get very big number
        smallest = 100000

        nearest = goals[0]
        start_x = start[0]
        start_y = start[1]

        for goal in goals:
            maze = WeightedMaze(self.maze)
            maze = self.heuristic_method.calculate(maze, goal)

            if maze.get_weight(start_x, start_y) < smallest:
                smallest = maze.get_weight(start_x, start_y)
                nearest = goal

        return nearest

    def solve(self):
        """
        Solves the maze. Throws exception if maze is not set of if method
        is not set. Returns an array of paths from starting point to goal.
        """
        self.maze = WeightedMaze(self.maze)

        goals = self.find_goal()
        all_goals = list(goals)
        start = self.find_start()

        if start == (0, 0) or goals == []:
            # If there is no start or goal, return.
            return

        cur_loc = (start[0], start[1])
        path = []
        cost = 0
        visited_ctr = 1
        visited_goals = []

        while len(goals) > 0:
            self.open_list = []
            self.closed_list = []
            goal = self.get_nearest_goal(cur_loc, goals)
            goals.remove(goal)

            # Use specified method
            method = self.heuristic_method
            self.calculate_heuristics(method, goal)

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
                        if self.in_open_list(node):
                            # Check if already in open_list
                            self.update_open_list(node, cost, heuristics, total)
                        else:
                            # coordinates, cost, heuristics, total
                            self.open_list.append((node, cost, heuristics, total))

                        self.parent_list.append((cur_loc, node))

                cur_node = self.get_smallest()
                cur_loc = cur_node[0]
                self.open_list.remove(cur_node)

            path.append(cur_loc)
            cost = cost + cur_node[2]

            back_loc = cur_loc

            while back_loc != start:
                if back_loc in all_goals and back_loc not in visited_goals:
                    tile = str(visited_ctr)
                    self.maze.set_tile(back_loc[0], back_loc[1], tile)
                    visited_ctr = visited_ctr + 1
                    visited_goals.append(back_loc)
                elif back_loc not in visited_goals:
                    self.maze.set_tile(back_loc[0], back_loc[1], '.')
                for item in self.parent_list:
                    if item[1] == back_loc:
                        path.append(item[0])
                        back_loc = item[0]
                        break

        print("\nPath: ", path, "\n")
        print("Cost: ", len(path))
        print("Solution: ")
        print(self.maze)


class BaseHeuristic():

    def calculate(self, maze, goal):
        """
        Accepts a maze and calculates the heuristics
        of the maze.
        """
        pass

    class Meta:
        abstract = True


class ManhattanHeuristic(BaseHeuristic):

    def calculate(self, maze, goal):
        """
        Calculate heuristics using Manhattan Distance.
        Formula: |x1 - x2| + |y1 _ y2|
        """
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
    def calculate(self, maze, goal):
        """
        Calculate heuristics using Straight Line Distance.
        Formula: dx = |x1 - x2|
                 dy = |y1 - y2|
                 cost * max(dx,dy)
        """

        self.maze = maze

        D = 1
        goal_x = goal[0]
        goal_y = goal[1]

        y = 0
        for row in maze.maze:
            x = 0
            for item in row:
                dx = math.fabs(goal_x - x)
                dy = math.fabs(goal_y - y)
                weight = D * max(dx, dy)
                maze.set_weight(x, y, weight)
                x = x + 1

            y = y + 1
        return maze
