import matplotlib.pyplot as plt
import numpy as np

Bank_A = [43.1, 45.3, 47.3, 30.3, 54.1, 35.6, 43.5, 31.2, 31.4, 45.6, 37.6, 40.3, 42.2, 35.6, 36.5, 36.5, 50.2, 45.5,
          45.2, 43.1]
Bank_B = [33.1, 35.3, 37.3, 32.3, 44.1, 31.6, 33.5, 35.2, 30.4, 35.6, 32.6, 42.3, 40.2, 36.6, 38.5, 36.5, 30.2, 42.5,
          50.2, 40.1]
fig = plt.figure()
plt.subplot(121)
plt.hist(Bank_A, bins=range(30, 60, 5), color='r', label="Bank A")
plt.title("Bank A", fontsize=25)
plt.xlabel('Time(in seconds')
plt.ylabel('Number of customers')
plt.subplot(122)
plt.hist(Bank_B, bins=range(30, 60, 5), color='b', label="Bank B")
plt.title("Bank B", fontsize=25)
plt.xlabel('Time(in seconds')
plt.ylabel('Number of customers')
plt.show()

m1 = np.mean(Bank_A)
m2 = np.mean(Bank_B)
if m1 > m2:
    print(
        "Bank B serves its customers faster compered to Bank A as its avg. time per customer is less compared to bank "
        "A and its plot also show that most of its customers are served faster")
else:
    print(
        "Bank A serves its customers faster compered to Bank B as its avg. time per customer is less compared to Bank "
        "B and its plot also show that most of its customers are served faster")
