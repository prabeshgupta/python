"""
To discover duplicates, we can use the duplicated() method.

The duplicated() method returns a Boolean values for each row
"""

import pandas as pd

df = pd.read_csv('data.csv')

df.drop_duplicates(inplace = True)

print(df.to_string())
