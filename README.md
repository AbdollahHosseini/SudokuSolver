# Sudoku Solver
This project models the Sudoku puzzle as a Constraint Satisfaction Problem (CSP). Empty cells are treated as variables, with their possible values constrained by the rules of Sudoku. The solver implements a Minimum Remaining Value (MRV) heuristic and forward checking to ensure efficient backtracking and faster solutions.

Key features include:

valid_values function: Ensures a value adheres to Sudoku rules for a given row, column, and grid.
Dynamic domain reduction: The update_cells function dynamically updates the possible values for related cells, pruning invalid paths.
Priority queue: Cells with the fewest options are prioritized for solving, minimizing unnecessary recursion.

Recursive solver (csp_solve): Processes the grid starting with the most constrained cells, returning a solution if one exists or a grid of -1 values if none is possible.
This optimized algorithm can solve most Sudoku puzzles in under 0.1 seconds.

Future improvements could include constraint propagation to further reduce search space by propagating constraints across related cells, improving efficiency.
