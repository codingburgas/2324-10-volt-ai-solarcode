
from sklearn.cluster import KMeans
import numpy as np


data = np.array([[1, 2], [2, 3], [8, 7], [10, 9], [11, 8]])


k = 2


kmeans = KMeans(n_clusters=k)


kmeans.fit(data)


centroids = kmeans.cluster_centers_

labels = kmeans.labels_


print("Cluster centroids:")
print(centroids)
print("Cluster labels:")
print(labels)
