import sys
from src.MazeGenerator import MazeGenerator


def parse_config(file_path: str) -> dict[str, str]:
    """Reads the configuration file and returns a dictionary of arguments."""
    argument = {}
    mandatory = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]

    with open(file_path, 'r') as text_file:
        for line in text_file:
            if line.startswith("#") or line.strip() == "":
                continue

            data = line.split("=")
            argument[data[0].strip()] = data[1].strip()

    for item in mandatory:
        if item not in argument:
            print(f"CRITICAL ERROR: missing required_item={item}")
            sys.exit(1)
    return argument


def validate_arguments(
        argument: dict[str, str]
        ) -> tuple[int, int, bool, int, int, int, int]:
    """Validates the parsed arguments and ensures
    they are the correct data types/bounds """
    if_error = False
    list_ranges: list[str] = []

    width = height = entry_x = entry_y = exit_x = exit_y = 0
    is_perfect = False

    try:
        width = int(argument["WIDTH"])
        height = int(argument["HEIGHT"])
    except ValueError:
        if_error = True
        print("width and height must be int values")
    try:
        if width < 3 or height < 3:
            raise ValueError("width and hight must be < 3")
    except ValueError as e:
        list_ranges.append(str(e))
    try:
        perfect_val = argument["PERFECT"].lower()
        if perfect_val not in ("true", "false"):
            raise ValueError
        is_perfect = (perfect_val == "true")
    except ValueError:
        if_error = True
        print("PERFECT must be 'True/ture' or 'False/false'")

    try:
        entry = argument["ENTRY"].split(",")
        exit_pts = argument["EXIT"].split(",")
        entry_x, entry_y = int(entry[0]), int(entry[1])
        exit_x, exit_y = int(exit_pts[0]), int(exit_pts[1])
    except (ValueError, IndexError):
        if_error = True
        print("ENTRY and EXIT point must be x,y int values")

    if not if_error:
        if entry_x >= width or entry_x < 0:
            list_ranges.append("ENTRY_X out of range")
        if exit_x >= width or exit_x < 0:
            list_ranges.append("EXIT_X out of range")
        if entry_y >= height or entry_y < 0:
            list_ranges.append("ENTRY_Y out of range")
        if exit_y >= height or exit_y < 0:
            list_ranges.append("EXIT_Y out of range")

    if list_ranges:
        for error in list_ranges:
            print(error)
        if_error = True

    if if_error:
        sys.exit(1)

    return width, height, is_perfect, entry_x, entry_y, exit_x, exit_y


def main() -> None:
    if len(sys.argv) < 2:
        print("missing config file")
        sys.exit(1)

    config_file = sys.argv[1]
    argument = parse_config(config_file)
    (width, height, is_perfect, entry_x,
        entry_y, exit_x, exit_y) = validate_arguments(argument)

    generatemaze = MazeGenerator(
        width, height,
        is_perfect,
        entry_x, entry_y,
        exit_x, exit_y
    )

    draw = False
    first_try = True
    color = 0

    while True:
        print("*===* A-Maze-ing *===*")
        print("1. Generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate the maze color")
        print("4. Quit")

        try:
            choice = input("Choice? (1-4) -> \
Chose 1 first to generate the maze: \n")
            num = int(choice)
        except ValueError:
            print("##############################")
            print("# Enter a number between 1-4 #")
            print("##############################")
            continue
        except KeyboardInterrupt:
            print("############################################")
            print("# [!] Ctrl+C detected. Shutting down safely #")
            print("#############################################")
            sys.exit(0)
        except Exception as e:
            print(f"unxpected error: {e}")
            sys.exit(1)
        if first_try and num != 1:
            print("\n === Please chose one for the first time === \n")
            continue
        if num == 1:
            first_try = False
            arr_numbers = generatemaze.back_trackinga_agorithm()
            if not is_perfect:
                arr_numbers = generatemaze.imperfect()
            direction = generatemaze.solve_maze_bfs()
            generatemaze.draw_maze(False, color)
            # Write results to the output file
            output_file_path = argument["OUTPUT_FILE"]
            with open(output_file_path, "w") as output:
                for row in arr_numbers:
                    # Convert to hex strings directly
                    line_chars = [str(hex(n))[2:] for n in row]
                    output.write("".join(line_chars) + "\n")
                output.write("\n" + argument["ENTRY"] + "\n")
                output.write(argument["EXIT"] + "\n")
                output.write(direction + "\n")

        elif num == 2:
            draw = not draw
            generatemaze.draw_maze(draw, color)

        elif num == 3:
            color += 1
            if color == 4:
                color = 0
            generatemaze.draw_maze(draw, color)

        elif num == 4:
            break


if __name__ == "__main__":
    main()
