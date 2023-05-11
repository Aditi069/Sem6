# Import necessary libraries
import copy
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Define the Puzzle class
class Puzzle:
    # Define the goal state of the puzzle
    goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    # Define the initial state of the puzzle
    board_config = [[2, 3, 4], [1, 8, 0], [7, 6, 5]]
    # Initialize the number of steps taken to solve the puzzle
    steps = 0

    # Calculate the heuristic value of a given configuration
    def calculate_fOfn(self, cal_config):
        """
        This function calculates the heuristic value of a given configuration.

        Args:
        cal_config (list): A 3x3 list representing the configuration of the puzzle.

        Returns:
        h (int): The heuristic value of the given configuration.
        """
        h = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if cal_config[i][j] != self.goal[i][j]:
                    h += 1
        return h

    # Check if a given move is safe
    def isSafe(self, x, y):
        """
        This function checks if a given move is safe.

        Args:
        x (int): The x-coordinate of the move.
        y (int): The y-coordinate of the move.

        Returns:
        bool: True if the move is safe, False otherwise.
        """
        return x >= 0 and x < 3 and y >= 0 and y < 3

    # Print the current configuration of the puzzle
    def print_board(self, print_config):
        """
        This function prints the current configuration of the puzzle.

        Args:
        print_config (list): A 3x3 list representing the configuration of the puzzle.
        """
        for i in range(0, 3):
            for j in range(0, 3):
                print(" " + str(print_config[i][j]) + " ", end="")
        print()

    # Find all possible configurations of the puzzle from the current configuration
    def find_all_configs(self, all_config):
        """
        This function finds all possible configurations of the puzzle from the current configuration.

        Args:
        all_config (list): A 3x3 list representing the configuration of the puzzle.

        Returns:
        config_boards (list): A list of all possible configurations of the puzzle from the current configuration.
        """
        config_boards = []
        config2 = copy.deepcopy(all_config)
        config1 = copy.deepcopy(all_config)
        config3 = copy.deepcopy(all_config)
        config4 = copy.deepcopy(all_config)
        for i in range(0, 3):
            for j in range(0, 3):
                if all_config[i][j] != 0:
                    if self.isSafe(i - 1, j):
                        if all_config[i - 1][j] == 0:
                            config1[i - 1][j] = config1[i][j]
                            config1[i][j] = 0
                            config_boards.append(config1)
                    if self.isSafe(i + 1, j):
                        if all_config[i + 1][j] == 0:
                            config2[i + 1][j] = config2[i][j]
                            config2[i][j] = 0
                            config_boards.append(config2)
                    if self.isSafe(i, j + 1):
                        if all_config[i][j + 1] == 0:
                            config3[i][j + 1] = config3[i][j]
                            config3[i][j] = 0
                            config_boards.append(config3)
                    if self.isSafe(i, j - 1):
                        if all_config[i][j - 1] == 0:
                            config4[i][j - 1] = config4[i][j]
                            config4[i][j] = 0
                            config_boards.append(config4)
        return config_boards

    # Start the puzzle
    def puzzle_start(self, config, goal_heuristic):
        """
        This function starts the puzzle.

        Args:
        config (list): A 3x3 list representing the initial configuration of the puzzle.
        goal_heuristic (int): The heuristic value of the goal state of the puzzle.
        """
        objective_values = []
        new_config = copy.deepcopy(config)
        boards_configs = []
        open_list = []
        closed_list = []
        visited = []
        open_list.append(new_config)
        visited.append(new_config)
        print(Fore.RED + "\t\t\tLIST IS DISPLAYED IN ROW MAJOR ORDER\n\n")
        print("Initially - ")
        print("Open List - ")
        print(open_list)
        print("Closed List - ")
        print(closed_list)
        print("\n\n")
        while True:
            self.steps += 1
            boards_configs.clear()
            open_list.remove(new_config)
            closed_list.append(new_config)
            heuristic_value = self.calculate_fOfn(new_config)
            if heuristic_value == goal_heuristic:
                print("Solution Reached !!")
                print(f"\nIn {self.steps} Steps\n")
                break
            boards_configs = self.find_all_configs(new_config)
            for i in boards_configs:
                visited.append(i)
                open_list.append(i)
                h = self.calculate_fOfn(i)
                objective_values.append(h)
            print("Open List - ")
            print(open_list)
            print("Closed List - ")
            print(closed_list)
            print("\n\n")
            min_value = min(objective_values)
            min_value_index = objective_values.index(min_value)
            new_config = boards_configs[min_value_index]
            print(
                f"Board Configuration Selected With Heuristic Value -{str(self.steps)} + {str(min_value)}"
            )
            self.print_board(new_config)
            print("\n")
            objective_values.clear()

    # Start the puzzle solving process
    def Start_Puzzle(self):
        """
        This function starts the puzzle solving process.
        """
        print("8-Puzzle Problem Using Best First Search\n")
        goal_heuristic = self.calculate_fOfn(self.goal)
        self.puzzle_start(self.board_config, goal_heuristic)


# Create an instance of the Puzzle class and start the puzzle solving process
s = Puzzle()
s.Start_Puzzle()