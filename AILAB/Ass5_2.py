# Import necessary modules
from colorama import Fore, init

# Initialize colorama
init(strip=False)
init(autoreset=True)

# Define Cryptarithmetic class
class Cryptarithmetic():
    """
    This class solves cryptarithmetic puzzles by finding the values of letters that make 
    the arithmetic equation true. The puzzle consists of three words, where each letter 
    represents a unique digit, and the sum of the first two words equals the third word.

    Attributes:
    is_solved (bool): A boolean indicating if the puzzle has been solved.
    solution_count (int): An integer indicating the number of solutions found.

    Methods:
    start(): Prompts the user to enter the three words of the puzzle and solves the puzzle.
    solve(letters, values, visited, equation): Recursively solves the puzzle by finding 
    the values of letters that make the arithmetic equation true.
    """

    def __init__(self):
        """
        Initializes the Cryptarithmetic class with default values for is_solved and solution_count.
        """
        self.is_solved = False
        self.solution_count = 0

    def start(self):
        """
        Prompts the user to enter the three words of the puzzle and solves the puzzle.
        """
        # Prompt user to enter the three words of the puzzle
        word1 = input("Enter First Word - ").upper()
        word2 = input("Enter Second Word - ").upper()
        result = input("Enter Result - ").upper()
        values = []
        visited = [False for _ in range(10)]
        equation = [word1, word2, result]

        # Get Unique Letters
        unique_letters = list(set(word1 + word2 + result))
        if len(unique_letters) > 10:
            print("\nNo Solution (as values will repeat)\n")
            exit()

        # Print the puzzle
        print("Solution Is - ")
        print(f" \t{word1}\n+\t{word2}\n-------------\n\t{result}\n\n")

        # Solve the puzzle
        self.solve(unique_letters, values, visited, equation)

    def solve(self, letters, values, visited, equation):
        """
        Recursively solves the puzzle by finding the values of letters that make the arithmetic equation true.

        Args:
        letters (list): A list of unique letters in the puzzle.
        values (list): A list of values assigned to letters.
        visited (list): A list of boolean values indicating if a value has been assigned to a letter.
        equation (list): A list of three words in the puzzle.

        Returns:
        None
        """
        # If all letters have been assigned a value, check if the equation is true
        if len(letters) == len(values):
            letter_value_map = {letter: value for letter,
                                value in zip(letters, values)}
            if letter_value_map[equation[0][0]] == 0 or letter_value_map[equation[1][0]] == 0 or letter_value_map[equation[2][0]] == 0:
                return

            word1 = ''.join(str(letter_value_map[c]) for c in equation[0])
            word2 = ''.join(str(letter_value_map[c]) for c in equation[1])
            res = ''.join(str(letter_value_map[c]) for c in equation[2])

            if int(word1) + int(word2) == int(res):
                self.solution_count += 1
                print(
                    Fore.GREEN + f"Result {self.solution_count} = {word1} + {word2} = {res}\n")
                self.is_solved = True
            return

        # Assign values to letters and recursively solve the puzzle
        for i in range(10):
            if not visited[i]:
                visited[i] = True
                values.append(i)
                self.solve(letters, values, visited, equation)
                values.pop()
                visited[i] = False


# Create an instance of the Cryptarithmetic class and solve the puzzle
temp = Cryptarithmetic()
temp.start()