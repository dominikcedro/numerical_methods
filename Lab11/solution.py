"""
author: Dominik Cedro
date: 18.12.2024
description: File contains logic to perform three body problem calculations.
"""

import numpy as np
from scipy.integrate import solve_ivp

def three_body_system(t, y, G, m1, m2, m3):
    """
    Defines the system of differential equations for the three-body problem.

    :param t: Time variable.
    :type t: float
    :param y: Array containing positions and velocities of the three bodies.
    :type y: list of float
    :param G: Gravitational constant.
    :type G: float
    :param m1: Mass of the first body.
    :type m1: float
    :param m2: Mass of the second body.
    :type m2: float
    :param m3: Mass of the third body.
    :type m3: float
    :return: Derivatives of positions and velocities.
    :rtype: list of float
    """
    x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3 = y

    r12 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    r13 = np.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    r23 = np.sqrt((x3 - x2)**2 + (y3 - y2)**2)

    ax1 = G * m2 * (x2 - x1) / r12**3 + G * m3 * (x3 - x1) / r13**3
    ay1 = G * m2 * (y2 - y1) / r12**3 + G * m3 * (y3 - y1) / r13**3
    ax2 = G * m1 * (x1 - x2) / r12**3 + G * m3 * (x3 - x2) / r23**3
    ay2 = G * m1 * (y1 - y2) / r12**3 + G * m3 * (y3 - y2) / r23**3
    ax3 = G * m1 * (x1 - x3) / r13**3 + G * m2 * (x2 - x3) / r23**3
    ay3 = G * m1 * (y1 - y3) / r13**3 + G * m2 * (y2 - y3) / r23**3

    return [vx1, vy1, vx2, vy2, vx3, vy3, ax1, ay1, ax2, ay2, ax3, ay3]

G = 1
m1 = 1
m2 = 1
m3 = 1

initial_positions = [-0.97000436, 0.24308753, 0, 0, 0.97000436, -0.24308753]
initial_velocities = [0.466203685, 0.432365730, -0.93240737, -0.86473146, 0.466203685, 0.432365730]
y0 = initial_positions + initial_velocities

t_span = [0, 20]
t_eval = np.linspace(0, 20, 1000)

solution = solve_ivp(three_body_system, t_span, y0, t_eval=t_eval, args=(G, m1, m2, m3), rtol=1e-10, atol=1e-10)

np.savez('three_body_solution.npz', t=solution.t, y=solution.y)