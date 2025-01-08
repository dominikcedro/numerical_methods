import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def three_body_system(t, y, G, m1, m2, m3):
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

# Define initial conditions and parameters for each scenario
scenarios = [
    {
        "name": "Figure-8",
        "G": 1,
        "masses": [1, 1, 1],
        "initial_positions": [-0.97000436, 0.24308753, 0, 0, 0.97000436, -0.24308753],
        "initial_velocities": [0.466203685, 0.432365730, -0.93240737, -0.86473146, 0.466203685, 0.432365730]
    },
    {
        "name": "Euler",
        "G": 1,
        "masses": [1, 1, 1],
        "initial_positions": [-1, 0, 0, 0, 1, 0],
        "initial_velocities": [0, 0.3, 0, -0.6, 0, 0.3]
    },
    {
        "name": "Lagrange",
        "G": 1,
        "masses": [1, 1, 4],
        "initial_positions": [-1, 0, 0.5, 0.866, 0.5, -0.866],
        "initial_velocities": [0, -0.5, -0.433, -0.25, 0.433, -0.25]
    },
    {
        "name": "Sitnikov",
        "G": 1,
        "masses": [1, 1, 4],
        "initial_positions": [-0.5, 0, 0.5, 0, 0, 0],
        "initial_velocities": [0, -0.6, 0, 0.6, 0.3, 0]
    }
]

t_span = [0, 20]
t_eval = np.linspace(0, 20, 1000)

# Solve and save solutions for each scenario
for scenario in scenarios:
    G = scenario["G"]
    m1, m2, m3 = scenario["masses"]
    y0 = scenario["initial_positions"] + scenario["initial_velocities"]

    solution = solve_ivp(three_body_system, t_span, y0, t_eval=t_eval, args=(G, m1, m2, m3), rtol=1e-10, atol=1e-10)
    np.savez(f'three_body_solution_{scenario["name"]}.npz', t=solution.t, y=solution.y)

# Plot solutions
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
axes = axes.flatten()

for i, scenario in enumerate(scenarios):
    data = np.load(f'three_body_solution_{scenario["name"]}.npz')
    t = data['t']
    y = data['y']

    x1, y1 = y[0], y[1]
    x2, y2 = y[2], y[3]
    x3, y3 = y[4], y[5]

    ax = axes[i]
    ax.plot(x1, y1, label='Body 1', color='red')
    ax.plot(x2, y2, label='Body 2', color='blue')
    ax.plot(x3, y3, label='Body 3', color='green')
    ax.set_title(scenario["name"])
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.legend()
    ax.grid(True)
    ax.set_aspect('equal')

plt.tight_layout()
plt.show()