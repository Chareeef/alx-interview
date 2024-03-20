#!/usr/bin/python3
"""
Implementation of a solution to the Minimum Operations problem
Refer to the README to read the problem's detailed explanation
"""


def is_prime(n: int) -> bool:
    """Return whether n is prime or not"""

    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed
    to result in exactly `n` H characters in the file.

    Args:
        n (int): The desired number of H characters in the file.

    Returns:
        int: The minimum number of operations required.
        If n is impossible to achieve or no operations are needed, return 0.
    """

    # If n is not an int
    if not type(n) is int:
        return 0

    # We can't achieve n if n < 1
    # And if n == 1, it's exactly the initial state so we do nothing
    if n <= 1:
        return 0

    # If n is prime we can only get it by pasting it n times
    if is_prime(n):
        return n

    # Initialize Divisor and Prime Factors Sum
    divisor = 2
    factors_sum = 0

    # Extract n's Prime Factors Sum
    num = n
    while num > 1:
        while num % divisor == 0:
            factors_sum += divisor
            num //= divisor
        divisor += 1

    # Return the minimum required operations which is the n's PF Sum
    return factors_sum
