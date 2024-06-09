#Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.

#Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

import matplotlib.pyplot as mpp
import seaborn as sb

sb.distplot([1,4,7,8,10])

mpp.show()