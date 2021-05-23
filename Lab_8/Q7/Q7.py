import numpy as np
import matplotlib.pyplot as plt


def f_norm(m, n, r):
    x = np.random.randint(0, r + 1, (m, n))
    return np.linalg.norm(x)


a = []
for i in range(1000):
    a.append(f_norm(5, 5, 20))
plt.hist(a, rwidth=0.8)
plt.xlabel("Frobenius Norm Value")
plt.show()

r = [5000, 5500, 7000, 8000]
b = []
for x in r:
    a = []
    for i in range(1000):
        a.append(f_norm(5, 5, x))
    b.append(a)

fig, axs = plt.subplots(2, 2)
fig.set_figheight(15)
fig.set_figwidth(20)
axs[0, 0].boxplot(b[0])
axs[0, 0].set_title('R = 5000')
axs[0, 1].boxplot(b[1])
axs[0, 1].set_title('R = 5500')
axs[1, 0].boxplot(b[0])
axs[1, 0].set_title('R = 7000')
axs[1, 1].boxplot(b[0])
axs[1, 1].set_title('R = 8000')
plt.show()
