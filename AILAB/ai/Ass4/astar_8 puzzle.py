GOAL = {
    1: 1,
    2: 2,
    3: 3,
    4: 8,
    5: -1,
    6: 4,
    7: 7,
    8: 6,
    9: 5,
}
t_board = dict[int, int]


class Node:
    def __init__(self, board: dict[int, int], steps: int, prev=None, op=None):
        self.board = board.copy()
        self.steps = steps
        self.prev = prev
        self.operation = op

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self) -> int:
        return heuristic(self.board)

    def __repr__(self):
        return str(self.heu())

    def heu(self) -> int:
        return self.steps + heuristic(self.board)


def get_empty_pos(puzzle: t_board) -> int:
    for key in puzzle:
        if puzzle[key] == -1:
            return key


def move_up(puzzle: t_board):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos - 3] = puzzle[pos - 3], puzzle[pos]
    # swapping 2 variables a,b = b,a
    return puzzle


def move_down(puzzle: t_board):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos + 3] = puzzle[pos + 3], puzzle[pos]
    return puzzle


def move_right(puzzle: t_board):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos + 1] = puzzle[pos + 1], puzzle[pos]
    return puzzle


def move_left(puzzle: t_board):
    pos = get_empty_pos(puzzle)
    puzzle[pos], puzzle[pos - 1] = puzzle[pos - 1], puzzle[pos]
    return puzzle


def get_available_operations(puzzle: t_board):
    operations = {
        move_up,
        move_left,
        move_right,
        move_down,
    }
    empty_pos = get_empty_pos(puzzle)

    if empty_pos in {1, 2, 3}:
        operations.remove(move_up)
    if empty_pos in {7, 8, 9}:
        operations.remove(move_down)
    if empty_pos in {3, 6, 9}:
        operations.remove(move_right)
    if empty_pos in {1, 4, 7}:
        operations.remove(move_left)

    return operations


def get_operation_name(op):
    return {
        move_up: "\nMove Empty Slot UP",
        move_down: "\nMove Empty Slot DOWN",
        move_left: "\nMove Empty Slot LEFT",
        move_right: "\nMove Empty Slot RIGHT",
    }[op]


# In the given code, `[op]` is used to access the value of the dictionary corresponding to the key `op`.
# The function `get_operation_name()` takes an input argument `op`, which is expected to be one of the four function names: `move_up`,
# `move_down`, `move_left`, `move_right`.
# The dictionary that follows the `return` statement is used to map each function name to a corresponding operation name.
# The value associated with each key in the dictionary is a string that represents the name of the operation.
# So, `[op]` after the return statement returns the value associated with the key `op` in the dictionary. Essentially, this
# returns the operation name associated with the function name `op` passed as an argument to the `get_operation_name()` function.


def heuristic(puzzle: t_board) -> int:
    score = 0

    for key in puzzle:
        if puzzle[key] != GOAL[key]:
            score += 1

    return score


def safe_get(puzzle: t_board, key: int) -> str:
    if puzzle[key] != -1:
        return puzzle[key]
    return "@"


def display_board(puzzle: dict[int, int]):
    print(
        str(safe_get(puzzle, 1)).center(3, " ")
        + str(safe_get(puzzle, 2)).center(3, " ")
        + str(safe_get(puzzle, 3)).center(3, " ")
    )
    print("-" * 10)
    print(
        str(safe_get(puzzle, 4)).center(3, " ")
        + str(safe_get(puzzle, 5)).center(3," ")
        + str(safe_get(puzzle, 6)).center(3, " ")
    )
    print("-" * 10)
    print(
        str(safe_get(puzzle, 7)).center(3, " ")
        + str(safe_get(puzzle, 8)).center(3, " ")
        + str(safe_get(puzzle, 9)).center(3, " ")
    )


def start(puzzle) -> Node:
    root = Node(puzzle, 0)
    opened = []
    closed = [root]
    steps = 0
    previous = set()
    best_score = 1000

    while len(closed) > 0:
        # print("\n\nOpened:", opened)
        # print("\nClosed:", closed)
        steps += 1
        closed.sort(key=lambda n: n.heu())
        current = closed.pop(0)
        opened.append(current)
        score = heuristic(current.board)

        if score == 0:
            return current

        if current in previous:
            continue
        else:
            previous.add(current)

        if score < best_score:
            best_score = score

        for operation in get_available_operations(current.board):
            child = Node(operation(current.board.copy()), steps, current, operation)
            closed.append(child)

    return current


def main():
    puzzle = {
        1: 1,
        2: -1,
        3: 3,
        4: 8,
        5: 2,
        6: 6,
        7: 7,
        8: 5,
        9: 4,
    }

    print("\nInitial State : ")
    display_board(puzzle)
    print("\nGoal State : ")
    display_board(GOAL)
    node = start(puzzle)

    path: list[Node] = []
    # This line initializes an empty list called 'path' that can only contain objects of type 'Node'.
    # The ': list[Node]' is a type hint indicating that 'path' is a list of 'Node' objects.
    # Without the hint, the interpreter would complain that 'path' is not a list of 'Node' objects.

    # This code segment is used to backtrack the path from the destination node to the source node
    # The path list is initialized to an empty list
    while node:
        # While there is a node in the path, the current node is added to the path list and the pointer is set to its previous node
        path.append(node)
        node = node.prev
    path = path[::-1]
    # The path list is reversed so that the source node appears first and the destination node appears last
    path = path[1:]
    # The first node in the path list is removed because it is the same as the source node

    for i, node in enumerate(path):
        print(f"\n\nStep {i + 1} ")
        if node.operation:
            print(get_operation_name(node.operation))

        display_board(node.board)
        print(f"\nObjective Function Score : {heuristic(node.board) + i + 1}")

    if heuristic(path[-1].board) != 0:
        # path[-1].board just means that the last node in the path list accessed to access the second last node we can use path[-2].board

        print("\nGoal State not Achieved!")
    else:
        print("\nGoal State Achieved")


if __name__ == "__main__":
    main()

# if __name__ == '__main__': is a conditional statement that checks if the current script is being run as the main program (i.e.,
# if it is being directly executed rather than being imported as a module into another script).
# The double underscore (also known as "dunder") before and after the word "name" is a Python convention for
# indicating that it is a special attribute.
# If the condition is true, the code inside the block (in this case, the main() function) will be executed.
# This is a common way to structure Python code to allow a script to be both run as a standalone program and imported as a
# module into another script.
