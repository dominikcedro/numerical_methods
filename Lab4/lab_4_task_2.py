import numpy as np
import scipy.misc
from matplotlib import pyplot as plt

def function_sin(x):
    power = np.sin(2 * x)
    return np.e ** power

def calculate_derivative_empirical_2(x, h):
    result = (function_sin(x + h) - function_sin(x)) / h
    return result

def calculate_derivative_analytical_2(x):
    return scipy.misc.derivative(function_sin, x, dx=1e-6)

x_value = 0.5
derivative_a_2 = calculate_derivative_analytical_2(x_value)
print(f"The derivative of function_sin at x = {x_value} is {round(derivative_a_2,3)}")

list_of_errors = []
h_values = []

for n in range(1, 11):
    h = 10 ** (-n)
    derivative_e = calculate_derivative_empirical_2(x_value, h)
    print(f"The empirical derivative for h: {h:.2e} and x: {x_value:.2e} equals: {round(derivative_e,3)}")
    error_e = abs(derivative_a_2 - derivative_e)
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