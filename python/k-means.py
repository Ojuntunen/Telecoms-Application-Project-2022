import numpy as np
import matplotlib.pyplot as plt

raw_data = np.loadtxt("./python/putty.log")
DATA_LENGTH = int(len(raw_data) / 3)
data = np.reshape(raw_data, (DATA_LENGTH, 3))

CLUSTERS = 4
EXPECTED_CLUSTER_SIZE = DATA_LENGTH / CLUSTERS

center_points = np.random.rand(CLUSTERS, 3) * 1023
data_points_cumulative_sum = np.zeros((CLUSTERS,3))
points_in_clusters = np.zeros((CLUSTERS,1))
distance = np.zeros((CLUSTERS,1))
center_points_log = []
loop = 0

while (1):
    print(loop)
    loop +=1
    center_points_log.append(center_points)
    points_in_clusters[:] = 0
    data_points_cumulative_sum[:] = 0
        
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
    if (np.array_equal(center_points, center_points_log[-1]) & (points_in_clusters.max() <= EXPECTED_CLUSTER_SIZE)):
        center_points_log.append(center_points)
        break
    
print(points_in_clusters)

with open("./python/test-data-center-points.txt", "w") as file:
        file.write(f"{center_points}")