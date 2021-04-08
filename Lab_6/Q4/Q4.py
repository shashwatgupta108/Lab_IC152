import matplotlib.pyplot as plt

no_of_children = [8, 10, 18, 10, 12, 6]
plt.bar(range(0, 12, 2), no_of_children, color='violet', width=2, ec="k", align="edge")
plt.ylabel("Number of children")
plt.xlabel("Age of children")
xm = range(1, 12, 2)
tf = 0
td = 0
for i in range(6):
    tf = tf + no_of_children[i]
    td = td + no_of_children[i] * xm[i]
mean = td / tf
cf = no_of_children[0] + no_of_children[1] + no_of_children[2]
median = 6 + (tf / 2 - cf) / no_of_children[3] * 2
mode = 4 + ((no_of_children[2] - no_of_children[1]) / (
        2 * no_of_children[2] - no_of_children[1] - no_of_children[3])) * 2
plt.vlines(mean, 0, 20, label="mean", colors='red', linestyle='dashed')
plt.vlines(median, 0, 20, label='median', colors='blue', linestyle='dashed')
plt.vlines(mode, 0, 20, label="mode", colors='black', linestyles='dashed')
plt.legend()
plt.show()
