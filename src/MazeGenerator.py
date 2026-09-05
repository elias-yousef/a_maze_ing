import random
from collections import deque


class MazeGenerator():
    """
    A class used to generate, solve, and visualize a maze.
    """
    def __init__(
            self, width: int, height: int, is_perfect: bool,
            entry_x: int, entry_y: int, exit_x: int,
            exit_y: int
            ) -> None:
        """
        Initializes the MazeGenerator with specified dimensions, type,
          and entry/exit points.

        Args:
            width (int): The width of the maze in cells.
            height (int): The height of the maze in cells.
            is_perfect (bool): Flag indicating if the maze should be a perfect
              maze (True) or a playable board with loops (False).
            entry_x (int): The x-coordinate of the maze entry.
            entry_y (int): The y-coordinate of the maze entry.
            exit_x (int): The x-coordinate of the maze exit.
            exit_y (int): The y-coordinate of the maze exit.

        Returns:
            None
        """
        self.width = width
        self.height = height
        self.is_perfect = is_perfect
        self.entry_x = entry_x
        self.entry_y = entry_y
        self.exit_x = exit_x
        self.exit_y = exit_y
        self.direction_string: str = ""

    def pattern_42(self) -> list[tuple[int, int]]:
        """
        Generates the coordinates for the "42" pattern to be carved
          into the maze.

        Calculates a fixed set of coordinates in the center
          of the maze that will be skipped
        during the wall-generation process to visually form the number "42".

        Returns:
            list[tuple[int, int]]: A list of (x, y) coordinate tuples
              representing the "42" pattern.
        """
        self.point_42 = []
        if self.width > 9 and self.height > 7:
            x = self.width // 2
            y = self.height // 2
            self.point_42.append((x - 1, y))
            self.point_42.append((x - 2, y))
            self.point_42.append((x - 3, y))
            self.point_42.append((x - 3, y - 1))
            self.point_42.append((x - 3, y - 2))
            self.point_42.append((x - 1, y + 1))
            self.point_42.append((x - 1, y + 2))
            self.point_42.append((x + 1, y))
            self.point_42.append((x + 2, y))
            self.point_42.append((x + 3, y))
            self.point_42.append((x + 3, y - 1))
            self.point_42.append((x + 3, y - 2))
            self.point_42.append((x + 2, y - 2))
            self.point_42.append((x + 1, y - 2))
            self.point_42.append((x + 1, y + 1))
            self.point_42.append((x + 1, y + 2))
            self.point_42.append((x + 2, y + 2))
            self.point_42.append((x + 3, y + 2))
        return self.point_42

    def back_trackinga_agorithm(self) -> list[list[int]]:
        """
        Generates a perfect maze using a randomized depth-first search
          (backtracking) algorithm.

        Initializes a grid where all walls are intact (represented by 15),
          then carves
        paths by tearing down walls using bitwise operations while avoiding
          the "42" pattern.

        Returns:
            list[list[int]]: A 2D list representing the maze grid, where each
            cell is an integer encoding its walls.
        """
        skipped_point = self.pattern_42()
        self.arr = [[15 for i in range(
            self.width)] for j in range(self.height)]
        self.num_cells = self.width * self.height
        self.visited_cells = []
        while True:
            start_x = random.randint(0, self.width - 1)
            start_y = random.randint(0, self.height - 1)
            if (start_x, start_y) not in skipped_point:
                break
        self.visited_cells.append((start_x, start_y))
        while self.visited_cells:
            self.next_cell = []
            x, y = self.visited_cells[-1]
            if x >= 1:
                if self.arr[y][x - 1] == 15:
                    if (x - 1, y) not in skipped_point:
                        self.next_cell.append(((x - 1), y))
            if x < self.width - 1:
                if self.arr[y][x + 1] == 15:
                    if (x + 1, y) not in skipped_point:
                        self.next_cell.append(((x + 1), y))
            if y >= 1:
                if self.arr[y - 1][x] == 15:
                    if (x, y - 1) not in skipped_point:
                        self.next_cell.append((x, (y - 1)))
            if y < self.height - 1:
                if self.arr[y + 1][x] == 15:
                    if (x, y + 1) not in skipped_point:
                        self.next_cell.append((x, (y + 1)))
            if self.next_cell:
                chosen = random.choice(self.next_cell)
                x1, y1 = chosen
                x, y = self.visited_cells[-1]
                val = ((x - x1), (y - y1))
                if val == (1, 0):
                    self.arr[y][x] -= 8
                    self.arr[y1][x1] -= 2
                elif val == (-1, 0):
                    self.arr[y][x] -= 2
                    self.arr[y1][x1] -= 8
                elif val == (0, 1):
                    self.arr[y][x] -= 1
                    self.arr[y1][x1] -= 4
                elif val == (0, -1):
                    self.arr[y][x] -= 4
                    self.arr[y1][x1] -= 1
                self.visited_cells.append(chosen)
            else:
                self.visited_cells.pop()
        return self.arr

    def imperfect(self) -> list[list[int]]:
        """
        Modifies a perfect maze into an imperfect one (playable board)
        by finding and eliminating dead-ends to create loops.
        """
        skipped_point = self.pattern_42()

        while True:
            dead_ends = []

            for y in range(self.height):
                for x in range(self.width):
                    if (x, y) in skipped_point:
                        continue

                    if bin(self.arr[y][x]).count('1') == 3:
                        dead_ends.append((x, y))

            if not dead_ends:
                break

            broken_wall = False
            for x, y in dead_ends:
                if bin(self.arr[y][x]).count('1') != 3:
                    continue

                val = self.arr[y][x]
                removable_walls = []

                # Check North (1) - subtract 1 here,
                # subtract 4 (South) from neighbor
                if val & 1 and y > 0 and (x, y - 1) not in skipped_point:
                    removable_walls.append((x, y - 1, 1, 4))
                # Check East (2) - subtract 2 here,
                # subtract 8 (West) from neighbor
                if (
                    val & 2 and x < self.width - 1 and (
                        x + 1, y) not in skipped_point
                ):
                    removable_walls.append((x + 1, y, 2, 8))
                # Check South (4) - subtract 4 here,
                # subtract 1 (North) from neighbor
                if (
                    val & 4 and y < self.height - 1 and (
                        x, y + 1) not in skipped_point
                ):
                    removable_walls.append((x, y + 1, 4, 1))
                # Check West (8) - subtract 8 here,
                # subtract 2 (East) from neighbor
                if val & 8 and x > 0 and (x - 1, y) not in skipped_point:
                    removable_walls.append((x - 1, y, 8, 2))

                # If there is a valid wall to break,
                # pick one randomly and tear it down
                if removable_walls:
                    nx, ny, wall_val, opp_val = random.choice(removable_walls)
                    self.arr[y][x] -= wall_val
                    self.arr[ny][nx] -= opp_val
                    broken_wall = True

            # Prevent an infinite loop if remaining dead
            # ends are completely trapped (e.g. by borders and 42)
            if not broken_wall:
                break

        return self.arr

    def solve_maze_bfs(self) -> str:
        """
        Finds the shortest valid path from
          the entry to the exit using Breadth-First Search (BFS).

        Traverses the generated maze grid,
          respecting the encoded walls and avoiding the
        "42" pattern, to find the most direct route.

        Returns:
            str: A string of characters ('N', 'S', 'E', 'W')
              representing the sequence of directions to solve the maze.
        """
        start = (self.entry_x, self.entry_y)
        end = (self.exit_x, self.exit_y)
        skipped_point = self.pattern_42()

        visited = set()
        visited.add(start)
        paths: dict[tuple[int, int], tuple[int, int] | None] = {start: None}
        queue = deque([start])

        while queue:
            curr_point = queue.popleft()
            if curr_point == end:
                break
            x, y = curr_point
            if x >= 1 and not (self.arr[y][x] & 8):
                neighbor = (x - 1, y)
                if neighbor not in skipped_point and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    paths[neighbor] = curr_point

            if x < self.width - 1 and not (self.arr[y][x] & 2):
                neighbor = (x + 1, y)
                if neighbor not in skipped_point and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    paths[neighbor] = curr_point

            if y >= 1 and not (self.arr[y][x] & 1):
                neighbor = (x, y - 1)
                if neighbor not in skipped_point and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    paths[neighbor] = curr_point

            if y < self.height - 1 and not (self.arr[y][x] & 4):
                neighbor = (x, y + 1)
                if neighbor not in skipped_point and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    paths[neighbor] = curr_point
        final_path = []
        current: tuple[int, int] | None = end
        while current is not None:
            final_path.append(current)
            current = paths[current]

        final_path = final_path[::-1]

        self.direction_string = ""
        for i in range(len(final_path) - 1):
            curr_x, curr_y = final_path[i]
            next_x, next_y = final_path[i + 1]
            dx = next_x - curr_x
            dy = next_y - curr_y

            if dy == -1:
                self.direction_string += "N"
            elif dy == 1:
                self.direction_string += "S"
            elif dx == 1:
                self.direction_string += "E"
            elif dx == -1:
                self.direction_string += "W"

        return self.direction_string

    def draw_maze(self, show_hide: bool, color: int) -> None:
        """
        Renders the maze visually in the terminal using ASCII characters.

        Draws the generated walls, the entry/exit points,
          and optionally the shortest path
        using terminal color codes.

        Args:
            show_hide (bool): Flag indicating whether to
              show (True) or hide (False) the solution path.
            color (int): An integer representing the color
              theme choice for the maze rendering.

        Returns:
            None
        """
        WHITE = '\033[37m'
        RED = '\033[91m'
        GREEN = '\033[92m'
        BLUE = '\033[94m'
        WELLOW = '\033[93m'
        MAGENTA = '\033[95m'
        CYAN = '\033[96m'
        RESET = '\033[0m'
        if color == 0:
            c = WHITE
            w = GREEN
        elif color == 1:
            c = RED
            w = WELLOW
        elif color == 2:
            c = GREEN
            w = MAGENTA
        elif color == 3:
            c = BLUE
            w = CYAN
        scale_x = 8
        scale_y = 5
        self.seed = True
        room_width = ((scale_x - 1) * self.width) + 1
        room_hight = ((scale_y - 1) * self.height) + 1

        empty = [[" " for _ in range(room_width)] for _ in range(room_hight)]
        curr_x = self.entry_x
        curr_y = self.entry_y
        for logical_y in range(self.height):
            for logical_x in range(self.width):
                vis_y = logical_y * (scale_y - 1)
                vis_x = logical_x * (scale_x - 1)
                # North Wall (1)
                if self.arr[logical_y][logical_x] & 1:
                    for i in range(scale_x):
                        empty[vis_y][vis_x + i] = c + "-" + RESET
                    empty[vis_y][vis_x + (scale_x - 1)] = c + "+" + RESET
                    empty[vis_y][vis_x] = c + "+" + RESET

                # East Wall (2)
                if self.arr[logical_y][logical_x] & 2:
                    for i in range(scale_y):
                        empty[vis_y + i][vis_x + (
                            scale_x - 1)] = c + "|" + RESET
                    empty[vis_y + (scale_y - 1)][vis_x + (
                        scale_x - 1)] = c + "+" + RESET
                    empty[vis_y][vis_x + (
                        scale_x - 1)] = c + "+" + RESET

                # South Wall (4)
                if self.arr[logical_y][logical_x] & 4:
                    for i in range(scale_x):
                        empty[vis_y + (
                            scale_y - 1)][vis_x + i] = c + "-" + RESET
                    empty[vis_y + (scale_y - 1)][vis_x + (
                        scale_x - 1)] = c + "+" + RESET
                    empty[vis_y + (scale_y - 1)][vis_x] = c + "+" + RESET

                # West Wall (8)
                if self.arr[logical_y][logical_x] & 8:
                    for i in range(scale_y):
                        empty[vis_y + i][vis_x] = c + "|" + RESET
                    empty[vis_y + (scale_y - 1)][vis_x] = c + "+" + RESET
                    empty[vis_y][vis_x] = c + "+" + RESET
        if show_hide:
            for direction in self.direction_string:
                vis_x = curr_x * (scale_x - 1)
                vis_y = curr_y * (scale_y - 1)
                if direction == "N":
                    curr_y -= 1
                    empty[vis_y + scale_y // 2][
                        vis_x + scale_x // 2] = w + "o" + RESET
                elif direction == "S":
                    curr_y += 1
                    empty[vis_y + scale_y // 2][
                        vis_x + scale_x // 2] = w + "o" + RESET
                elif direction == "E":
                    curr_x += 1
                    empty[vis_y + scale_y // 2][
                        vis_x + scale_x // 2] = w + "o" + RESET
                elif direction == "W":
                    curr_x -= 1
                    empty[vis_y + scale_y // 2][
                        vis_x + scale_x // 2] = w + "o" + RESET
            empty[(
                self.entry_y * (scale_y - 1)) + scale_y // 2][(
                    self.entry_x * (
                        scale_x - 1)) + scale_x // 2] = RED + "S" + RESET
            empty[(
                self.exit_y * (scale_y - 1)) + scale_y // 2][(
                    self.exit_x * (
                        scale_x - 1)) + scale_x // 2] = GREEN + "E" + RESET
        for row in empty:
            print("".join(row))
