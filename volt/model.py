class ClusteringModule:
    def __init__(self):
        pass

    def run_clustering(self, algorithm, data):
        """
        Run a clustering algorithm on the given data.

        Parameters:
        algorithm (str): Name of the clustering algorithm. Supported values: 'kmeans', 'dbscan', 'agglomerative'.
        data (array-like): Input data for clustering.

        Returns:
        array: Cluster labels assigned to each data point.
        """
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