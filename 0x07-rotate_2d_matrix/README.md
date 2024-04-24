# Rotate 2D Matrix

## Introduction
Welcome to the Rotate 2D Matrix task! This problem is an exciting challenge that allows us to dive into the world of matrices and rotations. As a software engineering student, I am thrilled to tackle this problem head-on and demonstrate the power of Python.

## Problem Statement
The task at hand is to rotate an n x n 2D matrix 90 degrees clockwise, with the rotation being performed in-place. This means we won't be creating a new matrix but rather modifying the existing one.

## Approach
To accomplish this task, we need to understand the concept of transposing a matrix and then reversing each row. Transposing a matrix involves swapping its rows and columns. In our case, transposing the matrix will prepare it for the clockwise rotation. After transposing, we reverse each row to achieve the desired rotation.

## Implementation
Our function `rotate_2d_matrix(matrix)` will take the given matrix as input and rotate it in place. We won't return anything from the function, as the matrix will be modified directly. The provided prototype is:

```python
def rotate_2d_matrix(matrix):
    # Implementation goes here
```

## Example
Let's illustrate the task with an example:

Given matrix:
```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

After rotating it 90 degrees clockwise, the expected output should be:
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Conclusion
I'm excited to dive into my code editor and start implementing the solution for this task. By applying the concepts of matrix manipulation, we'll be able to rotate the 2D matrix effortlessly. Let's embark on this journey and conquer the Rotate 2D Matrix challenge!
