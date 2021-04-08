import pandas as pd
import matplotlib.pyplot as plt

d1 = pd.read_csv('d1.txt', sep=' ', header=None)
d2 = pd.read_csv('d2.txt', sep=' ', header=None)
d3 = pd.read_csv('d3.txt', sep=' ', header=None)
d4 = pd.read_csv('d4.txt', sep=' ', header=None)
data = [d1[0], d2[0], d3[0], d4[0]]

plt.boxplot(data)
plt.xlabel("Data file")
plt.ylabel("Values")
plt.title("Boxplot for 4 data files")
plt.show()
