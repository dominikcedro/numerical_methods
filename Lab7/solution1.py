"""
author: Dominik Cedro
date: 13.11.2024
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad

A_PARAM = 0
B_PARAM = 1
N_ONCE = 100
N_ITERATIONS = 10000
def function_f(x):
    nominator = 1
    denominator = np.sqrt((x**2) + 1)
    return nominator/denominator


def rectangular_method(function, a, b):
    return function(a) * (b - a)


def rectangular_over_n(function_f, a, b, n):
    h = (b - a) / n
    total_rect = 0
    for k in range(n):
        total_rect += function_f(a + k * h) * h
    return total_rect


def trapezoid_method(function, a,b):
    result = (function(a) + function(b))/2
    result *= (b- a)
    return result


def trapezoid_over_n(function, a, b, n):
    h = (b - a) / (n - 1)
    total_trap = 0.5 * (function(a) + function(b))
    for k in range(1, n - 1):
        total_trap += function(a + k * h)
    total_trap *= h
    return total_trap


def simpson_over_n(function, a, b, n):
    if n % 2 == 0:
        n += 1
    h = (b - a) / (n - 1)
    total_simpson = function(a) + function(b)
    for k in range(1, n - 1, 2):
        total_simpson += 4 * function(a + k * h)
    for k in range(2, n - 2, 2):
        total_simpson += 2 * function(a + k * h)
    total_simpson *= h / 3
    return total_simpson

a = A_PARAM
b = B_PARAM
n = N_ONCE

analytical_i, error = quad(function_f, 0, 1) # analytical


rectangular_i_sum = rectangular_over_n(function_f, a, b, n)
absolute_error_rectangular = abs(analytical_i - rectangular_i_sum)
print(f"Value for rectangular: {round(rectangular_i_sum,5)}")
print(f"Absolute error rectangular: {round(absolute_error_rectangular,5)}")

trapezoid_i_sum = trapezoid_over_n(function_f, a, b, n)
absolute_error_trapezoid = abs(analytical_i - trapezoid_i_sum)
print(f"Value for trapezoid: {round(trapezoid_i_sum,5)}")
print(f"Absolute error trapezoid: {(absolute_error_trapezoid)}")

simpson_i_sum = simpson_over_n(function_f, a, b, n)
absolute_error_simpson = abs(analytical_i - simpson_i_sum)
print(f"Value for Simpson: {round(simpson_i_sum,5)}")
print(f"Absolute error Simpson: {(absolute_error_simpson)}")

solutions_rectangular = []
solutions_trapezoid = []
solutions_simpson = []
list_of_n = []
for j in range(10, N_ITERATIONS):
    n = j
    list_of_n.append(n)
    absolute_error_rectangular = abs(analytical_i - rectangular_over_n(function_f, a, b, n))
    absolute_error_trapezoid = abs(analytical_i - trapezoid_over_n(function_f, a, b, n))
    absolute_error_simpson = abs(analytical_i - simpson_over_n(function_f, a, b, n))
    solutions_trapezoid.append(absolute_error_trapezoid)
    solutions_rectangular.append(absolute_error_rectangular)
    solutions_simpson.append(absolute_error_simpson)

plt.figure(figsize=(10, 6))
plt.plot(list_of_n,solutions_rectangular , linestyle='-', color='brown', label='Rectangular')
plt.plot( list_of_n,solutions_trapezoid,  linestyle='-', color='orange', label='Trapezoid')
plt.plot(list_of_n, solutions_simpson,  linestyle='-', color='green', label='Simpson')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Absolute Error')
plt.title('Absolute Error of chosen functions of Integral (Log-Log Scale)')
plt.grid(True)
plt.legend()
plt.show()
