import numpy as np
import pylab
from sklearn import linear_model
import matplotlib .pyplot as plt

#importing inputs through numpy arrays
x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])
#taking the average of input
X=np.mean(x)
print(X)
#taking the average of Output
Y=np.mean(y)
print(Y)
#linear regression(X, Y)

numerator= np.sum((x-X)*(y-Y))
denominator=np.sum((x-X)*(x-X))

slope=numerator/denominator
print(slope)

constant=Y- slope*X
print("constant", constant )
Yline= slope*x + constant
print(Yline)

linear_mod = linear_model.LinearRegression()
x = np.reshape(x,(len(x),1))
y = np.reshape(y,(len(y),1))
linear_mod.fit(x,y)
predicted_output = linear_mod.predict(1)
print(predicted_output)
plt.plot(x,Yline)
plt.scatter(x,y)
plt.show()