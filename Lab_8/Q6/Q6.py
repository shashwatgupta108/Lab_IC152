import numpy as np
import matplotlib.pyplot as plt

men = np.random.normal(5, 1.05, 500)
women = np.random.normal(4, 0.983, 500)
children = np.random.normal(3, 0.786, 500)
plt.hist(men,  rwidth=0.25, label="MAN")
plt.hist(women, rwidth=0.25, label="Women")
plt.hist(children, rwidth=0.25, label="Children")
plt.legend()
plt.xlabel("Height in Feet")
plt.show()
