#### Step 1: Import necessary libraries

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# For demonstration, assume we have a DataFrame `weather_data` with necessary columns
# weather_data = pd.read_csv('path_to_meteo_data.csv')

# Example DataFrame structure
weather_data = pd.DataFrame({
    'location': ['Location1', 'Location2', 'Location3', 'Location4'],
    'avg_daily_solar_radiation': [5.5, 6.2, 4.8, 6.5],  # kWh/m²/day
    'cloud_cover': [30, 45, 60, 20],  # percentage
    'sunshine_duration': [2500, 2300, 1800, 2600],  # hours/year
    'temperature': [25, 28, 22, 26],  # degrees Celsius
    'precipitation': [500, 600, 800, 400]  # mm/year
})


#### Step 2: Data Preprocessing
# Normalize the data
scaler = StandardScaler()
weather_features = weather_data[
    ['avg_daily_solar_radiation', 'cloud_cover', 'sunshine_duration', 'temperature', 'precipitation']]
weather_features_scaled = scaler.fit_transform(weather_features)

#### Step 3: Apply Clustering
# Apply KMeans clustering
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(weather_features_scaled)

# Add the cluster labels to the original DataFrame
weather_data['cluster'] = clusters

#### Step 4: Evaluate and Visualize Clusters
# Visualize the clustering results
plt.figure(figsize=(10, 6))
sns.scatterplot(data=weather_data, x='avg_daily_solar_radiation', y='sunshine_duration', hue='cluster',
                palette='viridis')
plt.title('Clustering of Locations for Photovoltaic Suitability')
plt.xlabel('Average Daily Solar Radiation (kWh/m²/day)')
plt.ylabel('Sunshine Duration (hours/year)')
plt.show()

# Label clusters as good or bad spots
cluster_centers = kmeans.cluster_centers_
good_cluster = np.argmax(cluster_centers[:, 0])  # Assuming higher solar radiation is better
weather_data['pv_suitability'] = weather_data['cluster'].apply(lambda x: 'Good' if x == good_cluster else 'Bad')
print(weather_data[['location', 'pv_suitability']])
