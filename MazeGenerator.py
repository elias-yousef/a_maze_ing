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
    
    def first_generate_maze(self) -> None:
            arr = [["F" for i in range(self.width)] for j in range(self.height)]
            self.arr = arr
            arr_string = ""
            for item in arr:
                for hx in item:
                    arr_string += hx
                arr_string += "\n"



test = MazeGenerator(5, 5, True, 0, 0, 5, 5)
test.first_generate_maze()