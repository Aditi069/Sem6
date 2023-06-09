# This code is a Python implementation of the Tic Tac Toe game using the MinMax algorithm.

# This function prints the current state of the board.
def ConstBoard(board):
    """
    This function prints the current state of the board.

    Args:
    board (list): A list representing the current state of the board.

    Returns:
    None
    """
    print("Current State Of Board : \n\n")
    for i in range(0, 9):
        if ((i > 0) and (i % 3) == 0):
            print("\n")
        if (board[i] == 0):
            print("- ", end=" ")
        if (board[i] == 1):
            print("O ", end=" ")
        if (board[i] == -1):
            print("X ", end=" ")
    print("\n\n")

# This function takes the user move as input and make the required changes on the board.
def User1Turn(board):
    """
    This function takes the user move as input and makes the required changes on the board.

    Args:
    board (list): A list representing the current state of the board.

    Returns:
    None
    """
    pos = input("Enter X's position from [1...9]: ")
    pos = int(pos)
    if (board[pos-1] != 0):
        print("Wrong Move!!!")
        exit(0)
    board[pos-1] = -1

# MinMax function.
def minimax(board, player):
    """
    This function implements the MinMax algorithm to determine the best move for the computer.

    Args:
    board (list): A list representing the current state of the board.
    player (int): The player whose turn it is. 1 for computer, -1 for user.

    Returns:
    value (int): The score of the best move for the computer.
    """
    x = analyzeboard(board)
    if (x != 0):
        return (x*player)
    pos = -1
    value = -2
    for i in range(0, 9):
        if (board[i] == 0):
            board[i] = player
            score = -minimax(board, (player*-1))
            if (score > value):
                value = score
                pos = i
            board[i] = 0

    if (pos == -1):
        return 0
    return value

# This function makes the computer's move using minmax algorithm.
def CompTurn(board):
    """
    This function makes the computer's move using the MinMax algorithm.

    Args:
    board (list): A list representing the current state of the board.

    Returns:
    None
    """
    pos = -1
    value = -2
    for i in range(0, 9):
        if (board[i] == 0):
            board[i] = 1
            score = -minimax(board, -1)
            board[i] = 0
            if (score > value):
                value = score
                pos = i

    board[pos] = 1

# This function is used to analyze a game.
def analyzeboard(board):
    """
    This function analyzes the current state of the board to determine if there is a winner.

    Args:
    board (list): A list representing the current state of the board.

    Returns:
    int: 1 if computer wins, -1 if user wins, 0 if no winner yet.
    """
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
          [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in range(0, 8):
        if (board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]]
    return 0

# Main Function.
def main():
    """
    This function is the main function that runs the Tic Tac Toe game.

    Args:
    None

    Returns:
    None
    """
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Computer : O Vs. You : X")
    player = input("Enter to play 1(st) or 2(nd) :")
    player = int(player)
    for i in range(0, 9):
        if (analyzeboard(board) != 0):
            break
        if ((i+player) % 2 == 0):
            CompTurn(board)
        else:
            ConstBoard(board)
            User1Turn(board)

    x = analyzeboard(board)
    if (x == 0):
        ConstBoard(board)
        print("Draw!!!")
    if (x == -1):
        ConstBoard(board)
        print("X Wins!!! Y Loose !!!")
    if (x == 1):
        ConstBoard(board)
        print("X Loose!!! O Wins !!!!")

# Call the main function to run the game.
main()