from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering

class ClusteringModule:
    def run_clustering(self, algorithm, data):
        if algorithm.lower() == 'kmeans':
            model = KMeans()
        elif algorithm.lower() == 'dbscan':
            model = DBSCAN()
        elif algorithm.lower() == 'agglomerative':
            model = AgglomerativeClustering()
        else:
            raise ValueError("Unsupported clustering algorithm. Supported values are: 'kmeans', 'dbscan', 'agglomerative'.")

        # Fit the model to the data and return the cluster labels
        return model.fit_predict(data)
