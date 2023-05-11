# Import the necessary module
from colorama import init

# Initialize the colorama module
init(autoreset=True)

# Define a class for city distance calculation
class cityDistance:
    # Define the city map with distances between cities
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
    # Define the heuristic function using straight line distance
    hSLD = {
        "Delhi": 0,
        "Indore": 800,
        "Mumbai": 1300,
        "Hyderabad": 1500,
        "Bangalore": 1800,
        "Nagpur": 1000,
        "Kolkata": 1300,
    }
    # Define the queue, open and closed lists, start and end cities, and total distance
    queue = []
    open = []
    closed = []
    start = "Hyderabad"
    end = "Delhi"
    totalDistance = 0

    # Function to expand the near cities from the current city
    def expand(self, s: str):
        """
        This function expands the near cities from the current city.

        Args:
        s (str): The current city.

        Returns:
        near_cities (list): A list of tuples containing the distance and name of the near cities.
        """
        near_cities = self.cityMap.get(s)
        if near_cities is not None:
            near_cities.sort(reverse=True)
        return near_cities

    # Function to check if the move is valid
    def validMove(self, near_cities: list):
        """
        This function checks if the move to the near cities is valid.

        Args:
        near_cities (list): A list of tuples containing the distance and name of the near cities.
        """
        for city in near_cities:
            self.queue.append((self.hSLD.get(city[1]), city[1], city[0]))
            if city[1] not in self.closed:
                self.open.append(city[1])
            if self.open.count(city[1]) > 1:
                self.open.remove(city[1])
        self.queue.sort(reverse=True)

    # Function to perform best first search
    def bestFirstSearch(self):
        """
        This function performs the best first search algorithm to find the shortest path between two cities.
        """
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

# Create an instance of the cityDistance class and perform the best first search
s = cityDistance()
s.bestFirstSearch()