# A-Maze-ing

*This activity has been created as part of the 42 curriculum by eabushak.*

## Description
A-Maze-ing is a Python-based maze generator and visualizer. The program reads configuration parameters from a file to generate either a perfect maze (a single valid path) or a playable board (an imperfect maze with loops and multiple routes). It ensures the maze contains a visually distinct "42" pattern in its center, saves the structural output in a specific hexadecimal format, and provides an interactive terminal ASCII rendering for users to view the maze and its shortest solution path.

## Instructions
### Prerequisites
- Python 3.10 or later.
- Make (for running automation commands).

### Installation & Execution
A `Makefile` is provided to automate standard tasks:
- **Install dependencies:** `make install`
- **Run the program:** `make run` (Alternatively: `python3 a_maze_ing.py config.txt`)
- **Lint the code:** `make lint` (Runs flake8 and mypy)
- **Clean cache/artifacts:** `make clean`
- **Debug mode:** `make debug`

## Configuration File Format
The generator requires a configuration file passed as an argument. The file uses a `KEY=VALUE` format, one pair per line (lines starting with `#` are ignored). 

**Mandatory Keys:**
- `WIDTH`: Maze width (number of cells)
- `HEIGHT`: Maze height
- `ENTRY`: Entry coordinates (x,y)
- `EXIT`: Exit coordinates (x,y)
- `OUTPUT_FILE`: Output filename (e.g., `maze.txt`)
- `PERFECT`: Boolean flag (`True` for a perfect maze, `False` for an imperfect playable board)

## Maze Generation Algorithm
1. **Generation (Perfect Maze):** The core generation relies on a **Randomized Depth-First Search (Backtracking)** algorithm. It starts with a grid fully populated with walls and iteratively carves paths by breaking down walls between neighboring cells using bitwise operations, backtracking only when it hits a dead end. The algorithm explicitly skips the coordinates that make up the "42" pattern.
2. **Modification (Imperfect Maze):** If the `PERFECT` flag is `False`, a custom wall-removal algorithm is applied over the generated perfect maze to strategically knock down additional walls, creating loops and eliminating dead-ends to make it suitable for a Pac-Man-like playable board.
3. **Pathfinding:** The shortest path between the entry and exit points is calculated using **Breadth-First Search (BFS)**, guaranteeing the most direct route is found and visually rendered.

## Why These Algorithms?
- **DFS (Backtracking):** Chosen for its efficiency in generating highly winding, complex perfect mazes with long corridors. It is relatively straightforward to implement using a stack and makes it simple to carve around reserved spaces (like the "42" pattern).
- **BFS:** Chosen for the solver because it is mathematically guaranteed to find the shortest path in an unweighted grid, which is required by the subject for the solution string and visual display.

## Code Reusability
The maze generation logic is entirely decoupled from the CLI and display logic. It is encapsulated within the `MazeGenerator` class in a standalone module. 

**How to reuse the package:**
1. Build the package from the root of this repository.
2. Install it via pip: `pip install mazegen-1.0.0-py3-none-any.whl` (or the `.tar.gz` equivalent).
3. Import and use it in your Python projects:

```python
from MazeGenerator import MazeGenerator

# Initialize the generator
maze = MazeGenerator(width=20, height=15, is_perfect=True, entry_x=0, entry_y=0, exit_x=19, exit_y=14)

# Generate the maze structure
maze_grid = maze.back_trackinga_agorithm()

# Find the shortest path
solution = maze.solve_maze_bfs()