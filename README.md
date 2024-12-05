# Sudoku Solver (Backtracking and Recursion)

This Python program utilizes backtracking and recursion to solve Sudoku puzzles.

**How it Works:**

1. **Initialization:**
   - Takes a 9x9 Sudoku grid as input (represented as a list of lists).
   - Empty cells are represented by -1.

2. **Find Empty Cell:**
   - A helper function efficiently locates the next empty cell in the grid.

3. **Backtracking Algorithm:**
   - If no empty cells are found, the current grid is a valid solution, and the program returns True.
   - For each possible number (1-9):
      - Place the number in the empty cell.
      - Recursively call the solver to check if the updated grid is valid.
      - If the recursive call returns True, the current grid is solved, and the program returns True.
      - If the recursive call returns False, remove the number from the cell and try another number.
   - If no number leads to a valid solution, backtrack and try different numbers in previous empty cells.

4. **Validation:**
   - Checks if a number is valid in a specific cell by ensuring it doesn't violate Sudoku rules:
      - No duplicates in the same row.
      - No duplicates in the same column.
      - No duplicates in the same 3x3 subgrid.

**Usage:**

1. **Prepare Input:**
   - Create a 9x9 list of lists representing the Sudoku grid.
   - Use -1 to represent empty cells.

2. **Run the Program:**
   - Call the `solve_sudoku()` function with the input grid.

3. **Output:**
   - Sudoku grid solved, in place.


**Example:**

```python
grid = [
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
