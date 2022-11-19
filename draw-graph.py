import numpy as np
import matplotlib.pyplot as plot

# Get x values of the sine wave
time = np.arange(0, 1, 0.01)

# Amplitude of the sine wave is sine of a variable like time
amplitude = np.cos(time*19.1)

# Plot a sine wave using time and amplitude obtained for the sine wave
plot.plot(time, amplitude)

# Give a title for the sine wave plot
plot.title('Cos wave')

# Give x axis label for the sine wave plot
plot.xlabel('Time')

# Give y axis label for the sine wave plot
plot.ylabel('Amplitude = cos(time)')

plot.grid(True, which='both')

plot.axhline(y=0, color='k')
plot.show()

# Display the sine wave
plot.show()