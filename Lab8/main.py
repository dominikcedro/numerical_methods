"""
author: Dominik Cedro
date: 20.11.2024
description: Lab 8 - solving equations with naive Gauss elimination.
"""
import numpy as np

from Lab8.gauss_elimination import naive_gauss_elimination
from Lab8.test_gauss import test_with_empiric, test_with_numpy

### firstly I calculate the

matrix_A = np.array([
        [10, 2, -1],
        [4, 5, -2],
        [3, -1, 2]
    ], dtype=float)

matrix_B = np.array([27, 15, 10], dtype=float)

solutions = naive_gauss_elimination(matrix_A, matrix_B)
test_with_empiric(matrix_A, matrix_B, solutions)
test_with_numpy(matrix_A, matrix_B)