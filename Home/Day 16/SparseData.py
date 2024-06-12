#Sparse data is data that has mostly unused elements (elements that don't carry any information ).

"""


Sparse Data: is a data set where most of the item values are zero.

Dense Array: is the opposite of a sparse array: most of the values are not zero.


CSC - Compressed Sparse Column.
CSR - Compressed Sparse Row
"""

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))