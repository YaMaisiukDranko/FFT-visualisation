import numpy as np
import matplotlib.pyplot as plt

waveType = input("Enter type of wave: cos or sin:  ")
freq = int(input("Enter wave frequency:  "))
maxTime = int(input("Enter graph time in seconds:  "))


fs = 60  # point / sec
pc = 2 * np.pi * freq
t = np.linspace(0, maxTime, fs * maxTime)

if waveType == "cos":
    wave = np.cos(pc * t)
elif waveType == "sin":
    wave = np.sin(pc * t)



plt.plot(t, wave)
plt.show()


