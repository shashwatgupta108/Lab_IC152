import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data.csv')
state = np.array(data)
a = state.tolist()
dit = {"S": -1, "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10}


# PLotting
def p2_ans(c):
    m = dit[c]
    a2 = []
    for i in a:
        a2.append((i[m + 1]))
    return a2


p, d = p2_ans('D'), p2_ans('E')
S = p2_ans('S')
Width = 0.3
fig = plt.subplots(figsize=(20, 12))
g1 = np.arange(len(S))
g2 = [S + Width for S in g1]

plt.bar(g1, p, color='red', width=Width, edgecolor='black', label='Percentage area with slope > 30%')
plt.bar(g2, d, color='blue', width=Width, edgecolor='blue', label='Road Density')
plt.xlabel('State')
plt.ylabel('Percentage area with slope > 30% and Road Density')
plt.xticks([r + Width for r in range(len(S))], S, rotation=45)

plt.legend()
plt.show()
