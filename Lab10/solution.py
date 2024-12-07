"""
author: Dominik Cedro
date: 07.12.2024
description: Solution to laboratory 10, Newton's second law of motion
in context of Lenard-Jones potential. Integration.
"""
import scipy.misc
import numpy as np
from icecream import ic


def leonard_james(x:float | int) -> float:
    result = 4 * ((x**(-12))-(x**(-6)))
    return result


def force_function(x:float | int) -> float:
    derivative = scipy.misc.derivative(leonard_james, x, dx=1e-6)
    negative_differential = -derivative
    return negative_differential

# Verlet algorythm - setup of variables

x_0 = 2
v_0 = 0
m = 1
delta_t = 1

# Verlet - initialize lists to store results

position_list = []
time_list = []
velocity_list = []
kinetic_e_list = []
potential_e_list = []
total_e_list = []

initial_a = force_function(x_0) / m
ic(initial_a)

# verlet
# TODO(3) Integrate the Newtonian equation of motions  []
# TODO(4) Experiment with different values of the integration step dt []
# TODO(5) Prepare presentation of data []
