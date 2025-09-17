import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 4, 6, 8]

plt.scatter(x, y, color='red', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.savefig('matPlotLib/scatter_plot.png')
plt.show()
