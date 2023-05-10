""" Question 4: Implement the following algorithms:
A* Algorithm -
a. Robot navigation
b. City Distance Problem
c. 8-Puzzle
"""
import copy
from colorama import Fore, init

init(autoreset=True)


class Puzzle:
    goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    board_config = [[2, 3, 4], [1, 8, 0], [7, 6, 5]]
    steps = 0

    def calculate_fOfn(self, cal_config):
        h = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if cal_config[i][j] != self.goal[i][j]:
                    h += 1
        return h

    def isSafe(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y < 3

    def print_board(self, print_config):
        for i in range(0, 3):
            for j in range(0, 3):
                print(" " + str(print_config[i][j]) + " ", end="")
        print()

    def find_all_configs(self, all_config):
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

    def puzzle_start(self, config, goal_heuristic):
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

    def Start_Puzzle(self):
        print("8-Puzzle Problem Using Best First Search\n")
        goal_heuristic = self.calculate_fOfn(self.goal)
        self.puzzle_start(self.board_config, goal_heuristic)


class Robot:
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
    goalX = 6
    goalY = 2
    startX = 0
    startY = 3
    newTable = copy.deepcopy(table)
    queue = []
    visited = []

    def calcManhatten(self):
        self.table[self.startY][self.startX] = Fore.BLUE + "S"
        self.table[self.goalY][self.goalX] = Fore.RED + "G"
        print("\n Manhatten Distance: \n")
        for i in range(5):
            for j in range(11):
                if self.table[i][j] != Fore.YELLOW + "#":
                    self.newTable[i][j] = str(
                        abs(self.goalX - j) + abs(self.goalY - i))
                print("\t", self.newTable[i][j], end="")
            print("\n")
        position = [self.startX, self.startY]
        self.queue.append((self.newTable[self.startY][self.startX], position))

    def getNeighbors(self):
        position = [[0] * 2] * 4
        value = ["0"] * 4
        position[0] = [self.startX + 1, self.startY]
        position[1] = [self.startX - 1, self.startY]
        position[2] = [self.startX, self.startY - 1]
        position[3] = [self.startX, self.startY + 1]
        for i in range(4):
            if (
                position[i][1] > -1
                and position[i][1] < 5
                and position[i][0] > -1
                and position[i][0] < 11
            ):
                value[i] = self.newTable[position[i][1]][position[i][0]]
                if value[i] != Fore.YELLOW + "#" and (
                    (value[i], position[i]) not in self.visited
                ):
                    self.queue.append((value[i], position[i]))
        self.queue.sort(reverse=True)

    def bestFirstSearch(self):
        steps = 0
        while self.queue:
            input()
            print(f"Steps taken: {steps}")
            print(f"Queue: {self.queue}")
            next = self.queue.pop()
            print(f"Selecting: {next}")
            print(f"Current queue: {self.queue}")
            if next[1][0] == self.goalX and next[1][1] == self.goalY:
                print(f"Goal State reached in {steps} steps")
                exit(1)
            if next[1] == [self.startX, self.startY]:
                self.table[next[1][1]][next[1][0]] = Fore.BLUE + "S"
            else:
                self.table[next[1][1]][next[1][0]] = Fore.GREEN + str(next[0])
            self.visited.append(next)
            self.startX = next[1][0]
            self.startY = next[1][1]
            self.getNeighbors()
            print(
                f"Adding neighbours of {next} to queue\nCurrent queue:{self.queue}\n")
            self.printTable(self.table)
            print(
                "\t---------------------------------------------------------------------------------"
            )
            steps += 1

    def printTable(self, table):
        for i in range(5):
            for j in range(11):
                print("\t" + Fore.WHITE + table[i][j], end="")
            print("\n")


class cityDistance:
    cityMap = {
        "Delhi": [(800, "Indore"), (1300, "Kolkata")],
        "Indore": [(600, "Mumbai"), (500, "Nagpur"), (800, "Delhi")],
        "Kolkata": [(1200, "Nagpur"), (1500, "Hyderabad"), (1300, "Delhi")],
        "Mumbai": [(800, "Hyderabad"), (1000, "Bangalore"), (600, "Indore")],
        "Nagpur": [(500, "Indore"), (1200, "Kolkata"), (500, "Hyderabad")],
        "Hyderabad": [
            (800, "Mumbai"),
            (500, "Nagpur"),
            (1500, "Kolkata"),
            (500, "Bangalore"),
        ],
        "Bangalore": [(1000, "Mumbai"), (500, "Hyderabad")],
    }
    hSLD = {
        "Delhi": 0,
        "Indore": 800,
        "Mumbai": 1300,
        "Hyderabad": 1500,
        "Bangalore": 1800,
        "Nagpur": 1000,
        "Kolkata": 1300,
    }
    queue = []
    open = []
    closed = []
    start = "Hyderabad"
    end = "Delhi"
    totalDistance = 0

    def expand(self, s: str):
        near_cities = self.cityMap.get(s)
        if near_cities is not None:
            near_cities.sort(reverse=True)
        return near_cities

    def validMove(self, near_cities: list):
        for city in near_cities:
            self.queue.append((self.hSLD.get(city[1]), city[1], city[0]))
            if city[1] not in self.closed:
                self.open.append(city[1])
            if self.open.count(city[1]) > 1:
                self.open.remove(city[1])
        self.queue.sort(reverse=True)

    def bestFirstSearch(self):
        self.queue.append((self.hSLD.get(self.start), self.start, 0))
        self.open.append(self.start)
        while 1:
            next: str = self.queue.pop()
            near_cities = self.expand(next[1])
            self.closed.append(next[1])
            self.totalDistance = self.totalDistance + int(next[2])
            if near_cities is not None:
                self.validMove(near_cities)
            self.open.remove(next[1])
            print(f"\nOpen List: {self.open}\nClosed List: {self.closed}")
            if next[1] == self.end:
                print("Path Reached")
                print(
                    f"Total Distance from {self.start} to {self.end}: {self.totalDistance}km"
                )
                exit(1)


print("Select a problem(Best First Search): ")
print("1. 8-Puzzle")
print("2. Robot Navigation")
print("3. City Distance Problem")
ch = int(input("Enter your choice(1-3):"))
if ch == 1:
    print("[+]8 Puzzle")
    s = Puzzle()
    s.Start_Puzzle()
elif ch == 2:
    print("[+]Robot Navigation")
    s = Robot()
    s.calcManhatten()
    print("\n Current State:")
    s.printTable(s.table)
    s.bestFirstSearch()
elif ch == 3:
    print("[+]City Distance")
    s = cityDistance()
    s.bestFirstSearch()
else:
    print("[-]Run again and enter valid choice")
    exit(1)
