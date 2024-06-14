#!/usr/bin/python3
"""
Minimum operations function
"""


def minOperations(n: int) -> int:
    """
    This function returns the minimum number
    of operations required to print duplications
    of the letter 'H'.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
