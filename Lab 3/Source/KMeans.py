import csv
import numpy as np
import matplotlib.pyplot as pl
from sklearn.cluster import KMeans

#Extracting the data from Customers.csv file

def getData(fileName):
    x=[]
    y=[]
    csvdata = open (fileName, 'r')
    fileData = csv.reader(csvdata)
    next(fileData)
    for columns in fileData:
        x.append(int(columns[2]))
        y.append(int(columns[3]))
    data = list(zip(x,y))
    return data

fileName = "Customers.csv"
data = getData(fileName)
#Appending the Kmeans algorithm for the data with 5 clusters
kmeans = KMeans(n_clusters = 5)
#Fitting the data into the model
kmeans.fit(data)
#Determining the centroids and respective labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
#Appending colors and labels
colors = ["r","g","b","y","c"]
clusterLabel = ["Cluster-1","Cluster-2","Cluster-3","Cluster-4","Cluster-5"]

#Performing Clustering

for i in range(len(data)):
    pl.scatter(data[i][0],data[i][1],c=colors[labels[i]], label=clusterLabel[labels[i]])

#Plotting the graph with description
pl.scatter(centroids[:, 0], centroids[:, 1], label="Centroids", marker=".", s=100, linewidths=20, zorder=25)
pl.title('Customer Clusters')
pl.xlabel('Customer Age')
pl.ylabel('Annual Income(k$)')
pl.show()

