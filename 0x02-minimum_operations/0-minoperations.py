#!/usr/bin/python3
"""File that uses the min of operations"""


def minOperations(n):
    """
    given a number n, this method calculates the fewest name of operations
    """
    minOps = 0
    divisor = 2
    while (isinstance(n, int) and n > 1):
        while (n % divisor):
            divisor += 1
        minOps += divisor
        n = n // divisor
    return minOps
