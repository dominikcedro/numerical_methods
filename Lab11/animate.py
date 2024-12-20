"""
author: Dominik Cedro
date: 18.12.2024
description: File contains logic to animate calculations done in solutions.py.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

matplotlib.use('TkAgg')  # Use TkAgg backend

def animate_three_body():
    data = np.load('three_body_solution.npz')
    t = data['t']
    y = data['y']

    x1, y1 = y[0], y[1]
    x2, y2 = y[2], y[3]
    x3, y3 = y[4], y[5]

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.grid(True)

    colors = ['red', 'blue', 'green']
    particles = [ax.plot([], [], 'o', color=c, markersize=10, label=f'Particle {i+1}')[0]
                 for i, c in enumerate(colors)]
    trails = [ax.plot([], [], '-', color=c, alpha=0.5)[0] for c in colors]

    ax.legend()
    plt.title('Three-Body Problem')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')

    def init():
        """Initialize animation"""
        for particle, trail in zip(particles, trails):
            particle.set_data([], [])
            trail.set_data([], [])
        return particles + trails

    def update(frame):
        """Update animation"""
        trail_length = 50  # Length of the trail
        for i, (particle, trail, x, y) in enumerate(zip(particles, trails, [x1, x2, x3], [y1, y2, y3])):
            particle.set_data([x[frame]], [y[frame]])
            start = max(0, frame - trail_length)
            trail.set_data(x[start:frame], y[start:frame])
        return particles + trails

    anim = FuncAnimation(fig, update, frames=len(t),
                         init_func=init, blit=True,
                         interval=20, repeat=True)

    plt.show()
    return anim

# Run the animation
if __name__ == "__main__":
    anim = animate_three_body()