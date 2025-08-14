import matplotlib.pyplot as plt
#example of histogram 
#please mixed the data of score with good distribution 
score = [1,2,3,44,23,24,43,54,64,63,63,8,62,41,34,63,42,62,8,7,45,45,82,90,88]
plt.hist(score, bins=10, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()
