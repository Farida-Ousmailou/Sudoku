import random

def generate_sudoku_grid():
    grid = [[0 for _ in range(9)] for _ in range(9)]  

    solve_sudoku(grid)

    for _ in range(9):  
        row_indices = list(range(9))
        col_indices = list(range(9))
        random.shuffle(row_indices)
        random.shuffle(col_indices)

        grid[row_indices[0]][_] = 0
        grid[_][col_indices[0]] = 0

    return grid
