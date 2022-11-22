# Importing Required Libraries
import numpy as np
import matplotlib.pyplot as plt
# sampling rate
freq = 3
sr = 100.0
# sampling interval
ts = 1/sr
t = np.arange(0, 4.5, ts)


y = np.cos(2*np.pi*freq*t)
plt.xlim(0, 4.5)
plt.ylim(0, 1)
#plt.axis('square')
#plt.axis('square')
plt.figure(figsize = (8, 2))
plt.plot(t, y, 'b')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
