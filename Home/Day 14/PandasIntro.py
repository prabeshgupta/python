#Pandas, Python Data Analysis is a Python library. Pandas is used to analyze data. It has functions for analyzing, cleaning, exploring, and manipulating data.

import pandas as pd

print(pd.__version__)

solar = {
"planets": ["Earth", "Mars", "Jupiter"],
"positions": [3,4,5]
}

show = pd.DataFrame(solar)
print(show)