import pandas as pd
import matplotlib.pyplot as plt

d1 = pd.read_csv('Class1.txt', sep='\t', header=None)
d2 = pd.read_csv('Class2.txt', sep='\t', header=None)
d1.drop(columns=2, inplace=True)
d2.drop(columns=2, inplace=True)
x1, y1 = d1[0], d1[1]
x2, y2 = d2[0], d2[1]
plt.scatter(x1, y1, c='b', marker='^', label='Class 1')
plt.scatter(x2, y2, c='r', marker='x', label='Class 2')
plt.legend()
plt.show()
y1 = [0] * len(y1)
y2 = [0] * len(y2)
plt.scatter(x1, y1, c='r', marker='^', label='Class 1')
plt.scatter(x2, y2, c='b', marker='x', label='Class 2')
plt.show()
