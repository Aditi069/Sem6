# This code solves the water jug problem using a breadth-first search algorithm.
# The problem involves two jugs of different sizes and the goal is to measure a specific amount of water using these jugs.
# The program takes in the starting node, the sizes of the jugs, the goal amount, and a dictionary to keep track of visited nodes.
# It then performs a breadth-first search to find the goal state and prints the path taken to reach the goal.

from collections import deque

def main():
    # Define the starting node, jug sizes, goal amount, and a dictionary to keep track of visited nodes
    starting_node = [[0, 0]]
    jugs = [5, 3]
    goal_amount = 4
    check_dict = {}
    
    # Call the search function with the defined parameters
    search(starting_node, jugs, goal_amount, check_dict)


def get_index(node):
    """
    This function takes in a node and returns an index value based on the values of the node.
    The index value is used to keep track of visited nodes in the search algorithm.

    Args:
    node (list): A list of two integers representing the amount of water in each jug.

    Returns:
    index (int): An integer index value based on the values of the node.
    """
    # Calculate the index value based on the values of the node
    index = pow(7, node[0]) * pow(5, node[1])
    
    # Return the calculated index value
    return index


def is_goal(path, goal_amount):
    """
    This function takes in a path and a goal amount and checks if the goal state has been reached.

    Args:
    path (list): A list of nodes representing the path taken to reach the current state.
    goal_amount (int): The amount of water to be measured using the jugs.

    Returns:
    (bool): True if the goal state has been reached, False otherwise.
    """
    # Check if the goal amount has been reached in either of the jugs
    return path[-1][0] == goal_amount or path[-1][1] == goal_amount


def been_there(node, check_dict):
    """
    This function takes in a node and a dictionary of visited nodes and checks if the node has been visited before.

    Args:
    node (list): A list of two integers representing the amount of water in each jug.
    check_dict (dict): A dictionary of visited nodes.

    Returns:
    (bool): True if the node has been visited before, False otherwise.
    """
    # Check if the index value of the node is in the dictionary of visited nodes
    return check_dict.get(get_index(node), False)


def next_transitions(jugs, path, check_dict):
    """
    This function takes in the jug sizes, the current path, and a dictionary of visited nodes.
    It generates all possible next states from the current state.

    Args:
    jugs (list): A list of two integers representing the sizes of the jugs.
    path (list): A list of nodes representing the path taken to reach the current state.
    check_dict (dict): A dictionary of visited nodes.

    Returns:
    result (list): A list of paths representing all possible next states from the current state.
    """
    # Initialize variables
    result = []
    next_nodes = []
    node = []
    a_max = jugs[0]
    b_max = jugs[1]
    a = path[-1][0]
    b = path[-1][1]
    
    # Generate all possible next states from the current state
    node.append(a_max)
    node.append(b)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []
    node.append(a)
    node.append(b_max)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []
    node.append(min(a_max, a + b))
    node.append(b - (node[0] - a))
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []
    node.append(min(a + b, b_max))
    node.insert(0, a - (node[0] - b))
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []
    node.append(0)
    node.append(b)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []
    node.append(a)
    node.append(0)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    
    # Generate paths for all possible next states and add them to the result list
    for i in range(0, len(next_nodes)):
        temp = list(path)
        temp.append(next_nodes[i])
        result.append(temp)
    
    # Return the result list
    return result


def print_path(path):
    """
    This function takes in a path and prints the path taken to reach the goal state.

    Args:
    path (list): A list of nodes representing the path taken to reach the goal state.

    Returns:
    None
    """
    # Print the path taken to reach the goal state
    print(f"0: {path[0]}")
    for i in range(0, len(path) - 1):
        print(i+1, ":", path[i+1])


def search(starting_node, jugs, goal_amount, check_dict):
    """
    This function takes in the starting node, jug sizes, goal amount, and a dictionary of visited nodes.
    It performs a breadth-first search to find the goal state and prints the path taken to reach the goal.

    Args:
    starting_node (list): A list of nodes representing the starting state.
    jugs (list): A list of two integers representing the sizes of the jugs.
    goal_amount (int): The amount of water to be measured using the jugs.
    check_dict (dict): A dictionary of visited nodes.

    Returns:
    None
    """
    # Initialize variables
    goal = []
    solved = False
    q = deque()
    q.appendleft(starting_node)
    
    # Perform a breadth-first search to find the goal state
    while len(q) != 0:
        path = q.popleft()
        check_dict[get_index(path[-1])] = True
        if is_goal(path, goal_amount):
            solved = True
            goal = path
            break
        next_moves = next_transitions(jugs, path, check_dict)
        for i in next_moves:
            q.append(i)
    
    # Print the path taken to reach the goal state or a message if the problem cannot be solved
    if solved:
        print_path(goal)
    else:
        print("Problem cannot be solved.")


if __name__ == '__main__':
    main()