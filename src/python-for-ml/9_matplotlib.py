import matplotlib.pyplot as plt
import numpy as np

# Create some data.
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot.
plt.figure(figsize=(6, 4))
plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Scatter plot.
plt.figure(figsize=(6, 4))
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Histogram.
plt.figure(figsize=(6, 4))
plt.hist(y, bins=20)
plt.title('Histogram')
plt.xlabel('y')
plt.ylabel('Frequency')
plt.show()

# Bar plot.
categories = ['A', 'B', 'C', 'D', 'E']
values = [7, 12, 15, 10, 8]
plt.figure(figsize=(6, 4))
plt.bar(categories, values)
plt.title('Bar Plot')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# Pie chart.
plt.figure(figsize=(6, 4))
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()