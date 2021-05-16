import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

# # Question 9.a.
ff = pd.read_csv('Cars93.csv')
ff['Max_min_ratio'] = ff['Max.Price'] / ff['Min.Price']
print(ff[ff['Max_min_ratio'] == 1][['Manufacturer', 'Model', 'Type']])

# Question 9.b.
g = ff.groupby(['Manufacturer'])
u = g['Max_min_ratio'].max() - g['Max_min_ratio'].min()
u = u.sort_values(ascending=False)
u1 = u.max()
print('Highest gap between max_min_ratio:', u.idxmax(), u1)

# Question 9.c.
filt = (ff['Max_min_ratio'] < ff['Max_min_ratio'].mean() * 1.01) & (
        ff['Max_min_ratio'] > ff['Max_min_ratio'].mean() * 0.99)
print(ff[filt][['Manufacturer', 'Model']])

# Question 10.a.
ff['AverageMPG'] = (ff['MPG.city'] + ff['MPG.highway']) / 2
u = ff.sort_values(['AverageMPG'], ascending=False)
print(u[:5])

# Question 10.b
print(ff[ff['Type'] == 'Midsize'].sort_values(['AverageMPG'])[["Manufacturer", "Model", "Type", "Price", "AverageMPG"]])

# Question 10.c
filt = (ff['AverageMPG'] > ff['AverageMPG'].mean()) & (ff['Origin'] == 'non-USA')
print(ff[filt])

# # Question 11.a.
ff['Horsepower'] = ff['Horsepower'].astype(str)
ff['Identifier'] = ff['Manufacturer'].str[:3] + '-' + ff['Model'].str[:3] + '-' + ff['Horsepower']

# Qyestion 11.b
ff.to_csv('Cars93b20318.csv')
new_data = pd.read_csv('Cars93b20318.csv')
old_data = pd.read_csv('Cars93.csv')

u1 = new_data.columns
u2 = old_data.columns

for i in u1:
    if i not in u2:
        print(i)

# # Question 12
u = ff.groupby(['Origin', 'Type'])
print(u['Price'].mean())
print(ff['Price'][:5])
# # Statistical Analysiss
#
# # Question 13
print('CORRELATION')
print("AREA VS PASSENGERS", ":", (ff['Length'] * ff['Width']).corr(ff['Passengers']))
print("AREA VS Luggage.room", ":", (ff['Length'] * ff['Width']).corr(ff['Luggage.room']))
print("AREA VS Rear.seat.room", ":", (ff['Length'] * ff['Width']).corr(ff['Rear.seat.room']))
print("AREA VS Weight", ":", (ff['Length'] * ff['Width']).corr(ff['Weight']))

# # Question 14
ff['Horsepower'] = ff["Horsepower"].astype(float)
ff.drop(index=ff[ff['Cylinders'] == "rotary"].index, inplace=True)
ff['Cylinders'] = ff["Cylinders"].astype(float)
print("CORRELATION")
print("EngineSize VS Horsepower", ":", ff['EngineSize'].corr(ff['Horsepower']))
print("EngineSize VS Cylinders", ":", ff['EngineSize'].corr(ff['Cylinders']))
print("EngineSize VS Fuel.tank.capacity", ":", ff['EngineSize'].corr(ff['Fuel.tank.capacity']))

# # Question 15
fig, ax = plt.subplots()
(0.735 * ff['Price']).hist(bins=range(0, 50, 5), color='pink', grid=False)
ax.set_xlabel("Price in Lakhs(INR)")
ax.set_ylabel("No of Car Models")
plt.show()

(ff['AverageMPG'] * 0.425143708).hist(bins=np.linspace(0, 30, 13), color='yellow', grid=False)
ax.set_xlabel("Avg Km/liter")
ax.set_ylabel("No of Car Models")
plt.show()

(ff['Horsepower'] * 0.745699872).hist(bins=range(0, 220, 20), color='red', grid=False)
ax.set_xlabel("Horsepower in killowats")
ax.set_ylabel("No of Car Models")
plt.show()

(ff['Length'] * ff['Width'] * 0.00064516).hist(bins=range(0, 15, 1), color='blue', grid=False)
ax.set_xlabel("Area in sq meter")
ax.set_ylabel("No of Car Models")
plt.show()

(ff['Weight'] / 0.453592).hist(bins=range(0, 9500, 250), color='green', grid=False)
ax.set_xlabel("Weight in Kgs")
ax.set_ylabel("No of Car Models")
plt.show()
