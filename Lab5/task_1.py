"""
author: Dominik Cedro
"""
import numpy as np
import scipy.misc
from matplotlib import pyplot as plt


def function_sin(x):
    power = np.sin(2 * x)
    return np.e ** power


def calculate_derivative_empirical_sided(x, h):
    result = (function_sin(x + h) - function_sin(x)) / h
    return result


def calculate_derivative_empirical_central(x, h):
    result = (function_sin(x + h/2) - function_sin(x - h/2)) / h
    return result


def calculate_derivative_analytical(x):
    return scipy.misc.derivative(function_sin, x, dx=1e-6)


def calculate_optimal_h():
    epsilon = np.finfo(float).eps
    optimal_h = 2 * ((3*epsilon))**(1/3)
    return optimal_h


x_value = 0.5
derivative_a_2 = calculate_derivative_analytical(x_value)
print(f"The derivative of function_sin at x = {x_value} is {round(derivative_a_2,3)}")

list_of_errors_central = []
list_of_errors_sided = []
h_values = []

for n in range(1, 11,):
    h = 10 ** (-n)
    derivative_e_central = calculate_derivative_empirical_central(x_value, h)
    error_e_central = abs(derivative_a_2 - derivative_e_central)
    list_of_errors_central.append(error_e_central)

    derivative_e_side = calculate_derivative_empirical_sided(x_value, h)
    error_e_sided = abs(derivative_a_2 - derivative_e_side)
    list_of_errors_sided.append(error_e_sided)
    h_values.append(h)

min_error_index = np.argmin(list_of_errors_central)
optimal_h_empirical = h_values[min_error_index]
optimal_error = list_of_errors_central[min_error_index]

plt.figure(figsize=(10, 6))
plt.plot(h_values, list_of_errors_central, marker='o', linestyle='-', color='blue', label='Central Difference')
plt.plot(h_values, list_of_errors_sided, marker='o', linestyle='-', color='red', label='Sided Difference')
plt.scatter([optimal_h_empirical], [optimal_error], color='green', zorder=5)
plt.annotate(f'h={optimal_h_empirical:.2e}', (optimal_h_empirical, optimal_error), textcoords="offset points", xytext=(10,-10), ha='center')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('Absolute Error')
plt.title('Absolute Error of Empirical Derivative as a Function of h (Log-Log Scale)')
plt.grid(True)
plt.legend()
plt.show()

print(f"The value of h that minimizes the absolute error empirically is approximately {optimal_h_empirical:.2e}")
optimal_h_analytical = calculate_optimal_h()
print(f"The value of h that minimizes the absolute error analytically is approximately {optimal_h_analytical:.2e}")