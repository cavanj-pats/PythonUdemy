#backtracking_NQueens.py


n = 4  # should be able to change this
board = [-1] * n  # a list of size n filled with -1 
solution = list()

# Lookup sets for O(1) safety checks
cols = set()
pos_diag = set()  # stores (row + col)
neg_diag = set()  # stores (row - col)

"""
Queens attack diagonally along two types of lines: positive-sloping diagonals 
(bottom-left to top-right) and negative-sloping diagonals (top-left to bottom-right).

this is an identifier for the diagonal.  if it is in the set, the queen
can be attacked by the queen already placed on the board.

neg_diag = row-col
pos_diag = row + col

"""

def is_safe(row, col):
    """Returns True if a queen can be placed at (row, col)."""
    if col in cols:
        return False
    if (row + col) in pos_diag:
        return False
    if (row - col) in neg_diag:
        return False
    return True

def place_queen(row, col):
    """Registers a queen on the board and updates tracking structures."""
    board[row] = col
    cols.add(col)
    pos_diag.add(row + col)
    neg_diag.add(row - col)

def remove_queen(row, col):
    """Backtracks by removing a queen and clearing tracking structures."""
    board[row] = -1
    cols.remove(col)
    pos_diag.remove(row + col)
    neg_diag.remove(row - col)


def backtrack(row):
    if row == n:
        solution.append(board.copy())
        return

    for c in range(n):
        #print(row, c, cols, pos_diag, neg_diag)
        if is_safe(row,c):
            place_queen(row, c)
            backtrack(row+1)
            remove_queen(row, c)  #popping or removing the solution is part of backtracking

def print_board(solution):
    n = len(solution)
    print("\n" + "—" * (n * 2 + 1))  # Top border divider
    for col_index in solution:
        # Create a list of dots for the row
        row_str = ["."] * n
        # Place the Queen at the correct column index
        row_str[col_index] = "Q"
        # Join with spaces for better readability in the terminal
        print("| " + " ".join(row_str) + " |")
    print("—" * (n * 2 + 1))  # Bottom border divider

        
        

backtrack(0)

for i, single_sol in enumerate(solution):
    print(f"\nSolution {i + 1}:")      
    print_board(single_sol)


#if __name__ == "__main__":