# Python code for solving the 8-Puzzle Problem using A* algorithm

# Importing necessary libraries
from copy import deepcopy
from colorama import init

# Initializing colorama for colored output
init(autoreset=True)

class Puzzle:
    # Initializing the board and goal state
    board = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    startX = 0
    startY = 0
    queue = [] # Priority queue for storing the boards
    generatedBoards = [] # List for storing the generated boards

    def calcHeuristic(self, board):
        """
        This function calculates the heuristic value of the given board.

        Args:
        board (list): A 3x3 list representing the current state of the board.

        Returns:
        h (int): The heuristic value of the board.
        """
        h = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != self.goal[i][j]:
                    h = h + 1
        return h - 1

    def getValidMoves(self, board):
        """
        This function returns a list of valid moves that can be made from the current state of the board.

        Args:
        board (list): A 3x3 list representing the current state of the board.

        Returns:
        validMoves (list): A list of valid moves that can be made from the current state of the board.
        """
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    self.startX = j
                    self.startY = i
        position = [[0] * 2] * 4
        validMoves = []
        position[0] = [self.startX + 1, self.startY]
        position[1] = [self.startX - 1, self.startY]
        position[2] = [self.startX, self.startY - 1]
        position[3] = [self.startX, self.startY + 1]
        for i in range(4):
            if (
                position[i][1] > -1
                and position[i][1] < 3
                and position[i][0] > -1
                and position[i][0] < 3
            ):
                validMoves.append(position[i])
        return validMoves

    def playMove(self, move: list, board: list):
        """
        This function returns a new board after making a move.

        Args:
        move (list): A list representing the move to be made.
        board (list): A 3x3 list representing the current state of the board.

        Returns:
        newBoard (list): A 3x3 list representing the new state of the board after making the move.
        """
        newBoard = deepcopy(board)
        temp = newBoard[move[1]][move[0]]
        newBoard[move[1]][move[0]] = newBoard[self.startY][self.startX]
        newBoard[self.startY][self.startX] = temp
        return newBoard

    def astar(self):
        """
        This function implements the A* algorithm to solve the 8-Puzzle problem.
        """
        self.calcHeuristic(self.board)
        self.queue.append((self.calcHeuristic(self.board), self.board))
        self.generatedBoards.append(self.board)
        i = 0
        while i < 1000:
            next = self.queue.pop()
            moves = self.getValidMoves(next[1])
            print("\n---------------\n")
            print(f" step {i}\n")
            for j in range(3):
                print(" ", next[1][j])
            if next[1] == self.goal:
                print(f"\nGoal state reached in {i} steps")
                print("\n------------------------------\n")
                exit(1)
            for move in moves:
                newBoard = self.playMove(move, next[1])
                if newBoard not in self.generatedBoards:
                    self.generatedBoards.append(newBoard)
                    self.queue.append((self.calcHeuristic(newBoard), newBoard))
                    self.queue.sort(reverse=True)
            i += 1
        return None


print("8-Puzzle Problem\n")
temp = Puzzle()
temp.astar()