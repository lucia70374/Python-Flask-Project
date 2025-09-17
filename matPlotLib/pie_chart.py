import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 30, 15, 15]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Programming Language Popularity')
plt.grid()
plt.savefig('matPlotLib/pie_chart.png')
plt.show()