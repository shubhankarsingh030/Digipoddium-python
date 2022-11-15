import numpy as np
import matplotlib.pyplot as plt

rainfall = np.array([23,43,6,4,53,3,42,23])
year = np.array([2010,2011,2012,2013,2014,2015])

plt.bar(year, rainfall)
plt.show()