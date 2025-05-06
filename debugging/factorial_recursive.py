#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): Non-negative integer whose factorial to compute.

    Returns:
        int: The factorial of n (i.e., n!).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
