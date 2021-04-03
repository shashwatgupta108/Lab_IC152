import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')
state = np.array(data)
a = state.tolist()
dit = {"S": -1, "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10}


def mean(x):
    avg = 0
    for i in x:
        avg = avg + i[0]
    return round(avg / len(x), 5)


def median(y):
    n = len(y)
    if n % 2 == 0:
        return y[n // 2][0]
    else:
        return (y[(n - 1) // 2][0] + y[(n + 1) // 2][0]) / 2


def q1_ans(s):
    m = dit[s]
    a2 = []
    for i in a:
        a2.append((i[m + 1], i[0]))
    a2.sort(key=lambda x: x[0])
    return {"H": a2[-1][1], "L": a2[0][1], "A": str(mean(a2)), "M": str(median(a2))}


# Population Density
pd = q1_ans('F')
print("Highest: " + pd["H"], "Lowest: " + pd["L"], "Average: " + pd["A"], "Median: " + pd["M"])

# Percentage of marginal farmers
pmf = q1_ans('G')
print("Highest: " + pmf["H"], "Lowest: " + pmf["L"], "Average: " + pmf["A"], "Median: " + pmf["M"])

# Percentage of women in overall workforce
pww = q1_ans('K')
print("Highest: " + pww["H"], "Lowest: " + pww["L"], "Average: " + pww["A"], "Median: " + pww["M"])


