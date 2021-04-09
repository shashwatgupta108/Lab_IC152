import pandas as pd
import matplotlib.pyplot as plt

d1 = pd.read_csv('Class1.txt', sep=' ', header=None)
d2 = pd.read_csv('Class2.txt', sep=' ', header=None)
x1, y1 = d1[0], d1[1]
x2, y2 = d2[0], d2[1]

plt.scatter(x1, y1, c='b', marker='^', label='Class1')
plt.scatter(x2, y2, c='r', label='Class2')
plt.legend()
plt.show()
k = 0.5
y1 = y1 + 0.5
y2 = y2 - 0.5
plt.scatter(x1, y1, c='b', marker='^', label='Class1')
plt.scatter(x2, y2, c='r', label='Class2')
plt.legend()
plt.show()
