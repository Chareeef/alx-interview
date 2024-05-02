#!/usr/bin/python3
"""The 'Making Change' problem
"""


def makeChange(coins, total):
    """Given a pile of `coins` (List of integers) of different values,
    Return the fewest number of coins needed to meet a given `total`i
    or -1 if there is no possibility to make change
    """

    # If `total` is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize fewest needed number of coins to 0
    fewest_coins = 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Loop through coins from higher to lower values
    for c in coins:

        # Keep subtracting it from `total` until it becomes impossible
        while total - c >= 0:
            total -= c

            # Add a coin to fewest_coins
            fewest_coins += 1

        # If `total` became 0, so the change was successfully made
        if total == 0:
            return fewest_coins

    # Completing the for loop without returning means we can't make change
    else:
        return -1
