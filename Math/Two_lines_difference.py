import matplotlib.pyplot as plt
import numpy as np

# Create data for the falling graph
x1 = np.arange(0, 10, 0.1)
y1 = 10 - x1

# Create data for the rising graph
x2 = np.arange(0, 10, 0.1)
y2 = x2

# Create a plot and plot both lines on it
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x1, y1, 'r', label='Falling graph')
ax.plot(x2, y2, 'g', label='Rising graph')

# Set the title, legend, and axis labels for the plot
ax.set_title('Falling and Rising Graphs')
ax.legend()
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Show the plot
plt.show()