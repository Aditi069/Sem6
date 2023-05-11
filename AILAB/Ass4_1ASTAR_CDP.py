# Importing necessary libraries
from colorama import Fore, init

# Initializing colorama
init(autoreset=True)

# Defining a class to calculate the shortest distance between cities using A* algorithm
class City_Distance():
    # Defining a Graph class to represent the cities and their distances
    class Graph:
        def __init__(self, graph_dict=None, directed=True):
            """
            Initializes the Graph class with a dictionary to store the cities and their distances.

            Args:
            graph_dict (dict): A dictionary to store the cities and their distances. Default is None.
            directed (bool): A boolean value to indicate if the graph is directed or not. Default is True.
            """
            self.graph_dict = graph_dict or {}
            self.directed = directed
            if not directed:
                self.make_undirected()

        def make_undirected(self):
            """
            Makes the graph undirected by adding the reverse edges for each edge in the graph.
            """
            for a in list(self.graph_dict.keys()):
                for (b, dist) in self.graph_dict[a].items():
                    self.graph_dict.setdefault(b, {})[a] = dist

        def connect(self, A, B, distance=1):
            """
            Connects two cities with a distance.

            Args:
            A (str): The name of the first city.
            B (str): The name of the second city.
            distance (int): The distance between the two cities. Default is 1.
            """
            self.graph_dict.setdefault(A, {})[B] = distance
            if not self.directed:
                self.graph_dict.setdefault(B, {})[A] = distance

        def get(self, a, b=None):
            """
            Returns the distance between two cities.

            Args:
            a (str): The name of the first city.
            b (str): The name of the second city. Default is None.

            Returns:
            links (dict): A dictionary containing the distance between two cities.
            """
            links = self.graph_dict.setdefault(a, {})
            if b is None:
                return links
            else:
                return links.get(b)

        def nodes(self):
            """
            Returns a list of all the cities in the graph.

            Returns:
            nodes (list): A list of all the cities in the graph.
            """
            s1 = set([k for k in self.graph_dict.keys()])
            s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
            nodes = s1.union(s2)
            return list(nodes)

        def display_graph(self):
            """
            Displays the graph with the cities and their distances.
            """
            print(Fore.YELLOW+"\n\t\t\tTHE GRAPH IS - \n")
            for key in self.graph_dict:
                print(Fore.CYAN+key, Fore.WHITE+' -> ', self.graph_dict[key])

    # Defining a Node class to represent each city as a node in the graph
    class Node:
        def __init__(self, name: str, parent: str):
            """
            Initializes the Node class with the name of the city and its parent city.

            Args:
            name (str): The name of the city.
            parent (str): The name of the parent city.
            """
            self.name = name
            self.parent = parent
            self.g = 0
            self.h = 0
            self.f = 0

        def __eq__(self, other):
            """
            Checks if two nodes are equal.

            Args:
            other (Node): The other node to compare with.

            Returns:
            bool: True if the two nodes are equal, False otherwise.
            """
            return self.name == other.name

        def __lt__(self, other):
            """
            Compares the f value of two nodes.

            Args:
            other (Node): The other node to compare with.

            Returns:
            bool: True if the f value of the current node is less than the other node, False otherwise.
            """
            return self.f < other.f

    def a_star(self, graph, heuristics, start, end):
        """
        Calculates the shortest path between two cities using A* algorithm.

        Args:
        graph (Graph): The graph containing the cities and their distances.
        heuristics (dict): A dictionary containing the heuristic values for each city.
        start (str): The name of the starting city.
        end (str): The name of the destination city.

        Returns:
        path (list): A list of cities representing the shortest path between the starting and destination cities.
        """
        open = []
        closed = []
        start_node = self.Node(start, "")
        goal_node = self.Node(end, "")
        open.append(start_node)
        while len(open) > 0:
            print(Fore.BLUE+"\n\nOpen List - ")
            for i in open:
                print(i.name, end=" | ")
            print()
            print(Fore.BLUE+"Closed List - ")
            for i in closed:
                print(i.name, end=" | ")
            open.sort()
            current_node = open.pop(0)
            closed.append(current_node)
            if current_node == goal_node:
                path = []
                while current_node != start_node:
                    path.append(current_node.name)
                    current_node = current_node.parent
                path.append(start_node.name)
                return path[::-1]
            neighbors = graph.get(current_node.name)
            for key, unused_value in neighbors.items():
                neighbor = self.Node(key, current_node)
                if (neighbor in closed):
                    continue
                neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
                neighbor.h = heuristics.get(neighbor.name)
                neighbor.f = neighbor.g + neighbor.h
                if (self.add_to_open(open, neighbor) == True):
                    open.append(neighbor)
        return None

    def add_to_open(self, open, neighbor):
        """
        Adds a node to the open list if it is not already in the list or if its f value is less than the existing node.

        Args:
        open (list): The list of nodes in the open list.
        neighbor (Node): The node to be added to the open list.

        Returns:
        bool: True if the node is added to the open list, False otherwise.
        """
        for node in open:
            if (neighbor == node and neighbor.f >= node.f):
                return False
        return True

    def start(self):
        """
        Initializes the graph, calculates the shortest path between two cities using A* algorithm, and displays the path.
        """
        graph = self.Graph()
        graph.connect('Oradea', 'Zerind', 71)
        graph.connect('Oradea', 'Sibiu', 151)
        graph.connect('Zerind', 'Arad', 75)
        graph.connect('Arad', 'Sibiu', 140)
        graph.connect('Arad', 'Timisoara', 118)
        graph.connect('Timisoara', 'Lugoj', 111)
        graph.connect('Lugoj', 'Mehadia', 70)
        graph.connect('Mehadia', 'Drobeta', 75)
        graph.connect('Drobeta', 'Craiova', 120)
        graph.connect('Craiova', 'Pitesti', 138)
        graph.connect('Craiova', 'Rimnicu Vilcea', 146)
        graph.connect('Sibiu', 'Fagaras', 99)
        graph.connect('Fagaras', 'Bucharest', 211)
        graph.connect('Sibiu', 'Rimnicu Vilcea', 80)
        graph.connect('Rimnicu Vilcea', 'Pitesti', 97)
        graph.connect('Pitesti', 'Bucharest', 101)
        graph.connect('Bucharest', 'Giurgui', 90)
        graph.make_undirected()
        graph.display_graph()
        heuristics = {}
        heuristics['Arad'] = 366
        heuristics['Bucharest'] = 0
        heuristics['Craiova'] = 160
        heuristics['Drobeta'] = 242
        heuristics['Fagaras'] = 176
        heuristics['Guirgiu'] = 77
        heuristics['Lugoj'] = 244
        heuristics['Mehadia'] = 241
        heuristics['Oradea'] = 380
        heuristics['Pitesti'] = 160