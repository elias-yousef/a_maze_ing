import numpy as np
import random
import sys

class MazeGenerator():
    def __init__(
            self, width: int, height: int, is_perfect: bool,
            entry_x: int, entry_y: int, exit_x: int,
            exit_y: int
            ) -> None:
        self.width = width
        self.height = height
        self.is_perfect = is_perfect
        self.entry_x = entry_x
        self.entry_y = entry_y
        self.exit_x = exit_x
        self.exit_y = exit_y


    def back_trackinga_agorithm(self):
        direction = {"N": 1, "E": 8, "S": 4, "W": 2}

        self.arr = [[15 for i in range(self.width)] for j in range(self.height)]
        print(self.arr)
        self.num_cells = self.width * self.height
        self.visited_cells = []
        self.first_cell = (self.entry_x, self.entry_y)
        self.dist_cell = (self.exit_x, self.exit_y)
        self.visited_cells.append(((random.randint(0, self.width - 1), ((random.randint(0, self.height - 1))))))
        print(self.visited_cells)
        while self.visited_cells:
            self.next_cell = []
            current_x, current_y = self.visited_cells[-1]
            if current_x >= 1:
                if self.arr[current_y][current_x - 1] == 15:
                    self.next_cell.append(((current_x - 1), current_y))
            if current_x < self.width - 1:
                if self.arr[current_y][current_x + 1] == 15:
                    self.next_cell.append(((current_x + 1), current_y))
            if current_y >= 1:
                if self.arr[current_y - 1][current_x] == 15:
                    self.next_cell.append((current_x, (current_y - 1)))
            if current_y < self.height - 1:
                if self.arr[current_y + 1][current_x] == 15:
                    self.next_cell.append((current_x, (current_y + 1)))
            if self.next_cell:
                chosen = random.choice(self.next_cell)
                x1, y1 = chosen
                x, y = self.visited_cells[-1]
                val = ((x - x1) , (y - y1))
                print(val)
                if val == (1, 0):
                    self.arr[y][x] -= 2
                    self.arr[y][x - 1] -= 8
                elif val == (-1, 0):
                    self.arr[y][x] -= 8
                    self.arr[y][x + 1] -= 2
                elif val == (0, 1):
                    self.arr[y][x] -= 1
                    self.arr[y - 1][x] -= 4
                elif val == (0, -1):
                    self.arr[y][x] -= 4
                    self.arr[y + 1][x] -= 1
                self.visited_cells.append(chosen)
            else:
                self.visited_cells.pop()


test = MazeGenerator(5, 5, True, 0, 0, 5, 5)
test.back_trackinga_agorithm()
