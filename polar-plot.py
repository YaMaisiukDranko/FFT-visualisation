import matplotlib.pyplot as plt
import numpy as np

freq = int(input("Frequency:  "))
cs = float(input("Cycles/Second:  "))
t = float(input("Time:  "))
x = np.linspace(0, 2 * np.pi, 400)
y = np.cos((freq * x) / t)

fig, ax1 = plt.subplots(1, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)

plt.show()
