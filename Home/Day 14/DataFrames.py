#A Pandas DataFrame is a a 2 dimensional array, or a table with rows and columns.

#Series is like a column, a DataFrame is the whole table.

import pandas as pd

solar = {
"planets": ["Earth", "Mars", "Jupiter"],
"positions": [3,4,5]
}

show = pd.DataFrame(solar)

#Pandas use the loc attribute to return one or more specified row(s)
print(show.loc[[0, 1]])