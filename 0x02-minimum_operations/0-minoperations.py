#!/usr/bin/env python3
"""
Implementation of a solution to the Minimum Operations problem
Refer to the README to read the problem's detailed explanation
"""
from collections import deque


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

    # We can't achieve n if n < 1
    # And if n == 1, it's exactly the initial state so we do nothing
    if n <= 1:
        return 0

    # Initially, we have one 'H'
    # And we obviously must Copy All and Paste (2 operations) at least once

    # Current state:
    state = {'characters': 2, 'toPaste': 1, 'operations': 2}

    # Queue to traverse all possible states
    states_queue = deque()

    # Append the current state
    states_queue.appendleft(state)

    currently_copied = 1  # Equal to the current state['toPaste']

    solution = n  # The worst: Copy All + `n - 1` Paste = n

    # Traverse all possible states using Breadth First Search
    # Until we exceed `n` 'H' characters
    while len(states_queue) > 0:
        current_state = states_queue.popleft()

        # Store current stats
        characters = current_state['characters']
        toPaste = current_state['toPaste']
        operations = current_state['operations']

        # Add a sole Paste operation if relevant
        if characters + toPaste <= n:
            # This operation only adds `toPaste` to the existing characters
            new_state = {
                'characters': characters + toPaste,
                'toPaste': toPaste,
                'operations': operations + 1
            }

            # Append it if it may provide a better solution
            if new_state['operations'] < solution:
                # Update solution if characters == n
                if new_state['characters'] == n:
                    solution = new_state['operations']
                else:
                    states_queue.append(new_state)

        # Add a Copy All/Paste combo if relevant
        if toPaste == currently_copied and characters * 2 <= n:
            # The combination Copy All/Paste doubles the characters
            new_state = {
                'characters': characters * 2,
                'toPaste': characters,
                'operations': operations + 2
            }

            # Append it if it may provide a better solution
            if new_state['operations'] < solution:
                # Update solution if characters == n
                if new_state['characters'] == n:
                    solution = new_state['operations']
                else:
                    states_queue.append(new_state)

    # Return the solution
    return solution
