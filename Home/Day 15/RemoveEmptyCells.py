#dropna() method returns a new DataFrame, and will not change the original.

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

#he dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())

#The fillna() method allows us to replace empty cells with a value:

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())