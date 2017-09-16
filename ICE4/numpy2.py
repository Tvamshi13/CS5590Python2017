#importing numpy package

import numpy as np

#creating random array with 10*10 size
array = np.random.random((10,10))
minValue, maxValue = array.min(), array.max()
print("The minimum and maximum values of the array are ")
print(minValue , maxValue)