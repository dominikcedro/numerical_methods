"""
author: Dominik Cedro
date: 27.11.2024
description: Lab 9 - solving differntial equations with euler, midpoint and Range-Kutta methods
"""

import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def equation(x, y):
    """
    equation from instruction lab 9
    """
    return 4 * math.exp(0.8 * x) - (0.5 * y)


def euler_method(f, x0, y0, h, x_end):
    """
        function that uses euler's method for ordinary differential equations

    :param f:
    :param x0:
    :param y0:
    :param h:
    :param x_end:
    :return:
    """
    n_steps = int((x_end - x0) / h) + 1
    x_values = np.linspace(x0, x_end, n_steps)
    y_values = np.zeros(n_steps)
    y_values[0] = y0
    for i in range(1, n_steps):
        y_values[i] = y_values[i-1] + h * f(x_values[i-1], y_values[i-1])
    return x_values, y_values


def midpoint_method(f, x0, y0, h, x_end):
    """
        function that uses midpoint method for ordinary differential equations

    :param f:
    :param x0:
    :param y0:
    :param h:
    :param x_end:
    :return:
    """
    n_steps = int((x_end - x0) / h) + 1
    x_values = np.linspace(x0, x_end, n_steps)
    y_values = np.zeros(n_steps)
    y_values[0] = y0
    for i in range(1, n_steps):
        k1 = f(x_values[i-1], y_values[i-1])
        k2 = f(x_values[i-1] + h / 2, y_values[i-1] + h * k1 / 2)
        y_values[i] = y_values[i-1] + h * k2
    return x_values, y_values


def rk4_method(f, x0, y0, h, x_end):
    """
    function that uses runge kutta method for ordinary differential equations
    :param f:
    :param x0:
    :param y0:
    :param h:
    :param x_end:
    :return:
    """

    n_steps = int((x_end - x0) / h) + 1
    x_values = np.linspace(x0, x_end, n_steps)
    y_values = np.zeros(n_steps)
    y_values[0] = y0
    for i in range(1, n_steps):
        k1 = f(x_values[i-1], y_values[i-1])
        k2 = f(x_values[i-1] + h / 2, y_values[i-1] + h * k1 / 2)
        k3 = f(x_values[i-1] + h / 2, y_values[i-1] + h * k2 / 2)
        k4 = f(x_values[i-1] + h, y_values[i-1] + h * k3)
        y_values[i] = y_values[i-1] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x_values, y_values


x = sp.symbols('x')
y = sp.Function('y')

func = 4 * sp.exp(0.8 * x) - 0.5 * y(x)
differential_eq = sp.Eq(y(x).diff(x), func)
initial_condition = {y(0): 2}
particular_solution = sp.dsolve(differential_eq, y(x), ics=initial_condition)
analytical_solution = particular_solution.subs(x, 4).rhs
print(f"Analytical solution at x = 4: {analytical_solution}")
exact_value = analytical_solution


h_values = np.logspace(-1, -5, 5)
methods = [euler_method, midpoint_method, rk4_method]
method_names = ['Euler', 'Midpoint', 'RK4']
results = []

for h in h_values:
    for method, name in zip(methods, method_names):
        x_values, y_values = method(equation, 0, 2, h, 4)
        computational_cost = len(y_values) * (1 if name == 'Euler' else 2 if name == 'Midpoint' else 4)
        relative_error = abs(y_values[-1] - exact_value) / exact_value
        results.append({
            'method_name': name,
            'computational_cost': computational_cost,
            'h_value': h,
            'relative_error': relative_error
        })

# I will use dataframe to store and operate on results
import pandas as pd
df = pd.DataFrame(results)
print(df)

# Plot the results
plt.figure(figsize=(10, 6))
for name in method_names:
    method_results = df[df['method_name'] == name]
    plt.plot(method_results['computational_cost'], method_results['relative_error'], 'o-', label=name)
plt.xlabel('Computational Cost')
plt.ylabel('Relative Error')
plt.xscale('log')
plt.yscale('log')
plt.title('Error vs. Computational Cost')
plt.legend()
plt.show()