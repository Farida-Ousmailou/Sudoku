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
    
    for i in range(9):
        if grid[i][col] == num:
            return False

    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True


def print_sudoku_grid(grid, current_row, current_col):
    # os.system('cls' if os.name == 'nt' else 'clear') 
    print("  - - - - - - - - - - - - ")
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print(
                " | - - - - - - - - - - - |") 

        row_str = [str(num) if num != 0 else '.' for num in row]
        formatted_row = '|'.join(''.join(row_str[j:j + 3]) for j in range(0, 9, 3))

       
        row_marker = '>' if i == current_row else ' '

        print(f"{row_marker}| {' '.join(formatted_row)} |")

    
    col_marker = ' ' * (2 * current_col + 3) + '^'
    print(f"{col_marker}")

    print("  - - - - - - - - - - - - ")
    print(f"Position actuelle : ({current_row}, {current_col})")