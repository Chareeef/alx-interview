#!/usr/bin/python3
"""
Generate a Pascal's triangle of a certain height
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal’s triangle of `n` rows.

        - If `n <= 0`: Return an empty list.
        - We assume that `n` is always an integer.

    As an example, for 5 rows, the function returns:

        [
            [1],
            [1,1],
            [1,2,1],
            [1,3,3,1],
            [1,4,6,4,1]
        ]

    """

    # For no rows, return an empty list
    if n <= 0:
        return []

    # Define the list that will contain the rows (lists) of the triangle
    p_triangle = []

    # Loop through and generate each row of the Pascal's triangle
    for row_idx in range(0, n):
        # Define the actual row
        row = []

        # Each row has a length of `row_idx + 1`
        # So let's loop through each row's column
        for col_idx in range(0, row_idx + 1):

            # The extremities of each row are equal to 1
            if col_idx == 0 or col_idx == row_idx:
                row.append(1)

            # Otherwise compute the column value based on the above values
            # The first and second row (if required) won't pass to this `else`
            # So we will always find the `above values` to compute
            else:
                # Compute the actual column value
                col_value = p_triangle[row_idx - 1][col_idx] + \
                    p_triangle[row_idx - 1][col_idx - 1]

                # Append it to the actual row
                row.append(col_value)

        # Append the computed row (list) to the triangle
        p_triangle.append(row)

    # Return the final Pascal's triangle
    return p_triangle
