#!/usr/bin/python3
"""Rotate a 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it, in-place, 90° clockwise
    """

    # Matrix dimension
    n = len(matrix)

    # Transpose matrix
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # Reverse each row
    for idx in range(n):
        matrix[idx].reverse()


if __name__ == "__main__":
    matrix = [[1, 2, 3, 'l'],
              [4, 5, 6, 'o'],
              [7, 8, 9, 'o'],
              [10, 11, 12, 'l']]

    for r in matrix:
        print(r)
    rotate_2d_matrix(matrix)
    print('ROTAATE!')
    for r in matrix:
        print(r)
