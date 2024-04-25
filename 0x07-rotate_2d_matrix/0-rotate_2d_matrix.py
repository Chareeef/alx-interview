#!/usr/bin/python3
"""Rotate a 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it, in-place, 90° clockwise
    """

    # Matrix dimension
    n = len(matrix)

    # Loop through matrix cycles
    for x in range(int(n / 2)):
        for y in range(x, n - 1 - x):

            # Store top
            temp = matrix[x][y]

            # To top
            matrix[x][y] = matrix[n - 1 - y][x]

            # To left
            matrix[n - 1 - y][x] = matrix[n - 1 - x][n - 1 - y]

            # To down
            matrix[n - 1 - x][n - 1 - y] = matrix[y][n - 1 - x]

            # To right
            matrix[y][n - 1 - x] = temp


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    for r in matrix:
        print(r)

    rotate_2d_matrix(matrix)

    print('\nROTAATE!\n')
    for r in matrix:
        print(r)
