# Sudoku solver
# Solve sudoku using backtracking and recursions
# A sudoku puzzle here is a list of lists, where the inner list is a row
# Each list of list element is as such a cell in the sudoku puzzle
# Each blank space is represented using -1

SIZE = 9
BLANK_CELL = -1

def main():
    # Sudoku input
    puzzle = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    
    solve_sudoku(puzzle)
    print(puzzle)


def solve_sudoku(puzzle):
    # 1. Finding a cell in the puzzle to make a guess in
    row, col = next_empty(puzzle)

    # 2. If no more spaces are left in the puzzle (base case)
    if row is None:
        return True
    
    # 3. Giving the empty cell a value
    for value in range(1, 10):
        if check_fit(puzzle, value, row, col) == True:
            puzzle[row][col] = value
            
            # 4. If the base case is reached and we have solved the soduku
            if solve_sudoku(puzzle) == True:
                return True

        # 5. Resetting the cell if no solution for it was found to try again by backtracing
        puzzle[row][col] = BLANK_CELL

    # 6. If no solution could be reached until the end
    return False


def next_empty(puzzle):
    # Returning the next empty cell
    for row_index in range(9):
        for col_index in range(9):
            if puzzle[row_index][col_index] == BLANK_CELL:
                return row_index, col_index
            
    # If no empty cell found
    return None, None


def check_fit(puzzle, value, row, col):
    if value in puzzle[row]:
        return False

    for i in range(9):
        if value == puzzle[i][col]:
            return False
        
    row_begin = (row // 3) * 3
    col_begin = (col // 3) * 3

    for i in range(row_begin, row_begin + 3):
        for j in range(col_begin, col_begin + 3):
            if value == puzzle[i][j]:
                return False 

    return True


if __name__ == "__main__":
    main()
