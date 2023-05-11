# Python code to solve a word puzzle

def printMatrix(matrix, n):
    """
    This function prints the matrix.

    Args:
    matrix (list): A list of strings representing the matrix.
    n (int): The size of the matrix.

    Returns:
    None
    """
    for i in range(n):
        print(matrix[i])
    print()


def checkHorizontal(x, y, matrix, currentWord):
    """
    This function checks if the current word can be placed horizontally in the matrix.

    Args:
    x (int): The row index of the starting position.
    y (int): The column index of the starting position.
    matrix (list): A list of strings representing the matrix.
    currentWord (str): The current word to be placed.

    Returns:
    matrix (list): A list of strings representing the matrix with the current word placed horizontally.
    """
    n = len(currentWord)
    for i in range(n):
        if matrix[x][y + i] == "#" or matrix[x][y + i] == currentWord[i]:
            matrix[x] = matrix[x][:y + i] + \
                currentWord[i] + matrix[x][y + i + 1:]
        else:
            matrix[0] = "@"
            return matrix
    return matrix


def checkVertical(x, y, matrix, currentWord):
    """
    This function checks if the current word can be placed vertically in the matrix.

    Args:
    x (int): The row index of the starting position.
    y (int): The column index of the starting position.
    matrix (list): A list of strings representing the matrix.
    currentWord (str): The current word to be placed.

    Returns:
    matrix (list): A list of strings representing the matrix with the current word placed vertically.
    """
    n = len(currentWord)
    for i in range(n):
        if matrix[x + i][y] == "#" or matrix[x + i][y] == currentWord[i]:
            matrix[x + i] = matrix[x + i][:y] + \
                currentWord[i] + matrix[x + i][y + 1:]
        else:
            matrix[0] = "@"
            return matrix
    return matrix


def solvePuzzle(words, matrix, index, n):
    """
    This function solves the word puzzle by placing the words in the matrix.

    Args:
    words (list): A list of words to be placed in the matrix.
    matrix (list): A list of strings representing the matrix.
    index (int): The index of the current word to be placed.
    n (int): The size of the matrix.

    Returns:
    None
    """
    if index < len(words):
        currentWord = words[index]
        maxLen = n - len(currentWord)
        for i in range(n):
            for j in range(maxLen + 1):
                temp = checkVertical(j, i, matrix.copy(), currentWord)
                if temp[0] != "@":
                    solvePuzzle(words, temp, index + 1, n)
        for i in range(n):
            for j in range(maxLen + 1):
                temp = checkHorizontal(i, j, matrix.copy(), currentWord)
                if temp[0] != "@":
                    solvePuzzle(words, temp, index + 1, n)
    else:
        printMatrix(matrix, n)
        print()


if __name__ == "__main__":
    # Define the size of the matrix and the words to be placed
    n1 = 10
    matrix = []
    words = []
    matrix.append("*#********")
    matrix.append("*#********")
    matrix.append("*#****#***")
    matrix.append("*##***##**")
    matrix.append("*#****#***")
    matrix.append("*#****#***")
    matrix.append("*#****#***")
    matrix.append("*#*######*")
    matrix.append("*#********")
    matrix.append("***#######")
    words.append("PUNJAB")
    words.append("JHARKHAND")
    words.append("MIZORAM")
    words.append("MUMBAI")
    
    # Solve the puzzle
    solvePuzzle(words, matrix, 0, n1)