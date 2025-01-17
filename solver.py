from heapq import heappush, heappop
import numpy as np

def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """

    if not valid_sudoku(sudoku):
        return np.full((9, 9), -1)

    
    all_empty_cells = compute_empty_cells(sudoku)
    solution = csp_solve(sudoku, all_empty_cells)

    if solution is not None:
        return solution
    else: return np.full((9, 9), -1)



def csp_solve(sudoku, empty_cells):
    if not empty_cells:
        return sudoku # No empty cells to solve
    
    len_options, row, col, options = heappop(empty_cells) # returns item with least options
    
    for option in options:

        sudoku[row, col] = option
        new_empty_cells = update_cells(empty_cells, row, col, option)

        if new_empty_cells is not None:
            result = csp_solve(sudoku, new_empty_cells)
            if result is not None:
                return result
        
        sudoku[row, col] = 0 # Backtracking

    return None

def update_cells(curr_empty_cells, curr_row, curr_col, curr_option):
    updated_cells = []
    for len_options, row, col, options in curr_empty_cells:
        if curr_row == row or curr_col == col or (curr_row // 3 == row // 3 and curr_col // 3 == col // 3):
            new_options = [option for option in options if option != curr_option]
            if not new_options:
                return None # Coordinate that is an empty cell has no other options thus abort recursion as no value can be assigned here
            heappush(updated_cells, (len(new_options), row, col, new_options))

        else:
            heappush(updated_cells, (len_options, row, col, options))

    return updated_cells


def valid_values(sudoku, row, col):
    row_values = sudoku[row, :]
    column_values = sudoku[:, col]
    grid_values = sudoku[(row//3) * 3: ((row // 3) * 3) + 3, (col // 3) * 3 : ((col // 3 ) * 3) + 3]
    used = set(np.concatenate((row_values, column_values, grid_values.flatten()))) # set is used to remove redundant numbers, less iteration required in the line below
    return [num for num in range(1, 10) if num not in used]


def valid_sudoku(sudoku):
    for i in range(9):
        if not is_unique(sudoku[i, :]) or not is_unique(sudoku[:, i]): # Checks each row and column independently
            return False

    index_arr = [0, 3, 6] 
    for row in index_arr:
        for col in index_arr:
            if not is_unique(sudoku[row : row + 3, col : col + 3].flatten()):
                return False
    return True

def is_unique(check_list):
    check_list = [num for num in check_list if num != 0]
    return len(check_list) == len(set(check_list))

def compute_empty_cells(sudoku):
    empty_cells = []
    for row in range(9):
        for col in range(9):
            if sudoku[row, col] == 0:
                options = valid_values(sudoku, row, col)
                heappush(empty_cells, (len(options), row, col, options))
    return empty_cells










