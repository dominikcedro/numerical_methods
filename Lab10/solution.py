"""
author: Dominik Cedro
date: 07.12.2024
description: Utilizing Verlet algorythm in Newtonian equations.
"""
import os

import numdifftools as nd
import numpy as np
from icecream import ic
import matplotlib.pyplot as plt

def leonard_james(x: float) -> float:
    """
    Representation of Leonard-James potential.
    :param x: float
    :return: result: float
    """
    return 4 * ((x**(-12)) - (x**(-6)))

def force_function(x: float) -> float:
    """
    Calculation of force acting on material point in LJ potential.
    :param x: float
    :return: result: float
    """
    derivative = nd.Derivative(leonard_james)(x)
    return -derivative

def verlet_algorithm(x_0, v_0, m, delta_t, time_range):
    """
    Verlet algorythm returning lists of values of position, velocity, time,
    kinetic energy, potential energy, total energy.
    :param x_0:
    :param v_0:
    :param m:
    :param delta_t:
    :param time_range:
    :return:
    """
    position_list = [x_0]
    velocity_list = [v_0]
    time_list = [0]
    kinetic_e_list = []
    potential_e_list = []
    total_e_list = []

    a_0 = force_function(x_0) / m
    # ic(a_0)

    # initial values so len(time) == len(kinetic_energy)
    ke_0 = 0.5 * m * v_0 ** 2
    pe_0 = leonard_james(x_0)
    total_e_0 = ke_0 + pe_0
    kinetic_e_list.append(ke_0)
    potential_e_list.append(pe_0)
    total_e_list.append(total_e_0)

    for t in np.arange(delta_t, time_range, delta_t):
        v_half = velocity_list[-1] + 0.5 * delta_t * a_0
        x_new = position_list[-1] + delta_t * v_half
        a_new = force_function(x_new) / m
        v_new = v_half + 0.5 * delta_t * a_new

        ke = 0.5 * m * v_new**2
        pe = leonard_james(x_new)
        total_e = ke + pe

        position_list.append(x_new)
        velocity_list.append(v_new)
        time_list.append(t)
        kinetic_e_list.append(ke)
        potential_e_list.append(pe)
        total_e_list.append(total_e)

        a_0 = a_new

    return time_list, position_list, velocity_list, kinetic_e_list, potential_e_list, total_e_list

x_0 = 2
v_0 = 0
m = 1
delta_t_values = [0.01, 0.05, 0.1]
time_range = 10
for delta_t in delta_t_values:
    results = verlet_algorithm(x_0, v_0, m, delta_t, time_range)
    time_list, position_list, velocity_list, kinetic_e_list, potential_e_list, total_e_list = results

    # Plot position as a function of time
    plt.figure(figsize=(10, 6))
    plt.plot(time_list, position_list, label='Position', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title(f'Position vs Time (delta_t={delta_t})')
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join('plots', f'position_vs_time_dt_{delta_t}.png'))
    plt.close()

    # Plot velocity as a function of time
    plt.figure(figsize=(10, 6))
    plt.plot(time_list, velocity_list, label='Velocity', color='green')
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.title(f'Velocity vs Time (delta_t={delta_t})')
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join('plots', f'velocity_vs_time_dt_{delta_t}.png'))
    plt.close()

    # Plot kinetic energy as a function of time
    plt.figure(figsize=(10, 6))
    plt.plot(time_list, kinetic_e_list, label='Kinetic Energy', color='red')
    plt.xlabel('Time')
    plt.ylabel('Kinetic Energy')
    plt.title(f'Kinetic Energy vs Time (delta_t={delta_t})')
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join('plots', f'kinetic_energy_vs_time_dt_{delta_t}.png'))
    plt.close()

    # Plot potential energy as a function of time
    plt.figure(figsize=(10, 6))
    plt.plot(time_list, potential_e_list, label='Potential Energy', color='purple')
    plt.xlabel('Time')
    plt.ylabel('Potential Energy')
    plt.title(f'Potential Energy vs Time (delta_t={delta_t})')
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join('plots', f'potential_energy_vs_time_dt_{delta_t}.png'))
    plt.close()

    # Plot total energy as a function of time
    plt.figure(figsize=(10, 6))
    plt.plot(time_list, total_e_list, label='Total Energy', color='orange')
    plt.xlabel('Time')
    plt.ylabel('Total Energy')
    plt.title(f'Total Energy vs Time (delta_t={delta_t})')
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join('plots', f'total_energy_vs_time_dt_{delta_t}.png'))
    plt.close()

    # Plot phase plot: x(t) vs v(t)
    plt.figure(figsize=(10, 6))
    plt.plot(position_list, velocity_list, label='Phase Plot', color='black')
    plt.xlabel('Position')
    plt.ylabel('Velocity')
    plt.title(f'Phase Plot (delta_t={delta_t})')
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join('plots', f'phase_plot_dt_{delta_t}.png'))
    plt.close()