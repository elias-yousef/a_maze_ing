# A-Maze-ing

*This activity has been created as part of the 42 curriculum by eabushak, aabuzanh.*

## Description
This project is a maze generator implemented in Python that takes a configuration file to generate a maze. It is capable of generating both "perfect" mazes—which contain exactly one unique path between the entry and exit—and "imperfect" playable boards with loops and no dead-ends, akin to a Pac-Man level. The program writes the maze data to an output file using hexadecimal wall representation and provides an interactive visual rendering of the maze and its solution path.

## Instructions
A `Makefile` is included to automate common tasks. 
*   **Installation:** Run `make install` to install dependencies.
*   **Execution:** Run `python3 a_maze_ing.py config.txt` (or replace `config.txt` with your chosen configuration file name) to launch the generator.
*   **Debugging:** Run `make debug` to execute the script in debug mode.
*   **Linting:** Run `make lint` to check the code against `flake8` and `mypy` standards.
*   **Cleanup:** Run `make clean` to remove temporary files or caches.

## Configuration File Format
The program requires a configuration file containing one `KEY=VALUE` pair per line. Lines starting with `#` are treated as comments and ignored. The mandatory keys are:
*   **`WIDTH`**: Maze width (number of cells).
*   **`HEIGHT`**: Maze height.
*   **`ENTRY`**: Entry coordinates (x,y).
*   **`EXIT`**: Exit coordinates (x,y).
*   **`OUTPUT_FILE`**: Output filename.
*   **`PERFECT`**: Is the maze perfect?.

## Maze Generation Algorithm
*   **Algorithm Used:** Randomized Depth-First Search (Recursive Backtracker) for generation, and Breadth-First Search (BFS) for the solution pathfinding. 
*   **Why we chose it:** The recursive backtracker efficiently carves deep, winding corridors, making it ideal for generating challenging perfect mazes. For the imperfect maze mode, we implemented a custom algorithm that systematically hunts down dead-ends using bitwise operations, opening them up to create a cohesive, looped board without violating the maximum room-size constraints.

## Code Reusability
The core maze generation logic has been implemented as a standalone, reusable class inside the `mazegen` package. 
*   **Installation:** The package is provided as a `mazegen-*.whl` file at the root of the repository. You can install it via pip: `pip install ./mazegen-1.0.0-py3-none-any.whl`.
*   **Usage:** Once installed, you can import and instantiate it in any Python script:
    ```python
    from mazegen.MazeGenerator import MazeGenerator
    
    # Example instantiation
    maze = MazeGenerator(width=20, height=15, is_perfect=True, entry_x=0, entry_y=0, exit_x=19, exit_y=14)
    grid = maze.back_trackinga_agorithm() # Access generated structure
    ```

## Team and Project Management
*   **Roles:** 
    *   **eabushak:** Developed the core `MazeGenerator` class, the maze generation algorithms, and the main `a_maze_ing.py` execution script.
    *   **aabuzanh:** Handled everything else, including parsing the configuration file, formatting the output file, creating the `Makefile`, building the reusable `.whl` package, and writing the documentation.
*   **Planning:** We divided the tasks clearly from the beginning based on the required files and modules. We anticipated that splitting the core generation logic from the peripheral requirements (configuration, output formatting, packaging) would allow us to work in parallel efficiently.
*   **What worked well / Could be improved:** The clear separation of concerns worked very well and allowed for independent progress. However, combining the core generator with the output formatting and packaging requirements took extra coordination at the end. We could improve by integrating our modules earlier in the development process to catch integration issues sooner.
*   **Specific Tools Used:** Python 3, Visual Studio Code, Git, GitHub, Make, flake8, mypy.

## Resources
*   **References:** Wikipedia references on Maze generation algorithms and Breadth-first search; Python documentation for the `typing` and `collections` modules.
*   **AI Usage:** AI was utilized as an interactive assistant to help troubleshoot `mypy` module import errors related to Python's `src/` directory package structure, refine the bitwise logic for removing dead-ends while respecting room-size limits, and clarify `.whl` packaging deployment steps. All AI-assisted logic was thoroughly peer-reviewed to ensure full comprehension before integration.