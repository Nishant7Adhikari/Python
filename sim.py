import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

R = 5.0
dt = 0.05

x, y = 1.0, 2.0
vx, vy = 2.0, 1.5

fig, ax = plt.subplots()
ax.set_xlim(-R-1, R+1)
ax.set_ylim(-R-1, R+1)
ax.set_aspect('equal')
ax.grid(True)

theta = np.linspace(0, 2*np.pi, 400)
ax.plot(R*np.cos(theta), R*np.sin(theta))

ball, = ax.plot([], [], 'ro')
ball.set_data([x], [y])   # FIXED

def update(frame):
    global x, y, vx, vy

    x += vx * dt
    y += vy * dt

    dist = np.sqrt(x*x + y*y)

    if dist >= R:
        nx = x / dist
        ny = y / dist

        dot = vx*nx + vy*ny
        vx -= 2 * dot * nx
        vy -= 2 * dot * ny

        x = nx * (R - 0.001)
        y = ny * (R - 0.001)

    ball.set_data([x], [y])  # FIXED
    return ball,

ani = FuncAnimation(fig, update, frames=1000, interval=20, blit=False)
plt.show()
