"""
author: Dominik Cedro
date: 20.11.2024
description: Lab 8 - solving equations with naive Gauss elimination.
"""

import numpy as np
from icecream import ic


def forward_elimination(A, b):
    n = len(b) # lenght of b matrix (3?)
    # reshape b into column and horizontal stack both
    Ab = np.hstack([A, b.reshape(-1, 1)])
    # Forward Elimination
    for i in range(n):
        # Make the diagonal contain all 1's
        Ab[i] = Ab[i] / Ab[i, i]
        # print(f'Ab i  is {Ab[i]}')
        for j in range(i + 1, n):
            Ab[j] = Ab[j] - Ab[j, i] * Ab[i]
            # print(f'Ab  j s {Ab[j]}')
    return Ab


def back_substitution(Ab):
    n = Ab.shape[0]
    # ic(n)
    x = np.zeros(n)
    # ic(x)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.sum(Ab[i, i + 1:n] * x[i + 1:n])
        # ic(x[i])
    return x


def naive_gauss_elimination(A, b):
    Ab = forward_elimination(A, b)
    return back_substitution(Ab)


# I use arrays to store coefficients of the equations, right hand side is stored as separate column in matrix B
if __name__ == "__main__":
    pass



