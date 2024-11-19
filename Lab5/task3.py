"""
both series when summed toghether yield a result that satisfies the assumption
"""
import numpy as np
import scipy.misc
from matplotlib import pyplot as plt


def function_sin(x):
    power = np.sin(2 * x)
    return np.e ** power


def calculate_second_derivativel(x, h):
    inner = function_sin(x-h/2) + function_sin(x + h/2) - 2 * function_sin(x)
    inner *= 4
    return inner/ (h**2)


def calculate_derivative_analytical(x):
    return scipy.misc.derivative(function_sin, x, dx=1e-6, n=2)


x_value = 0.5
derivative_second_a = calculate_derivative_analytical(x_value)
print(f"The derivative of function_sin at x = {x_value} is {round(derivative_second_a,3)}")

list_of_errors_derivative_second = []
list_of_errors_sided = []
h_values = []

for n in range(1, 11,):
    h = 10 ** (-n)
    derivative_second= calculate_second_derivativel(x_value, h)
    error_derivative_second= abs(derivative_second_a - derivative_second)
    list_of_errors_derivative_second.append(error_derivative_second)
    h_values.append(h)

min_error_index = np.argmin(list_of_errors_derivative_second)
optimal_h = h_values[min_error_index]
optimal_error = list_of_errors_derivative_second[min_error_index]

plt.figure(figsize=(10, 6))
plt.plot(h_values, list_of_errors_derivative_second, marker='o', linestyle='-', color='blue', label='Central Difference')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('Absolute Error')
plt.title('Absolute Error of Empirical Derivative as a Function of h (Log-Log Scale)')
plt.grid(True)
plt.legend()
plt.show()

# print(f"The value of h that minimizes the absolute error is approximately {optimal_h:.2e}")