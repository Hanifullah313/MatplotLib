import matplotlib.pyplot as plt
# revenue per region using pie chart
"""
what is autopct='%1.1f%%', startangle=140
- autopct: This parameter is used to format the labels on the pie chart. '%1.1f%%' means that the percentage will be displayed with one decimal place.
- startangle: This parameter rotates the start of the pie chart by the specified angle (140 degrees in this case).
 what is plt.axis('equal')?
  - This function ensures that the pie chart is drawn as a circle. If this is not set, the pie chart may be drawn as an ellipse.
"""
region = ['North', 'South', 'East', 'West']
revenue = [25000, 30000, 20000, 15000]
plt.pie(revenue, labels=region, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Revenue Distribution by Region')
plt.show()