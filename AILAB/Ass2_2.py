# This code solves the "Water Jug Problem" using a breadth-first search algorithm.
# The problem involves two jugs of different sizes and the goal is to measure a specific amount of water using these jugs.
# The code takes the starting node, jugs' sizes, and the goal amount as input and outputs the solution path.

from collections import deque

def main():
    # Define the starting node, jugs' sizes, and the goal amount
    starting_node = [(0, 0)]
    jugs = (5, 3)
    goal_amount = 4
    check_set = set()
    
    # Call the search function to find the solution path
    search(starting_node, jugs, goal_amount, check_set)

def get_index(node):
    """
    This function calculates the index of a node based on its coordinates.

    Args:
    node (tuple): A tuple of two integers representing the coordinates of a node.

    Returns:
    index (int): An integer representing the index of the node.
    """
    # Calculate the index of the node using the given formula
    index = pow(7, node[0]) * pow(5, node[1])
    return index

def is_goal(path, goal_amount):
    """
    This function checks if the last node in a path has the goal amount of water.

    Args:
    path (list): A list of tuples representing the nodes in a path.
    goal_amount (int): An integer representing the goal amount of water.

    Returns:
    True if the last node in the path has the goal amount of water, False otherwise.
    """
    # Check if the last node in the path has the goal amount of water in either jug
    return path[-1][0] == goal_amount or path[-1][1] == goal_amount

def been_there(node, check_set):
    """
    This function checks if a node has been visited before.

    Args:
    node (tuple): A tuple of two integers representing the coordinates of a node.
    check_set (set): A set containing the indices of visited nodes.

    Returns:
    True if the node has been visited before, False otherwise.
    """
    # Check if the index of the node is in the set of visited nodes
    return get_index(node) in check_set

def next_transitions(jugs, path, check_set):
    """
    This function generates the next possible transitions from a node.

    Args:
    jugs (tuple): A tuple of two integers representing the sizes of the jugs.
    path (list): A list of tuples representing the nodes in a path.
    check_set (set): A set containing the indices of visited nodes.

    Returns:
    result (list): A list of paths representing the next possible transitions from the last node in the path.
    """
    # Define the maximum capacities of the jugs
    a_max, b_max = jugs
    # Get the coordinates of the last node in the path
    a, b = path[-1]
    # Define the next possible nodes based on the current node
    next_nodes = [(a_max, b), (a, b_max), (min(a_max, a + b), b - (min(a_max, a + b) - a)),
                  (min(a + b, b_max), a - (min(a + b, b_max) - b)), (0, b), (a, 0)]
    # Create a list of paths representing the next possible transitions from the last node in the path
    result = [list(path) + [node]
              for node in next_nodes if not been_there(node, check_set)]
    return result

def print_path(path):
    """
    This function prints the nodes in a path.

    Args:
    path (list): A list of tuples representing the nodes in a path.
    """
    # Print the nodes in the path
    print(f"0: {path[0]}")
    for i, node in enumerate(path[1:], 1):
        print(f"{i}: {node}")

def search(starting_node, jugs, goal_amount, check_set):
    """
    This function performs a breadth-first search to find the solution path.

    Args:
    starting_node (list): A list containing the starting node.
    jugs (tuple): A tuple of two integers representing the sizes of the jugs.
    goal_amount (int): An integer representing the goal amount of water.
    check_set (set): A set containing the indices of visited nodes.
    """
    # Initialize variables
    goal = []
    solved = False
    q = deque()
    q.appendleft(starting_node)
    
    # Perform breadth-first search
    while len(q) != 0:
        path = q.popleft()
        check_set.add(get_index(path[-1]))
        if is_goal(path, goal_amount):
            solved = True
            goal = path
            break
        next_moves = next_transitions(jugs, path, check_set)
        q.extendleft(next_moves)
    
    # Print the solution path if found, otherwise print an error message
    if solved:
        print_path(goal)
    else:
        print("Problem cannot be solved.")

if __name__ == '__main__':
    main()