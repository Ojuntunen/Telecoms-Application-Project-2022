import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import metrics

#plots example data into 3d scatter plot
def plot_test_data(path = './python/putty.log'):
    data = np.loadtxt(f'{path}')

    x = data[0::3]
    y = data[1::3]
    z = data[2::3]

    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.scatter(x,y,z, color='red')
    ax.set_xlabel('X-axis', fontweight ='bold')
    ax.set_ylabel('Y-axis', fontweight ='bold')
    ax.set_zlabel('Z-axis', fontweight ='bold')
    ax.set_title('Example data', fontweight='bold', fontsize=16)

    plt.show()

#plots a (n,3) list of points into 3d scatter plot
def plot_center_points(list_of_points):
    data = np.array(list_of_points)
    print(data.shape)
    # x = list_of_points[:][0]
    # y = list_of_points[:][1]
    # z = list_of_points[:][2]
    # fig = plt.figure()
    # ax = plt.axes(projection = '3d')
    # ax.scatter(x,y,z)

    # plt.show()

#plots all the data in found in the database into 3d scatter plot
def plot_all_data(filepath='./python/mysql_get.csv'):
    data = pd.read_csv(f'{filepath}', sep=';')
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.scatter(data.x, data.y, data.z, color='red')
    ax.set_xlabel('X-axis', fontweight ='bold')
    ax.set_ylabel('Y-axis', fontweight ='bold')
    ax.set_zlabel('Z-axis', fontweight ='bold')
    ax.set_title('All data', fontweight='bold', fontsize=16)
    plt.show()

#writes the results of the K-means algorithm into a C++ h-file for use with the arduino
def write_h_file(array):
    with open('./arduino_main/centerpoints.h', 'w') as file:
        file.write('#ifndef CENTERPOINTS_H\n')
        file.write('#define CENTERPOINTS_H\n\n')
        for i in range(len(array)):
            file.write(f'double center_point_{i+1}[] = {{{array[i,0]},{array[i,1]},{array[i,2]}}};\n')
        file.write('\n#endif')
        file.close()

def plot_results(data, center_points):
    x = data[:,0]
    y = data[:,1]
    z = data[:,2]
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.scatter3D(x,y,z, color='red', marker='^', label='data')
    x2 = center_points[:,0]
    y2 = center_points[:,1]
    z2 = center_points[:,2]
    ax.scatter3D(x2,y2,z2,color='blue', marker='o', s=200, label='center points')
    ax.set_xlabel('X-axis', fontweight ='bold')
    ax.set_ylabel('Y-axis', fontweight ='bold')
    ax.set_zlabel('Z-axis', fontweight ='bold')
    ax.set_title('Data and center points', fontweight='bold', fontsize=20)
    ax.legend()

    plt.show()
    
def plot_cm():
    df = pd.read_csv("./etc/alignment_data.csv")
    true = df['true']
    predicted = df['predicted']

    cm_display = metrics.ConfusionMatrixDisplay.from_predictions(y_true=true, y_pred=predicted, cmap='hot')
    cm_display.plot()
    plt.show() 
    
if __name__ == '__main__':
    test_array = np.array([[100,100,100],[200,200,200],[300,300,300],[400,400,400]])
    #write_h_file(test_array)
    #plot_all_data()
    plot_cm()