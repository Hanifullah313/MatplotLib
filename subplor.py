""" 
what is sub Plot?
A subplot is a smaller plot that is contained within a larger plot. Subplots are useful for displaying multiple plots in a single figure, allowing for easy comparison of different datasets or visualizations. In Matplotlib, subplots can be created using the `subplot` function, which takes the number of rows and columns of subplots, as well as the index of the current subplot.
"""

import matplotlib.pyplot as plt

# Create subplots
fig, axs = plt.subplots(2, 2)
fig.suptitle('Subplot Example')
# Plotting on each subplot
axs[0, 0].plot([1, 2, 3], [4, 5, 6] , color='blue')
axs[0, 0].set_title('Plot 1')

axs[0, 1].scatter([1, 2, 3], [4, 5, 6], color='red')
axs[0, 1].set_title('Plot 2')

axs[1, 0].bar([1, 2, 3], [4, 5, 6], color='green')
axs[1, 0].set_title('Plot 3')

axs[1, 1].hist([1, 2, 3], color='purple')
axs[1, 1].set_title('Plot 4')

# Adjust layout
plt.tight_layout()
plt.show()