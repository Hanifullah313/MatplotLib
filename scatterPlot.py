"""
what is scatter plot?
A scatter plot is a type of data visualization that displays values for typically two variables for a set of data. It uses Cartesian coordinates to display values for two variables, with one variable plotted along the x-axis and the other plotted along the y-axis. Each point on the scatter plot represents an observation in the dataset.
Scatter plots are useful for identifying relationships, trends, and patterns in data, as well as for spotting outliers.
"""
import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
study_hours2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores2 = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
study_hours3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores3 = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
plt.scatter(study_hours, test_scores, color='blue', alpha=0.7)
plt.scatter(study_hours2, test_scores2, color='red', alpha=0.7)
plt.scatter(study_hours3, test_scores3, color='green', alpha=0.7)
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Scatter Plot Example')
plt.show()  