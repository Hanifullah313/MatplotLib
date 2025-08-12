import matplotlib.pyplot as plt 
"""
Types of charts and its uses:

1. Line Chart: Used to display trends over time.
2. Bar Chart: Used to compare quantities of different categories.
3. Pie Chart: Used to show proportions of a whole.
4. Scatter Plot: Used to show relationships between two variables.
5. Histogram: Used to show the distribution of a dataset.

"""

# example of bar charts
# example of product and sales
categories = ['Product A', 'Product B', 'Product C', 'Product D']
values = [4, 7, 1, 8]
plt.bar(categories, values , color ="blue", alpha=0.7, edgecolor='black')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Bar Chart Example')
plt.show()
