#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n: int) -> int:
    """Return the minimum number of operations needed to result in n H chars.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed to achieve n H characters.
    """
    if n <= 0:
        return 0
    operations = 0
    i = 2
    while i <= n:
        operations += 1
        while n % i == 0:
            n = n / i
            operations += 1
        i += 1
    return operations
