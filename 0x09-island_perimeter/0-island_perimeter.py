#!/usr/bin/python3
"""Solution to the Island Perimeter problem
"""


def island_perimeter(grid):
    """Calculate and return the perimeter of the island within the grid
    The grid's specifications are detailed in the README
    """

    # The island perimeter is the sum of edges of each land cell,
    # Knowing that for each land cell, cell_edges = 4 - adjacent_ones

    # So let's compute that perimeter
    perimeter = 0
    N = len(grid)

    for i in range(N):
        for j in range(N):

            # If we hit a land cell
            if grid[i][j] == 1:

                # Count adjacent 1's
                adjacent_ones = 0

                # Check Up
                if i > 0 and grid[i - 1][j] == 1:
                    adjacent_ones += 1

                # Check Down
                if i < N - 1 and grid[i + 1][j] == 1:
                    adjacent_ones += 1

                # Check Right
                if j < N - 1 and grid[i][j + 1] == 1:
                    adjacent_ones += 1

                # Check Left
                if j > 0 and grid[i][j - 1] == 1:
                    adjacent_ones += 1

                # Update perimeter
                perimeter += 4 - adjacent_ones

    # Return perimeter
    return perimeter
