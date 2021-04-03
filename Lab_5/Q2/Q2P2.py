import Q2P1 as q


x = q.np.arange(10)
y1 = [q.f(i) for i in x]
y2 = [q.g(i) for i in x]
y3 = [q.h(i) for i in x]
y4 = [q.k(i) for i in x]
fig, a = q.plt.subplots(2, 2)
a[0][0].scatter(x, y1, label='f(x)')
a[0][0].set_title('f(x)')
a[0][1].scatter(x, y2, label='g(x)')
a[0][1].set_title('g(x)')
a[1][0].scatter(x, y3, label='h(x)')
a[1][0].set_title('h(x)')
a[1][1].scatter(x, y4, label='k(x)')
a[1][1].set_title('k(x)')
q.plt.show()
