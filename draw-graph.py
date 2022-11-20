# Importing Required Libraries
import numpy as np
import matplotlib.pyplot as plt
# sampling rate
sr = 100.0
# sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)

freq = 2
y = freq*np.sin(2*np.pi*freq*t)
plt.xlim(freq*-1, 1)
plt.ylim(-1, 1)
plt.axis('square')
#plt.axis('square')
# plt.figure(figsize = (8, 8))
plt.plot(t, y, 'b')
plt.ylabel('Amplitude')
plt.show()
