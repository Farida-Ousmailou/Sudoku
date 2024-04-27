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

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True 

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0 
    return False


def find_empty_cell(grid):

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i,j)
    return None

def is_valid(grid, row, col, num):

    for i in range(9):
        if grid[row][i] == num:
            return False