# N Queens Problem

## Introduction

The N Queens problem is a classic chess puzzle where the objective is to place N non-attacking queens on an N×N chessboard. 

## Problem Statement

We need to write a program in Python that solves the N Queens problem. The usage of the program should be as follows:

```
Usage: nqueens N
```

- If the user calls the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status 1.
- Where N must be an integer greater than or equal to 4.
- If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status 1.
- If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status 1.
- The program should print every possible solution to the problem.
- One solution per line.
- The format should match the given examples.

## Example

```
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

```
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Constraints

- We are only allowed to import the sys module.

Let's solve it! 😁
