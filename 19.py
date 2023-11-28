import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'TotalAmountSpent': [100, 300, 150, 500, 200, 600, 350, 800, 400, 700],
    'NumberOfItems': [5, 10, 6, 15, 8, 18, 12, 20, 10, 16]
}
df = pd.DataFrame(data)
X = df[['TotalAmountSpent', 'NumberOfItems']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
num_clusters = 3
kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans_model.fit_predict(X_scaled)
plt.scatter(df['TotalAmountSpent'], df['NumberOfItems'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.title('Customer Segmentation with K-Means Clustering')
plt.show()
