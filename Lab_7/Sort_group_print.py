import pandas as pd

# Question 1
ff = pd.read_csv('Cars93.csv')
car_manufac = ff['Manufacturer'].unique()
for i in range(len(car_manufac)):
    print(str(i + 1) + '.', car_manufac[i])

# Question 2
price_list = ff['Type'].unique()
for i in price_list:
    print(i, '-', ff[ff['Type'] == i]['Price'].max())


# Question 3
def find_model(x):
    y = ff[ff['Manufacturer'] == x]['Model']
    if y.tolist() == []:
        print("Entered Manufacturer is invalid")
    else:
        print(y)


a = input("Enter the Manufacturer: ")
find_model(a)

# Question 4
print(ff['Manufacturer'].value_counts())

# Question 5
b = (ff['Origin'] == 'non-USA') & (ff['Type'] == 'Small')
b = ff[b]['Make'].sort_values()
print(b)

# Question 6
c = ff.groupby(['Manufacturer'])
c = c['Price'].mean().sort_values()
print(c)

# Question 7
avg_price = ff['Price'].mean()
d = (ff['Type'] == 'Midsize') & (ff['Price'] < avg_price)
d = ff[d]['Model']
print(d)

# Question 8
avg_MGPcity = ff['MPG.city'].mean()
avg_MGPhighway = ff['MPG.highway'].mean()
filt = (ff['MPG.city'] > avg_MGPcity) & (ff['MPG.highway'] > avg_MGPhighway)
print(ff[filt]['Model'])
