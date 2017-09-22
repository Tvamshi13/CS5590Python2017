#Importing numpy package
import numpy as np
#Generating random vector
vector = np.random.random(15)
#appending maximum value to the vector
vector[vector.argmax()] = 10
print(vector)