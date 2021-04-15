from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def correl(x, y):
    n = len(x)
    sx = sy = sxy = sx2 = sy2 = 0
    for i in range(n):
        sx = sx + x[i]
        sy = sy + y[i]
        sxy = sxy + x[i] * y[i]
        sx2 = sx2 + x[i] ** 2
        sy2 = sy2 + y[i] ** 2
    r = ((n * sxy) - (sx * sy)) / (sqrt((n * sx2) - sx ** 2) * sqrt((n * sy2) - sy ** 2))
    return r


# A:
x1 = [3, -1, 6, 12, 8, 10, 9, 13, 15, -3, 0, -5, -2, 16]
y1 = [4, -2, 5, 11, 6, 11, 7, 8, 9, -4, 1, -6, -1, 14]
# B:
x2 = [3, -1, 6, 12, 8, 10, 9, -5, -2, 4, 2, 0, 14, 11]
y2 = [0, 2, -3, 4, 0, 1, 2, -1, -2, 2, 1, -2, 9, 2]
# C:
x3 = [3, 4, 2, 5, 8, -8, -6, -1, 0, -5, 4, 2, 6, 8]
y3 = [5, -1, 0, 1, 2, 2, 4, 2, 1, 2, 1, 2, -4, 4]

r1 = correl(x1, y1)
r2 = correl(x2, y2)
r3 = correl(x3, y3)

print(f"Correlation of A: {r1}")
if r1 > 0:
    print("y1 increases with increase in x1")
else:
    print("y1 does not always increase with increase in x1")

print(f"Correlation of B: {r2}")
if r2 > 0:
    print("y2 increases with increase in x2")
else:
    print("y2 does not always increase with increase in x2")

print(f"Correlation of C: {r3}")
if r3 > 0:
    print("y3 increases with increase in x3")
else:
    print("y3 does not always increase with increase in x3")
 
fig = plt.figure()
plt1 = fig.add_subplot(131)
plt2 = fig.add_subplot(132)
plt3 = fig.add_subplot(133)
plt1.title.set_text('A')
plt2.title.set_text('B')
plt3.title.set_text('C')
plt1.scatter(x1, y1)
plt2.scatter(x2, y2)
plt3.scatter(x3, y3)
plt.show()
