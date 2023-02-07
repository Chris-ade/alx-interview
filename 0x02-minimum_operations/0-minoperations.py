#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n: int) -> int:
    """Return the minimum number of operations needed to result in n H chars.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed to achieve n H characters.
    """
    if n < 2:
        return 0
    operations = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                operations.append(i)
    return sum(operations)
