# Import necessary libraries
from colorama import Fore, init
from copy import deepcopy

# Initialize colorama
init(autoreset=True)

# Define a Robot class
class Robot():
    # Define the table layout
    table = [
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', Fore.YELLOW+'#', '-', '-', '-', Fore.YELLOW+'#', Fore.YELLOW +
            '#', Fore.YELLOW+'#', Fore.YELLOW+'#', Fore.YELLOW+'#', '-'],
        ['-', Fore.YELLOW+'#', Fore.YELLOW+'#', '-', '-',
            '-', '-', '-', '-', Fore.YELLOW+'#', '-'],
        ['-', '-', Fore.YELLOW+'#', Fore.YELLOW+'#', Fore.YELLOW+'#', Fore.YELLOW+'#',
            Fore.YELLOW+'#', Fore.YELLOW+'#', Fore.YELLOW+'#', Fore.YELLOW+'#', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    ]
    # Define the goal and start positions
    goalX = 6
    goalY = 2
    startX = 0
    startY = 3
    # Create copies of the table for use in calculations
    newTable = deepcopy(table)
    newTable_2 = deepcopy(table)
    newTable_3 = deepcopy(table)
    # Initialize the queue and visited lists
    queue = []
    visited = []

    # Calculate the Manhatten distance
    def calcManhatten(self):
        """
        This function calculates the Manhatten distance between the start and goal positions
        and updates the table with the distance values.
        """
        # Update the table with the start and goal positions
        self.table[self.startY][self.startX] = Fore.BLUE+'S'
        self.table[self.goalY][self.goalX] = Fore.RED+'G'
        # Calculate the Manhatten distance for each cell in the table
        for i in range(5):
            for j in range(11):
                if self.table[i][j] != Fore.YELLOW+'#':
                    self.newTable_2[i][j] = str(
                        abs(self.goalX - j) + abs(self.goalY-i))
                    self.newTable_3[i][j] = str(
                        abs(self.startX - j) + abs(self.startY-i))
                    self.newTable[i][j] = self.newTable_2[i][j] + \
                        self.newTable_3[i][j]
                print(
                    f'\t{self.newTable_2[i][j]}+{self.newTable_3[i][j]}', end='')
            print('\n')
        # Add the start position to the queue
        position = [self.startX, self.startY]
        self.queue.append((self.newTable[self.startY][self.startX], position))

    # Get the neighbors of the current position
    def getNeighbors(self):
        """
        This function gets the neighbors of the current position and adds them to the queue.
        """
        position = [[0] * 2] * 4
        value = ["0"] * 4
        position[0] = [self.startX+1, self.startY]
        position[1] = [self.startX-1, self.startY]
        position[2] = [self.startX, self.startY-1]
        position[3] = [self.startX, self.startY+1]
        for i in range(4):
            if position[i][1] > -1 and position[i][1] < 5 and position[i][0] > -1 and position[i][0] < 11:
                value[i] = self.newTable[position[i][1]][position[i][0]]
                if value[i] != Fore.YELLOW+'#' and ((value[i], position[i]) not in self.visited) and ((value[i], position[i]) not in self.queue):
                    self.queue.append((value[i], position[i]))
        self.queue.sort(reverse=True)

    # Implement the A* algorithm
    def a_star(self):
        """
        This function implements the A* algorithm to find the shortest path from the start to the goal position.
        """
        steps = 0
        while (self.queue):
            # input()
            print(f"Steps taken: {steps}")
            print(f"Queue: {self.queue}")
            next = self.queue.pop()
            print(f"Selecting: {next}")
            print(f"Current queue: {self.queue}")
            if next[1][0] == self.goalX and next[1][1] == self.goalY:
                print(f"Goal State reached in {steps} steps")
                exit(1)
            if next[1] == [self.startX, self.startY]:
                self.table[next[1][1]][next[1][0]] = Fore.BLUE+'S'
            else:
                self.table[next[1][1]][next[1][0]
                                       ] = f"{Fore.GREEN+str(self.newTable_2[next[1][1]][next[1][0]])}+{str(self.newTable_3[next[1][1]][next[1][0]])}"
            self.visited.append(next)
            self.startX = next[1][0]
            self.startY = next[1][1]
            self.getNeighbors()
            print(
                f"Adding neighbours of {next} to queue\nCurrent queue: {self.queue}\n")
            self.printTable(self.table)
            print(
                '\t---------------------------------------------------------------------------------')
            steps += 1

    # Print the table
    def printTable(self, table):
        """
        This function prints the table.
        """
        for i in range(5):
            for j in range(11):
                print("\t"+Fore.WHITE+str(table[i][j]), end='')
            print('\n')


# Create a Robot object and run the A* algorithm
temp = Robot()
temp.calcManhatten()
print('\n Current State:')
temp.printTable(temp.table)
temp.a_star()