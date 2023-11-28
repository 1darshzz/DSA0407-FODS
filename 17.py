import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
np.random.seed(0)
num_customers = 200
total_amount_spent = np.random.randint(50, 1000, size=num_customers)
visit_frequency = np.random.randint(1, 30, size=num_customers)
data = pd.DataFrame({
'TotalAmountSpent': total_amount_spent,
'VisitFrequency': visit_frequency
})
kmeans = KMeans(n_clusters=3, n_init=10)
kmeans.fit(data)
cluster_labels = kmeans.labels_
# Add cluster labels to the DataFrame
data['Cluster'] = cluster_labels
plt.figure(figsize=(8, 6))
for cluster_id in range(3):
     plt.scatter(
data[data['Cluster'] == cluster_id]['TotalAmountSpent'],
data[data['Cluster'] == cluster_id]['VisitFrequency'],
label=f'Cluster {cluster_id}'
)
plt.xlabel('Total Amount Spent')
plt.ylabel('Visit Frequency')
plt.title('Customer Segmentation using K-Means Clustering')
plt.legend()
plt.show()
