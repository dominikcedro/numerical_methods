"""
author: Dominik Cedro
date: 27.11.2024
description: Lab 9 - solving differntial equations with euler, midpoint and Range-Kutta methods
"""

# TODO(1) define the function
import math
import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def equation(x, y):
    """
    equation from instruction lab 9
    """
    return 4 * math.exp(0.8 * x) - (0.5 * y)


# TODO(2 ) sympy

x = sp.symbols('x')
y = sp.Function('y')(x)
differential_eq = sp.Eq(y.diff(x), 4 * sp.exp(0.8 * x) - 0.5 * y)

solution = sp.dsolve(differential_eq, y)

C1 = sp.symbols('C1')
initial_condition = solution.rhs.subs({x: 0, y: 2})
C1_value = sp.solve(initial_condition, C1)[0]
particular_solution = solution.rhs.subs(C1, C1_value)
y_at_4 = particular_solution.subs(x, 4)
print(f"The solution to the differential equation at x = 4 is: {y_at_4}")



def equation(x, y):
    """
    equation from instruction lab 9
    """
    return 4 * math.exp(0.8 * x) - (0.5 * y)


# TODO(3) euler method
def euler_method(f, x0, y0, h, x_end):
    x, y = x0, y0
    steps = 0
    while x < x_end:
        y += h * f(x, y)
        x += h
        steps += 1
    return y, steps


# TODO(3) euler method

# TODO(4) midpoint method

# TODO(5) Runge-Kutta method

# TODO(6) plot error/cost
