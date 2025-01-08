"""
author: Dominik Cedro
desc: This code utilizes animation from lab11 - three body problem.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

matplotlib.use('TkAgg')

def animate_two_body():
    data = np.load('two_body_solution.npz')
    t = data['t']
    y = data['y']

    x1, y1 = y[0], y[1]
    x2, y2 = y[2], y[3]

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.grid(True)

    colors = ['red', 'blue']
    particles = [ax.plot([], [], 'o', color=c, markersize=10, label=f'Particle {i+1}')[0]
                 for i, c in enumerate(colors)]
    trails = [ax.plot([], [], '-', color=c, alpha=0.5)[0] for c in colors]

    ax.legend()
    plt.title('Two-Body Problem')
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
        for i, (particle, trail, x, y) in enumerate(zip(particles, trails, [x1, x2], [y1, y2])):
            particle.set_data([x[frame]], [y[frame]])
            trail.set_data(x[:frame+1], y[:frame+1])
        return particles + trails

    anim = FuncAnimation(fig, update, frames=len(t),
                         init_func=init, blit=True,
                         interval=20, repeat=True)

    plt.show()
    return anim

if __name__ == "__main__":
    animate_two_body()