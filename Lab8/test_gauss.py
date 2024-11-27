"""
author: Dominik Cedro
date: 20.11.2024
description: Lab 8 - solving equations with naive Gauss elimination.
"""

import numpy as np
from scipy.linalg import solve
from gauss_elimination import naive_gauss_elimination
# Coefficients of the equations
A = np.array([
    [10, 2, -1],
    [4, 5, -2],
    [3, -1, 2]
], dtype=float)

# Constants on the right-hand side
b = np.array([27, 15, 10], dtype=float)

def test_with_numpy(A,b):
    solution_function = naive_gauss_elimination(A,b)
    solution_numpy = solve(A, b)
    # print(solution_numpy, solution_function)
    for func, numpy in zip(solution_function, solution_numpy):
        assert func == numpy
    print("Tested with numpy 'solve', successful")
import numpy as np

def test_with_empiric(A, b, solutions):
    # defined function for use with those equations
    def function(coefficients, rhs, solution):
        left_side = np.dot(coefficients, solution)
        right_side = rhs
        assert np.isclose(left_side, right_side)


    for index, row in enumerate(A):
        function(row, b[index], solutions)
    print("Tested with empirical, successful")

# Example usage
if __name__ == "__main__":
    pass
