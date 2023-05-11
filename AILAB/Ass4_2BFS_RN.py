# Import necessary libraries
import copy
from colorama import Fore, init

# Initialize colorama to automatically reset color changes
init(autoreset=True)

# Define the Robot class
class Robot:
    # Define the table as a class variable
    table = [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        [
            "-",
            Fore.YELLOW + "#",
            "-",
            "-",
            "-",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            "-",
        ],
        [
            "-",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            Fore.YELLOW + "#",
            "-",
        ],
        [
            "-",
            "-",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            "-",
        ],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ]
    # Define the goal and start positions as class variables
    goalX = 6
    goalY = 2
    startX = 0
    startY = 3
    # Create a deepcopy of the table to be used for calculations
    newTable = copy.deepcopy(table)
    # Create empty lists to store the queue and visited positions
    queue = []
    visited = []

    # Calculate the Manhattan distance for each position on the table
    def calcManhatten(self):
        # Set the start and goal positions on the table
        self.table[self.startY][self.startX] = Fore.BLUE + "S"
        self.table[self.goalY][self.goalX] = Fore.RED + "G"
        # Print the header for the Manhattan distance table
        print("\n Manhatten Distance: \n")
        # Loop through each position on the table
        for i in range(5):
            for j in range(11):
                # If the position is not a wall, calculate the Manhattan distance
                if self.table[i][j] != Fore.YELLOW + "#":
                    self.newTable[i][j] = str(
                        abs(self.goalX - j) + abs(self.goalY - i))
                # Print the value of the position in the newTable
                print("\t", self.newTable[i][j], end="")
            print("\n")
        # Set the starting position and its Manhattan distance as the first item in the queue
        position = [self.startX, self.startY]
        self.queue.append((self.newTable[self.startY][self.startX], position))

    # Get the neighbors of the current position
    def getNeighbors(self):
        # Create a list to store the positions of the neighbors and their Manhattan distances
        position = [[0] * 2] * 4
        value = ["0"] * 4
        # Define the positions of the neighbors
        position[0] = [self.startX + 1, self.startY]
        position[1] = [self.startX - 1, self.startY]
        position[2] = [self.startX, self.startY - 1]
        position[3] = [self.startX, self.startY + 1]
        # Loop through each neighbor
        for i in range(4):
            # Check if the neighbor is within the bounds of the table and not a wall
            if (
                position[i][1] > -1
                and position[i][1] < 5
                and position[i][0] > -1
                and position[i][0] < 11
            ):
                # Get the Manhattan distance of the neighbor
                value[i] = self.newTable[position[i][1]][position[i][0]]
                # If the neighbor has not been visited, add it to the queue
                if value[i] != Fore.YELLOW + "#" and (
                    (value[i], position[i]) not in self.visited
                ):
                    self.queue.append((value[i], position[i]))
        # Sort the queue in descending order based on Manhattan distance
        self.queue.sort(reverse=True)

    # Perform the best-first search algorithm
    def bestFirstSearch(self):
        # Initialize the number of steps taken to 0
        steps = 0
        # Loop through the queue until it is empty
        while self.queue:
            # Wait for user input before continuing
            input()
            # Print the number of steps taken and the current queue
            print(f"Steps taken: {steps}")
            print(f"Queue: {self.queue}")
            # Select the next position from the queue
            next = self.queue.pop()
            # Print the selected position and the current queue
            print(f"Selecting: {next}")
            print(f"Current queue: {self.queue}")
            # Check if the goal position has been reached
            if next[1][0] == self.goalX and next[1][1] == self.goalY:
                print(f"Goal State reached in {steps} steps")
                exit(1)
            # Update the current position on the table
            if next[1] == [self.startX, self.startY]:
                self.table[next[1][1]][next[1][0]] = Fore.BLUE + "S"
            else:
                self.table[next[1][1]][next[1][0]] = Fore.GREEN + str(next[0])
            # Add the current position to the visited list
            self.visited.append(next)
            # Update the current position and get its neighbors
            self.startX = next[1][0]
            self.startY = next[1][1]
            self.getNeighbors()
            # Print the updated table and a separator
            print(
                f"Adding neighbours of {next} to queue\nCurrent queue:{self.queue}\n")
            self.printTable(self.table)
            print(
                "\t---------------------------------------------------------------------------------"
            )
            # Increment the number of steps taken
            steps += 1

    # Print the table with colors
    def printTable(self, table):
        for i in range(5):
            for j in range(11):
                print("\t" + Fore.WHITE + table[i][j], end="")
            print("\n")


# Create a Robot object and run the best-first search algorithm
s = Robot()
s.calcManhatten()
print("\n Current State:")
s.printTable(s.table)
s.bestFirstSearch()