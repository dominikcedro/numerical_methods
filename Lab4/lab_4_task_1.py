import numpy as np
import scipy
from matplotlib import pyplot as plt

def function_f(x):
    result = ((-0.1 * (x ** 4)) + (-0.15 * (x ** 3))
              + (-0.5 * (x ** 2)) - (0.25 * x) + 1.2)
    return result

def calculate_derivative_empirical(x, h):
    result = (function_f(x + h) - function_f(x)) / h
    return result

def calculate_derivative_analytical(x):
    return scipy.misc.derivative(function_f, x, dx=1e-6)

x_value = 0.5
derivative_a = calculate_derivative_analytical(x_value)
print(f"The derivative of function_f at x = {x_value} is {round(derivative_a,3)}")

list_of_errors = []
h_values = []

for n in range(1, 11):
    h = 10 ** (-n)
    derivative_e = calculate_derivative_empirical(x_value, h)
    print(f"The empirical derivative for h: {h} and x: {x_value} equals: {round(derivative_e,3)}")
    error_e = abs(derivative_a - derivative_e)
    list_of_errors.append(error_e)
    h_values.append(h)
    print(f"Error is {error_e}")

plt.figure(figsize=(10, 6))
plt.plot(h_values, list_of_errors, marker='o', linestyle='-', color='blue')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('Absolute Error')
plt.title('Absolute Error of Empirical Derivative as a Function of h (Log-Log Scale)')
plt.grid(True)
plt.show()
