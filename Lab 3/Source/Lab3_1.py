import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from sklearn.linear_model import LinearRegression
import csv

# Function to get data from the input file
def get_data(file_name):
#Reading from CSV file using Pandas library
    data = pd.read_csv(file_name)
    x_parameter =[]
    y_parameter =[]
#Appending age and annual income data into x and y parameters
    for age, annualincome in zip(data['Age'],data['Annual Income']):
        x_parameter.append([float(age)])
        y_parameter.append([float(annualincome)])
    return age,annualincome


file_name ='Customers.csv'
data = pd.read_csv(file_name)
x_parameter = []
y_parameter = []
#Iterating through the files to get columns data
for age, annualincome in zip(data['Age'], data['Annual Income']):
    x_parameter.append([float(age)])
    y_parameter.append([float(annualincome)])

#Using numpy arrays to extract data for x and y
x = np.array(x_parameter).reshape(-1, 1)
y = np.array(y_parameter).reshape(-1, 1)

#Using sklearn Linear Regression model
linearModel = LinearRegression()

#Fiiting the data into the model
linearModel.fit(x, y)
pl.scatter(x, y, color='y')

#Predicting the Annual incomes for a given age values
pl.plot(x, linearModel.predict(x), color='r')
#Labelling x and y axis
pl.xlabel("Ages")
pl.ylabel("Annual Income")
#Displaying the graph
pl.show()