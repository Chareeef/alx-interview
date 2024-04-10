#!/usr/bin/python3
"""N Queens problem"""
import sys

total_solutions = []


def solve_nqueens(board, N, solution, row):
    """Solve N Queens problem"""

    # Solution found
    if row == N:
        print(solution)
        global total_solutions
        total_solutions.append(solution)
        return

    # Try each column in row
    for col in range(N):
        # If the case is safe
        if is_safe(board, N, row, col):
            # Fill the chessboard square with 1
            board[row][col] = 1

            # Update solution
            solution.append([row, col])

            # Recursive call to solve
            solve_nqueens(board, N, solution, row + 1)

            # Backtrack square and empty the filled chessboard square
            solution.pop()
            board[row][col] = 0


def is_safe(board, N, row, col):
    """Return whether a chessboard square is safe or not"""

    # Go upwards in three directions
    up_row = row
    left_col = col
    right_col = col

    while up_row >= 0:
        # If a square is filled vertically above board[row][col]
        if board[up_row][col] == 1:
            return False

        # If a square is filled in left diagonale above board[row][col]
        if left_col >= 0 and board[up_row][left_col] == 1:
            return False

        # If a square is filled in right diagonale above board[row][col]
        if right_col < N and board[up_row][right_col] == 1:
            return False

        # Move upwards by one in the 3 directions
        up_row -= 1
        left_col -= 1
        right_col += 1

    # The square is safe
    return True


if __name__ == '__main__':

    # Check number of arguments
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    # Check that N must is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    # Check N is smaller than 4
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    # Create board
    board = [[0] * N for _ in range(N)]
    solve_nqueens(board, N, [], 0)
