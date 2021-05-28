import collections
import pandas as pd
import matplotlib.pyplot as plt

# P1
quotes = pd.read_csv('afi-top-100-quotes.csv')

# P2
quotes['YEAR'].hist(bins=10, grid=False)
plt.show()

# P3
ff = pd.DataFrame(quotes['MOVIE'].value_counts())
ff.index.name = "movie"
ff.columns = ['count']
print(ff[(ff['count'] > 1)])

# P4
movie = quotes['MOVIE']
movie = movie.astype(str)

# P5
a = []
c = []
for i in range(len(movie)):
    a.append(movie[i].split())
    c.append(len(a[i]))

plt.hist(c, bins=100)
plt.show()

# P6
final = []
for i in range(len(a)):
    for j in range(len(a[i])):
        final.append(a[i][j])

y = collections.Counter(final)

z = collections.Counter(y)
z = sorted(z.items())

ff = pd.DataFrame(z, columns=['Unique words', 'Number of occurrences'])
ff.to_csv('movies.csv')

# P7
quote = quotes['QUOTE']
quote = quote.astype(str)

a = []
c = []
for i in range(len(quote)):
    a.append(quote[i].split())
    c.append(len(a[i]))

plt.hist(c, bins=100)
plt.show()

final = []
for i in range(len(a)):
    for j in range(len(a[i])):
        final.append(a[i][j])

y = collections.Counter(final)

z = collections.Counter(y)
z = sorted(z.items())

df = pd.DataFrame(z, columns=['Unique words', 'Number of occurrences'])
df.to_csv('quotes.csv')
