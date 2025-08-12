# save a figure
import matplotlib.pyplot as plt 
x = [1, 2, 3]
y = [4, 5, 6]
plt.plot(x, y)
plt.savefig('line_plot.png' , dpi=300 , bbox_inches='tight')
plt.show()