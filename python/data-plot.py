# plots example dataset into 3d scatter graph

import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("./python/putty.log")

x = data[0::3]
y = data[1::3]
z = data[2::3]

fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.scatter(x,y,z, color="red")

plt.show()
