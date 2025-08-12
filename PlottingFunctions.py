import matplotlib.pyplot as plt
"""common functions of plot methods:
  color :  sets the color of the plot elements (eg : 'red')
  linestyle :  sets the style of the plot lines (eg : '--')
  linewidth :  sets the width of the plot lines (eg : 2)
  marker :  sets the marker style for the plot points (eg : 'o')
  alpha :  sets the transparency level of the plot elements (eg : 0.5)
  grid :  adds a grid to the plot (eg : True)
  title :  sets the title of the plot (eg : 'My Plot')
  xlabel :  sets the label for the x-axis (eg : 'X-axis')
  ylabel :  sets the label for the y-axis (eg : 'Y-axis')
  xlim :  sets the limits for the x-axis (eg : (0, 10))
  ylim :  sets the limits for the y-axis (eg : (0, 100))
  xticks :  sets the ticks for the x-axis (eg : [0, 1, 2, 3, 4, 5])
  yticks :  sets the ticks for the y-axis (eg : [0, 20, 40, 60, 80, 100])
  legend :  adds a legend to the plot (eg : True)
  annotate :  adds annotations to the plot (eg : (2, 30))
  errorbar :  adds error bars to the plot (eg : [1, 2, 1, 2, 1, 2])
  fill_between :  fills the area between two curves
  bar :  creates a bar plot
  hist :  creates a histogram
"""

# Sales of bakery in this week
days=['sun','mon','tue','wed','thurs','fri']
sales=[12,23,43,10,25,15]
plt.plot(days,sales , color='blue', linestyle = '--', linewidth= 3, marker='o', alpha=0.4)
plt.fill_between(days, sales, color='blue', alpha=0.1)
plt.title('Bakery Sales This Week')
plt.xlabel('Days')
plt.ylabel('Sales') 
plt.grid(True)
plt.legend(['Sales'])
plt.xticks(rotation=45 , color='black')
plt.show()
# This code creates a line plot of bakery sales over the week with various customizations.