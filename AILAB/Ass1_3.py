# Python code for solving the N-Queens problem using backtracking algorithm

def is_valid(board, row, col, n):
    """
    This function checks if it is valid to place a queen at the given row and column
    on the board of size n.

    Args:
    board (list): A list of lists representing the chess board.
    row (int): The row number to check.
    col (int): The column number to check.
    n (int): The size of the board.

    Returns:
    bool: True if it is valid to place a queen at the given row and column, False otherwise.
    """
    # check if the same row already has a queen
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n):
    """
    This function recursively places queens on the board until all queens have been placed
    or no valid placement is possible.

    Args:
    board (list): A list of lists representing the chess board.
    col (int): The current column number.
    n (int): The size of the board.

    Returns:
    bool: True if all queens have been placed, False otherwise.
    """
    # base case: all queens have been placed
    if col == n:
        return True

    # consider all rows in the current column
    for row in range(n):
        # check if the queen can be placed in this row and column
        if is_valid(board, row, col, n):
            # place the queen in this row and column
            board[row][col] = 1

            # recursively place the rest of the queens
            if solve_n_queens(board, col+1, n):
                return True

            # backtrack and remove the queen from this position
            board[row][col] = 0

    # if no valid placement was found in this column, backtrack
    return False


def n_queens(n):
    """
    This function initializes the board and calls the solve_n_queens function to solve
    the N-Queens problem for the given board size.

    Args:
    n (int): The size of the board.
    """
    board = [[0 for x in range(n)] for y in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists for n = {}".format(n))
    else:
        for row in board:
            print(row)


def main():
    """
    This function takes user input for the board size and calls the n_queens function
    to solve the N-Queens problem for the given board size.
    """
    n = int(input("Enter the value of n: "))
    n_queens(n)


if __name__ == '__main__':
    main()