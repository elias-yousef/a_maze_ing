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


    def back_trackinga_agorithm(self) -> list[int]: #width and height index error fix it
        direction = {"N": 1, "E": 8, "S": 4, "W": 2}
        self.arr = [[15 for i in range(self.width)] for j in range(self.height)]
        print(self.arr)
        self.num_cells = self.width * self.height
        self.visited_cells = []
        self.visited_cells.append(((random.randint(0, self.width - 1), ((random.randint(0, self.height - 1))))))
        print(self.visited_cells)
        while self.visited_cells:
            self.next_cell = []
            x, y = self.visited_cells[-1]
            if x >= 1:
                if self.arr[y][x - 1] == 15:
                    self.next_cell.append(((x - 1), y))
            if x < self.width - 1:
                if self.arr[y][x + 1] == 15:
                    self.next_cell.append(((x + 1), y))
            if y >= 1:
                if self.arr[y - 1][x] == 15:
                    self.next_cell.append((x, (y - 1)))
            if y < self.height - 1:
                if self.arr[y + 1][x] == 15:
                    self.next_cell.append((x, (y + 1)))
            if self.next_cell:
                chosen = random.choice(self.next_cell)
                x1, y1 = chosen
                x, y = self.visited_cells[-1]
                val = ((x - x1) , (y - y1))
                print(val)
                if val == (1, 0):
                    self.arr[y][x] -= 2
                    self.arr[y1][x1] -= 8
                elif val == (-1, 0):
                    self.arr[y][x] -= 8
                    self.arr[y1][x1] -= 2
                elif val == (0, 1):
                    self.arr[y][x] -= 1
                    self.arr[y1][x1] -= 4
                elif val == (0, -1):
                    self.arr[y][x] -= 4
                    self.arr[y1][x1] -= 1
                self.visited_cells.append(chosen)
            else:
                self.visited_cells.pop()
        self.arr[self.entry_y][self.entry_x] -= 2
        self.arr[self.exit_y][self.exit_x]  -= 8
        print(self.arr)
        return self.arr
    
    def imperfect(self) -> list[int]:
        x = 1
        y = 1
        length = (self.width * self.height) - (self.height * 2 - 2) - (self.width * 2 - 2) # fix this later i think it works
        while length > 0:
            if (( #delete from S -> N
                (self.arr[y - 1][x + 1] & 4) == 4 or (
                    self.arr[y - 1][x + 1] & 2) == 2 or (
                        self.arr[y][x + 1] & 2) == 2) and (
                            (self.arr[y - 1][x - 1] & 8) == 8 or (
                                self.arr[y - 1][x - 1] & 4) == 4 or (
                                    self.arr[y][x - 1] & 8) == 8) and (
                                        (self.arr[y][x] & 1) == 1
                                    )
                    ):
                if random.random() < 0.3:
                    self.arr[y][x] -= 1
                    self.arr[y - 1][x] -= 4
            if (( #delete from N -> S
                (self.arr[y + 1][x + 1] & 2) == 2 or (
                    self.arr[y + 1][x + 1] & 1) == 1 or (
                        self.arr[y][x + 1] & 2) == 2) and (
                            (self.arr[y + 1][x - 1] & 8) == 8 or (
                                self.arr[y - 1][x - 1] & 1) == 1 or (
                                    self.arr[y][x - 1] & 8) == 8) and (
                                        (self.arr[y][x] & 4) == 4
                                    )
                    ):
                if random.random() < 0.3:
                    self.arr[y][x] -= 4
                    self.arr[y + 1][x] -= 1
            if (( # delete from W -> E
                (self.arr[y - 1][x + 1] & 2) == 2 or (
                    self.arr[y - 1][x + 1] & 4) == 4 or (
                        self.arr[y - 1][x] & 4) == 4) and (
                            (self.arr[y + 1][x + 1] & 1) == 1 or (
                                self.arr[y + 1][x + 1] & 2) == 2 or (
                                    self.arr[y + 1][x] & 1) == 1) and (
                                        (self.arr[y][x] & 8) == 8
                                    )
                    ):
                if random.random() < 0.3:
                    self.arr[y][x] -= 8
                    self.arr[y][x + 1] -= 2
            if (( # delete from E -> W
                (self.arr[y - 1][x - 1] & 8) == 8 or (
                    self.arr[y - 1][x - 1] & 4) == 4 or (
                        self.arr[y - 1][x] & 4) == 4) and (
                            (self.arr[y + 1][x - 1] & 1) == 1 or (
                                self.arr[y + 1][x - 1] & 8) == 8 or (
                                    self.arr[y + 1][x] & 1) == 1) and (
                                        (self.arr[y][x] & 2) == 2
                                    )
                    ):
                if random.random() < 0.3:
                    self.arr[y][x] -= 2
                    self.arr[y][x - 1] -= 8
            x += 1
            if x == self.width - 1:
                y += 1
                x = 1
            length -= 1
        return self.arr


            


