import Q2P1 as q

x = q.np.arange(10)
y1 = [q.f(i) for i in x]
y2 = [q.g(i) for i in x]
y3 = [q.h(i) for i in x]
y4 = [q.k(i) for i in x]
plot2 = q.plt.figure(1)
q.plt.scatter(x, y1, label="f(x)")
q.plt.scatter(x, y2, label="g(x)")
q.plt.scatter(x, y3, label="h(x)")
q.plt.scatter(x, y4, label="k(x)")
q.plt.legend()
q.plt.title("Scatter Plot")
q.plt.xlabel('x')
q.plt.ylabel('function')
q.plt.show()
q.plt.plot(x, y1, label="f(X)")
q.plt.plot(x, y2, label="g(X)")
q.plt.plot(x, y3, label="h(X)")
q.plt.plot(x, y4, label="k(X)")
q.plt.legend()
q.plt.xlabel('x')
q.plt.ylabel('function')
q.plt.show()
x = q.np.arange(20)
y1 = [q.f(i) for i in x]
y2 = [q.g(i) for i in x]
y3 = [q.h(i) for i in x]
y4 = [q.k(i) for i in x]
q.plt.plot(x, y1, label="f(X)")
q.plt.plot(x, y2, label="g(X)")
q.plt.plot(x, y3, label="h(X)")
q.plt.plot(x, y4, label="k(X)")
q.plt.xlabel('x')
q.plt.ylabel('function')
q.plt.legend()
q.plt.show()
