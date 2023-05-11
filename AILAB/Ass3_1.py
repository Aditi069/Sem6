# This code is written in Python and solves the 8-puzzle problem using hill climbing algorithm.

import random

class EightPuzzle:
    # Define the goal state
    GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def __init__(self, state=None):
        """
        Initializes an instance of the EightPuzzle class.

        Args:
        state (list): A list of integers representing the initial state of the puzzle. 
        If no state is provided, a random state is generated.

        Returns:
        None
        """
        if state is None:
            self.state = self.random_state()
        else:
            self.state = state

    def random_state(self):
        """
        Generates a random state for the puzzle.

        Args:
        None

        Returns:
        state (list): A list of integers representing the randomly generated state of the puzzle.
        """
        state = self.GOAL_STATE.copy()
        random.shuffle(state)
        return state

    def is_goal_state(self):
        """
        Checks if the current state of the puzzle is the goal state.

        Args:
        None

        Returns:
        bool: True if the current state is the goal state, False otherwise.
        """
        return self.state == self.GOAL_STATE

    def get_successors(self):
        """
        Generates the possible successor states of the current state.

        Args:
        None

        Returns:
        successors (list): A list of EightPuzzle objects representing the possible successor states.
        """
        successors = []
        i = self.state.index(0)
        if i not in [0, 1, 2]:  # Move the blank up
            new_state = self.state.copy()
            new_state[i], new_state[i-3] = new_state[i-3], new_state[i]
            successors.append(EightPuzzle(new_state))
        if i not in [0, 3, 6]:  # Move the blank left
            new_state = self.state.copy()
            new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
            successors.append(EightPuzzle(new_state))
        if i not in [6, 7, 8]:  # Move the blank down
            new_state = self.state.copy()
            new_state[i], new_state[i+3] = new_state[i+3], new_state[i]
            successors.append(EightPuzzle(new_state))
        if i not in [2, 5, 8]:  # Move the blank right
            new_state = self.state.copy()
            new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
            successors.append(EightPuzzle(new_state))
        return successors

    def heuristic(self):
        """
        Calculates the heuristic value of the current state.

        Args:
        None

        Returns:
        int: The heuristic value of the current state.
        """
        return sum([1 if self.state[i] != self.GOAL_STATE[i] else 0 for i in range(9)])

    def __lt__(self, other):
        """
        Compares the heuristic values of two EightPuzzle objects.

        Args:
        other (EightPuzzle): The other EightPuzzle object to compare with.

        Returns:
        bool: True if the heuristic value of the current object is less than the other object, False otherwise.
        """
        return self.heuristic() < other.heuristic()

    def __eq__(self, other):
        """
        Compares the states of two EightPuzzle objects.

        Args:
        other (EightPuzzle): The other EightPuzzle object to compare with.

        Returns:
        bool: True if the states of the two objects are equal, False otherwise.
        """
        return self.state == other.state

    def __hash__(self):
        """
        Returns the hash value of the current state.

        Args:
        None

        Returns:
        int: The hash value of the current state.
        """
        return hash(str(self.state))

    def __str__(self):
        """
        Returns a string representation of the current state.

        Args:
        None

        Returns:
        str: A string representation of the current state.
        """
        return f"{self.state[:3]}\n{self.state[3:6]}\n{self.state[6:]}\n"


def hill_climbing(problem):
    """
    Solves the 8-puzzle problem using hill climbing algorithm.

    Args:
    problem (EightPuzzle): An instance of the EightPuzzle class representing the initial state of the puzzle.

    Returns:
    current (EightPuzzle): An instance of the EightPuzzle class representing the final state of the puzzle.
    """
    current = problem
    while True:
        print(current)
        if current.is_goal_state():
            return current
        successors = current.get_successors()
        if not successors:
            return current  # Local maxima or plateau
        best = min(successors)
        if best.heuristic() >= current.heuristic():
            return current  # Local maxima or plateau
        current = best


initial_state_a = [1, 2, 3, 4, 5, 6, 7, 0, 8]  # Solution is found
initial_state_b = [1, 2, 3, 4, 0, 5, 7, 8, 6]  # Local maxima or plateau

problem_a = EightPuzzle(initial_state_a)
solution_a = hill_climbing(problem_a)
print(f"Solution found:\n{solution_a}")

problem_b = EightPuzzle(initial_state_b)
local_maxima_or_plateau = hill_climbing(problem_b)
print(f"Local maxima or plateau:\n{local_maxima_or_plateau}")