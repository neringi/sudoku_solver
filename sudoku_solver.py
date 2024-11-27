# # # # # # # SUDOKU SOLVER

# # # # # # # Backtracking method


n = 9  # Size of the grid (9x9)

# Print the grid
def print_sudoku(arr):
    for i in range(n):
        for j in range(n):
            # Print the numbers with vertical separators
            print(arr[i][j] if arr[i][j] != 0 else '.', end=" ")
            if (j + 1) % 3 == 0 and j != n - 1:  
                print("|", end=" ")
        print()  
        
        # Print a horizontal line to separate boxes
        if (i + 1) % 3 == 0 and i != n - 1:
            print("-" * 21)  



def available(input, row, col):

    impossible_values = []

    # Check row (same row)
    impossible_values.extend([value for value in input[row] if value != 0])

    # Check column (same column)
    impossible_values.extend([input[x][col] for x in range(len(input)) if input[x][col] != 0])

    # Check 3x3 grid (subgrid)
    grid_row = row // 3  # Find the row index of the 3x3 grid
    grid_col = col // 3  # Find the column index of the 3x3 grid

    # Print grid row and column
    # print(f"Checking 3x3 grid for ({row}, {col}) - grid_row: {grid_row}, grid_col: {grid_col}")
    
    # Iterate through the 3x3 grid, ensuring we stay within bounds
    for row in range(grid_row * 3, grid_row * 3 + 3):  # Iterate over 3 rows
        # print("row: ", row)
        for col in range(grid_col * 3, grid_col * 3 + 3):  # Iterate over 3 columns
            # print("column: ", col)
            # Ensure the row and col are within valid bounds of the grid (0 to 8)
            if 0 <= row < 9 and 0 <= col < 9:
                # print(f"  Checking cell ({row}, {col})")
                if input[row][col] != 0:
                    impossible_values.append(input[row][col])
            else:
                print(f"  Out of bounds: ({row}, {col})")

    # Deduplicate the impossible values list
    impossible_values = list(set(impossible_values))

    print(f"Impossible values for ({row}, {col}):", impossible_values)

    # Determine possible values (1 through 9 not in impossible_values)
    possible_values = [value for value in range(1, 10) if value not in impossible_values]

    print(f"Possible values for cell ({row}, {col}): {possible_values}")
    return possible_values        


def is_unique(nums):
    nums = [num for num in nums if num != 0]  # Remove zeros
    return len(nums) == len(set(nums))  # Check if all non-zero numbers are unique



# # Check that a sudoku is valid by:
# * being a 9x9 grid 
# * numbers 0-9 
# * does not duplicate numbers in row, column or subgrid/box

def is_valid_sudoku(arr):
    # Check 9x9 grid
    if len(arr) != 9 or any(len(row) != 9 for row in arr):
        print('The grid is not 9x9!')
        return False

    # Check values within range (0-9)
    for row in arr:
        for num in row:
            if num < 0 or num > 9:  # Invalid number found
                return False

    # Check row dupes  
    for row in arr:
        if not is_unique(row):
            print("Duplicates in a row found")
            return False

    # Check column dupes
    for col in range(9):
        column = [arr[row][col] for row in range(9)]
        if not is_unique(column):
            print("Duplicates in a column found")
            return False
        
    # Check each 3x3 subgrid/box dupes
    for i in range(0, 9, 3):  
        for j in range(0, 9, 3): 
            subgrid = [arr[i + k][j + l] for k in range(3) for l in range(3)]
            if not is_unique(subgrid):
                return False
    # return print("Sudoku is valid")
    
def empty_cell(input):
    for i in range(len(input)):
        for j in range(len(input)):
            if input[i][j] == 0:
                return (i, j)
            
def brute_solve(input, row=0, col=0):

    find = empty_cell(input)

    if not find:
        return True
    else:
        row, col = find
    
    possible_values = available(input, row, col)

    for val in possible_values:
        input[row][col] = val

        if brute_solve(input):
            return True
        
        input[row][col] = 0

    return False





# available(input)


# TESTING IT OUT

example_input = [
         [5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]
         ]

input = example_input

print_sudoku(input)

is_valid_sudoku(input)

brute_solve(input)

print_sudoku(input)