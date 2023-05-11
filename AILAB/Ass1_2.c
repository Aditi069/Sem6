// This program generates a magic square of odd order using the Siamese method.
// A magic square is a square grid filled with distinct positive integers in such a way that each cell contains a unique integer and the sum of the integers in each row, column, and diagonal is equal.

#include <stdio.h>

// Declare global variable N
int N;

// Function to display the magic square
void dis(int ms[N][N])
{
    /*
    This function takes a 2D array of size N x N as input and displays it in the form of a magic square.
    
    Args:
    ms (int): A 2D array of size N x N.
    */
    
    // Loop through each row
    for (int i = 0; i < N; i++)
    {
        // Loop through each column
        for (int j = 0; j < N; j++)
        {
            // Print the value of the current cell
            printf("%3d ", ms[i][j]);
        }
        // Move to the next row
        printf("\n");
    }
}

// Function to create the magic square
void createe(int n)
{
    /*
    This function generates a magic square of odd order using the Siamese method.
    
    Args:
    n (int): The order of the magic square to be generated.
    */
    
    // Declare a 2D array of size N x N
    int ms[N][N];
    
    // Initialize all cells to 0
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            ms[i][j] = 0;
        }
    }
    
    // Set the starting position to the middle of the top row
    int i = n / 2;
    int j = n - 1;
    
    // Loop through each number from 1 to N^2
    for (int num = 1; num <= n * n;)
    {
        // If the current position is out of bounds, wrap around to the opposite side
        if (i == -1 && j == n)
        {
            j = n - 2;
            i = 0;
        }
        else
        {
            if (j == n)
            {
                j = 0;
            }
            if (i < 0)
            {
                i = n - 1;
            }
        }

        // If the current cell is already filled, move down two rows and one column to the right
        if (ms[i][j])
        {
            j = j - 2;
            i++;
            continue;
        }
        // Otherwise, fill the cell with the current number
        else
        {
            ms[i][j] = num++;
        }
        // Move one row up and one column to the right
        j++;
        i--;
    }
    // Display the generated magic square
    dis(ms);
}

// Main function
int main()
{
    /*
    This is the main function that prompts the user to enter an odd number and generates a magic square of that order using the Siamese method.
    */
    
    // Prompt the user to enter an odd number
    printf("Enter odd number: ");
    // Read the input from the user and store it in N
    scanf("%d", &N);
    // If N is odd, generate the magic square
    if (N % 2 != 0)
        createe(N);
    // Otherwise, print an error message
    else
        printf("Invalid input.");
    return 0;
}