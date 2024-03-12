#!/usr/bin/python3
"""
Attempt to solve the Lockboxes problem
"""
from collections import deque


def canUnlockAll(boxes):
    """
    Assumptions:
        - Each box may contain keys to other boxes.
        - A key with the same number as a box opens that box.
        - All keys will be positive integers.
        - There can be keys that do not have corresponding boxes.
        - The first box `boxes[0]` is already unlocked.

    Input:
        - boxes: A list of lists representing the boxes and their contents,
                 ex: `[[1, 4, 6], [2], [4, 1], [5, 6, 2], [3], [4, 1], [6]]`.

    Return `True` if all boxes can be opened, else return `False`.
    """

    # Declare a set of currently unlocked boxes's indices
    # and initialize it with `0` as the first box is already unlocked
    open_boxes_idx = {0}

    # Create a queue to keep track of available keys
    # and fill it with the first box's keys
    keyring = deque(boxes[0])

    # Create a set of already used keys
    used_keys = set()

    # Now use Breadth First Search (BFS) to try to open all the boxes

    # Use all the keys we can find as we open the boxes
    while len(keyring) > 0:
        # Take a key
        key = keyring.popleft()

        # Check that we use it for the first time
        if key not in used_keys:

            # Add it as a used key
            used_keys.add(key)

            # Check that it has a corresponding box which stills locked
            if key < len(boxes) and key not in open_boxes_idx:

                # Add the box index as an open box's index
                open_boxes_idx.add(key)

                # If all boxes are unlocked, return True
                if len(open_boxes_idx) == len(boxes):
                    return True

                # Add the keys inside this unlocked box to `keyring`
                keyring.extend(boxes[key])

    # Exiting the `while` means the boxes are not completely unlocked
    return False
