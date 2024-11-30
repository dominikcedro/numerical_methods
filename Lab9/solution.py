"""
author: Dominik Cedro
date: 27.11.2024
description: Lab 9 - solving differntial equations with euler, midpoint and Range-Kutta methods
"""

import math
import sympy as sp
import matplotlib.pyplot as plt

def equation(x, y):
    """
    equation from instruction lab 9
    """
    return 4 * math.exp(0.8 * x) - (0.5 * y)



def euler_method(f, x0, y0, h, x_end):
    x, y = x0, y0
    steps = 0
    while x < x_end:
        y += h * f(x, y)
        x += h
        if x >= x_end:
            break
        steps += 1
    print(x)
    return y, steps



def midpoint_method(f, x0, y0, h, x_end):
    x, y = x0, y0
    steps = 0
    while x < x_end:
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        y += k2
        x += h
        if x >= x_end:
            break
        steps += 2
    return y, steps


def runge_kutta_method(f, x0, y0, h, x_end):
    x, y = x0, y0
    steps = 0
    while x < x_end:
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
        if x >= x_end:
            break
        steps += 4
    return y, steps


x = sp.symbols('x')
y = sp.Function('y')(x)
differential_eq = sp.Eq(y.diff(x), 4 * sp.exp(0.8 * x) - 0.5 * y)

solution = sp.dsolve(differential_eq, y)

C1 = sp.symbols('C1')
initial_condition = solution.rhs.subs({x: 0, y: 2})
C1_value = sp.solve(initial_condition, C1)[0]
particular_solution = solution.rhs.subs(C1, C1_value)
exact_value = particular_solution.subs(x, 4).evalf()
print(f'The correct analytical solution at x = 4 is: {exact_value}')
analytical_up = 2 * (20 * math.exp(26/5) - 7)
analytical_dwn = 13 * math.exp(2)
exact_value = analytical_up/analytical_dwn
print(f'The correct analytical solution at x = 4 is: {exact_value}')

x0 = 0
y0 = 2
x_end = 4

h_values = [0.1, 0.01, 0.001, 0.0001]
errors_euler = []
errors_modified_euler = []
errors_runge_kutta = []
costs_euler = []
costs_modified_euler = []
costs_runge_kutta = []

for h in h_values:
    y_euler, steps_euler = euler_method(equation, x0, y0, h, x_end)
    y_modified_euler, steps_modified_euler = midpoint_method(equation, x0, y0, h, x_end)
    y_runge_kutta, steps_runge_kutta = runge_kutta_method(equation, x0, y0, h, x_end)

    error_euler = abs((y_euler - exact_value) / exact_value)
    error_modified_euler = abs((y_modified_euler - exact_value) / exact_value)
    error_runge_kutta = abs((y_runge_kutta - exact_value) / exact_value)

    errors_euler.append(error_euler)
    errors_modified_euler.append(error_modified_euler)
    errors_runge_kutta.append(error_runge_kutta)

    costs_euler.append(steps_euler)
    costs_modified_euler.append(steps_modified_euler)
    costs_runge_kutta.append(steps_runge_kutta)


plt.figure(figsize=(10, 6))
plt.plot(costs_euler, errors_euler, marker='o', linestyle='-', color='r', label="Euler's Method")
plt.plot(costs_modified_euler, errors_modified_euler, marker='s', linestyle='--', color='b', label="Midpoint Method")
plt.plot(costs_runge_kutta, errors_runge_kutta, marker='^', linestyle='-.', color='g', label="Runge-Kutta Method")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Computational Cost (Number of Function Evaluations)')
plt.ylabel('Relative Error')
plt.title('Log-Log Plot of Relative Error vs Computational Cost')
plt.grid(True)
plt.legend()
plt.show()

y_euler, steps_euler = euler_method(equation, x0, y0, 1, x_end)
print(y_euler,steps_euler)
