#!/usr/bin/python3
import sys

# Define a recursive function to compute the factorial of a non-negative integer n
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n (n!).
    """
    if n == 0:
        return 1  # Base case: 0! is defined as 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Entry point: Read an integer from command-line arguments and compute its factorial
if __name__ == "__main__":
    # Ensure that the user has provided one command-line argument
    if len(sys.argv) != 2:
        print("Usage: {} <non-negative integer>".format(sys.argv[0]))
        sys.exit(1)

    try:
        # Convert the argument to an integer
        num = int(sys.argv[1])

        # Check that the number is non-negative
        if num < 0:
            raise ValueError("Number must be non-negative.")

        # Compute the factorial and print the result
        f = factorial(num)
        print(f)
    except ValueError as e:
        # Handle the case where the input is not a valid non-negative integer
        print("Error:", e)
        sys.exit(1)
