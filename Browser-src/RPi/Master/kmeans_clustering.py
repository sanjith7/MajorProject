import pandas as pd
from sklearn.cluster import KMeans 
from sklearn import metrics 
from scipy.spatial.distance import cdist 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


with open('result.txt') as fp:
    data = [list(map(float, line.strip().split(' '))) for line in fp]
fp.close()
X=np.array(data[0])
kmeans = KMeans(n_clusters=4)
kmeans.fit(X.reshape(-1,1))
print(kmeans.cluster_centers_)
print(kmeans.labels_)
plt.scatter(X,[1]*len(X), c=kmeans.labels_ , cmap='rainbow')
plt.title('K-means Clustering Plot')
plt.xlabel('Forecasted Demand for 1 hour for 39 houses in KW')
plt.show()
file = open('clust_res.txt', 'w') #write to file
for i in kmeans.labels_:
    # print(i)
    file.write(str(i)+' ')
file.close()