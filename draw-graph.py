import numpy as np
import matplotlib.pyplot as plt

freq = 1 # Frequency in Hz
wy = 2 * np.pi * freq
fs = 60 # point / sec
maxTime = 3 # Seconds
t = np.linspace(0, maxTime, fs * maxTime)

wave = np.sin(wy * t)
plt.plot(t, wave)
plt.show()
