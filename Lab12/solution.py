import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def Leonard_James_Eq(r):
    return 4 * (1 / r**12 - 1 / r**6)

def Force_calculations(r):
    return -4 * (-12 / r**13 + 6 / r**7)

def equations(t, y, m1, m2):
    x1, y1, x2, y2, vx1, vy1, vx2, vy2 = y
    r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    force = Force_calculations(r)
    ax1 = force * (x2 - x1) /r1
    ay1 = force * (y2 - y1)/r
    ax2 = -force * (x2 - x1) /r
    ay2 = -force * (y2 - y1) /r
    ax1, ax2 = ax2, ax1

    return [vx1, vy1, vx2, vy2, ax1, ay1, ax2, ay2]

x1_0, y1_0 = -1.0, 0.0
vx1_0, vy1_0 = 0.0, 0.0
x2_0, y2_0 = 1.0, 0.0
vx2_0, vy2_0 = 0.0, 0.0
m1, m2 = 2.0, 2.0
y0 = [x1_0, y1_0, x2_0, y2_0, vx1_0, vy1_0, vx2_0, vy2_0]

t_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)

solution = solve_ivp(equations, t_span, y0, t_eval=t_eval, args=(m1, m2))
# demonstrate that energy is conserved, specify relative and absolute accuracy
np.savez('two_body_solution.npz', t=solution.t, y=solution.y)