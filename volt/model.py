from data_prep import CSVReader
from sklearn.cluster import KMeans


def cluster_data(data, algorithm, parameters):
  try: 
    if (algorithm.lower() == "kmeans"): 
        k_means = KMeans(**parameters)
        cluster_labels = k_means.fit_predict(data)
        return cluster_labels 
    else: 
        cluster_labels = []
        print(f"Sorry the '{algorithm.lower()}' algorithm isn't supported.") 
  except: 
    print(f"Sorry but there appears to be an error running '{algorithm.lower()}' on your data: {data}") 

    cluster_labels = []

  print("-"*80)

  cluster_count = len(set(cluster_labels))

  print(f"The clustering identified {cluster_count} distinct groups in the data.") 
  return cluster_labels

