import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,
ani = FuncAnimation(fig, update, frames=range(100), interval=50)
plt.title('Animated Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.savefig('matPlotLib/animated_sine_wave.webp')
plt.show()