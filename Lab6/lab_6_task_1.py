"""
author: Dominik Cedro
date: 06.11.2024
"""
import numpy as np
from matplotlib import pyplot as plt
from icecream import ic
from scipy.optimize import root_scalar

### TASK 1 - define function and plot for graphical interpretation


def flow_function(g, H, t, L):
    solution = np.sqrt(2 * g * H) * np.tanh(((np.sqrt(2 * g * H))/(2 * L)) * t)
    return solution


L = 5
t = 3
g = 9.81
target_v = 4

list_H = [i for i in range(0,50,1)]
list_V = [flow_function(g, H, t, L) for H in list_H]

target_v = 4
closest_index = np.argmin(np.abs(np.array(list_V) - target_v))
closest_H = list_H[closest_index]
closest_V = list_V[closest_index]
print(f"Optimal H via np.argmin: {closest_H}")

plt.figure(figsize=(10, 6))
plt.plot(list_H, list_V, marker='o', linestyle='-', color='blue')
plt.scatter([closest_H], [closest_V], color='red', zorder=5)
plt.annotate(f'H={closest_H}, V={closest_V:.2f}', (closest_H, closest_V), textcoords="offset points", xytext=(10,-10), ha='center')
plt.xlabel('H')
plt.ylabel('V')
plt.title('Flow Function V as a Function of H')
plt.grid(True)
plt.show()

### TASK 2 - bisection function created for root search


def bisection_function(flow_function, x_low, x_high, previous_estimate, des_accuracy):
    # ic("function run")
    new_estimate = (x_low + x_high) / 2
    error = np.abs((new_estimate - previous_estimate) / new_estimate) * 100  # error in percents
    # ic(x_low, x_high, new_estimate, error)
    if error < des_accuracy:
        return new_estimate  # terminate
    position = flow_function(g, x_low, t, L) - target_v
    new_position = flow_function(g, new_estimate, t, L) - target_v
    # ic(position, new_position)
    if position * new_position < 0:
        return bisection_function(flow_function, x_low, new_estimate, new_estimate, des_accuracy)
    else:
        return bisection_function(flow_function, new_estimate, x_high, new_estimate, des_accuracy)


xl = 0
xu = 50

optimal_H_bisection = bisection_function(flow_function, xl, xu, 0, 0.01)
print(f"Root found with bisection: {round(optimal_H_bisection,5)}")

### TASK 3 - NEWTON method

def f_prime(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def newtons_method(x0, f, f_prime, tolerance, epsilon, max_iterations, *args):

    for _ in range(max_iterations):
        y = f(x0, *args)
        yprime = f_prime(lambda H: f(H, *args), x0)

        if abs(yprime) < epsilon:
            break

        x1 = x0 - y / yprime

        if abs(x1 - x0) <= tolerance:
            return x1

        x0 = x1

    return None

initial_guess = 1
tolerance = 1e-6
epsilon = 1e-6
max_iterations = 100

root = newtons_method(initial_guess, lambda H, g, t, L: flow_function(g, H, t, L) - target_v, f_prime, tolerance, epsilon, max_iterations, g, t, L)
print(f"Root found with Newton method: {round(root,5)}")
optimal_H_newton= root

### TASK 4 - use of scipy library for root search

def target_function(H):
    return flow_function(g, H, t, L) - target_v

result = root_scalar(target_function, bracket=[0, 50], method='brentq')
optimal_H_scipy = result
if result.converged:
    print(f"Root found with scipy: {round(result.root,5)}")
else:
    print("Root finding did not converge")


