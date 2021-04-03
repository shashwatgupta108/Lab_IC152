import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data.csv')
state = np.array(data)
a = state.tolist()
dit = {"S": -1, "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10}


def p3_ans(c):
    m = dit[c]
    a2 = []
    for i in a:
        a2.append((i[m + 1], i[0]))
    a2.sort(key=lambda x: x[0])
    return a2


p = p3_ans('D')
n = p3_ans('E')

sn = []
rd = []
for i in p:
    for j in n:
        if i[1] == j[1]:
            rd.append(j[0])
            sn.append(j[1])
Width = 0.25
plt.bar(sn, rd, color='r', width=Width, edgecolor='k', label='Road Density')
plt.xlabel('State', fontweight='bold', fontsize='12')
plt.ylabel('Road Density', fontweight='bold', fontsize='12')
plt.xticks([r + Width for r in range(len(sn))], sn, rotation=45)
plt.title('States ordered by increasing percentage area with slope > 30% showing the road density')
plt.legend()
plt.show()
