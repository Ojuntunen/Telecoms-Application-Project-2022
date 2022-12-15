import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql_get
import data_utilities

#filename = mysql_get.get_data()
filename = './python/mysql_get.csv'
data = pd.read_csv(f'{filename}', sep=';')
data = data.head(95)
data = np.array(data)

DATA_LENGTH = len(data)

CLUSTERS = 4
EXPECTED_CLUSTER_SIZE = 15

center_points = np.random.rand(CLUSTERS, 3) * 1023
data_points_cumulative_sum = np.zeros((CLUSTERS,3))
points_in_clusters = np.zeros((CLUSTERS,1))
distance = np.zeros((CLUSTERS,1))
center_points_log = []

for i in range(1000):
    print(i)
    center_points_log.append(center_points)
    points_in_clusters[:] = 0
    data_points_cumulative_sum[:] = 0
    previous_result = points_in_clusters
        
    for i in range(DATA_LENGTH):
        for k in range(CLUSTERS):
            distance[k] = np.linalg.norm(data[i] - center_points[k])
        closest = np.argmin(distance)
        points_in_clusters[closest] += 1
        data_points_cumulative_sum[closest] += data[i]
        
    for k in range(CLUSTERS):
        if points_in_clusters[k] == 0:
            center_points[k] = np.random.rand(1,3) * 1023
        else:
            center_points[k] = data_points_cumulative_sum[k] / points_in_clusters[k]

    if (np.array_equal(center_points, center_points_log[-1]) & (points_in_clusters >= EXPECTED_CLUSTER_SIZE).all() & (np.array_equal(points_in_clusters, previous_result))):
        center_points_log.append(center_points)
        break
     
print(points_in_clusters)
print(center_points)
#data_utilities.write_h_file(center_points)
data_utilities.plot_center_points(center_points_log)
#data_utilities.plot_results(data, center_points)
