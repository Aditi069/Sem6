# Import necessary modules
from colorama import Fore, Back, Style, init

# Initialize colorama
init(strip=False)
init(autoreset=True)

# Define a class for map coloring
class map_coloring():
    # Colors to be used for coloring the map
    colors = [Fore.RED+'Red', Fore.GREEN+'Green',
              Fore.YELLOW+'Yellow', Fore.MAGENTA+'Violet']

    # Define the map
    states = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    neighbors = {}
    neighbors['A'] = ['B', 'C', 'D']
    neighbors['B'] = ['A', 'C']
    neighbors['C'] = ['A', 'B', 'D', 'E']
    neighbors['D'] = ['A', 'C', 'F', 'E']
    neighbors['E'] = ['F', 'C', 'D']
    neighbors['F'] = ['E', 'D', 'G']
    neighbors['G'] = ['F']

    # Dictionary to store the colors of each state
    colors_of_states = {}

    # Function to print the map
    def print_graph(self):
        """
        This function prints the map with its neighbors.
        """
        for key in self.neighbors:
            print(Fore.CYAN + key + Fore.WHITE + ' -> ', self.neighbors[key])

    # Function to check if a color can be assigned to a state
    def promising(self, state, color):
        """
        This function checks if a color can be assigned to a state by checking if any of its neighbors
        have already been assigned the same color.

        Args:
        state (str): The state to be checked.
        color (str): The color to be assigned to the state.

        Returns:
        bool: True if the color can be assigned to the state, False otherwise.
        """
        for neighbor in self.neighbors.get(state):
            color_of_neighbor = self.colors_of_states.get(neighbor)
            if color_of_neighbor == color:
                return False
        return True

    # Function to get a color for a state
    def get_color_for_state(self, state):
        """
        This function gets a color for a state by checking if the color can be assigned to the state.

        Args:
        state (str): The state to be assigned a color.

        Returns:
        str: The color to be assigned to the state.
        """
        for color in self.colors:
            if self.promising(state, color):
                return color

    # Function to start the map coloring process
    def start(self):
        """
        This function starts the map coloring process by printing the map, assigning colors to each state,
        and printing the solution.
        """
        print(Fore.BLUE+"\n\n\t\tThe Graph Is ")
        self.print_graph()
        print("\n\n")
        for state in self.states:
            self.colors_of_states[state] = self.get_color_for_state(state)
            print(
                f"Color Used For State {state} is {self.colors_of_states[state]}")
        print(Fore.BLUE+"\n\n\t\tThe Solution Is - ")
        for key in self.colors_of_states:
            print(Fore.BLUE+key + Fore.WHITE +
                  ' -> ', self.colors_of_states[key])

# Create an instance of the map_coloring class and start the map coloring process
temp = map_coloring()
temp.start()