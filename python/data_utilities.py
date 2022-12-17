# Makes a get request over http for a CSV file, which contains the data in the database.
def get_http():
    import requests
    data = requests.get("http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=70")

    string = data.text
    print(string)
    filename = "./python/accelerometer_data.csv"
    with open(f"{filename}", "w") as file:
        file.write(string)
    return filename

# Gets data from server with a TCP socket
def get_socket():
    import socket
    HOST = "172.20.241.9"
    PORT = 20000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"70\n")
        connected = True
        data = []
        while 1:
            msg = s.recv(1024)
            if msg:
                data.append(msg)
            else:
                break
            
        print(f"received {data}")
        
    with open("./python/tcp_socket_data.csv", "w") as file:
        for i in range(len(data)):
            file.write(data[i].decode("utf-8"))

# Gets data directly from the database
def get_mysql():
    import authentication
    import mysql.connector
    
    db = mysql.connector.connect(user=authentication.USER,
                             password=authentication.PASSWORD,
                             host='172.20.241.9',
                             database='measurements')

    cursor = db.cursor()
    query = 'SELECT sensorvalue_a, sensorvalue_b, sensorvalue_c FROM rawdata WHERE groupid = 70 ORDER BY id DESC'
    cursor.execute(query)

    filename = './python/mysql_get.csv'
    
    with open(f"{filename}", 'w') as file:
        file.write("x;y;z\n")
        for (sensorvalue_a, sensorvalue_b, sensorvalue_c) in cursor:
            file.write(f"{sensorvalue_a};{sensorvalue_b};{sensorvalue_c}\n")

    cursor.close()
    db.close()
    return(filename)

# Makes a 3D scatter plot of an example data set
def plot_test_data(path = './python/putty.log'):
    import numpy as np
    import matplotlib.pyplot as plt
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

# Plots all of the data fetched from the database by get_mysql() into 3D scatter plot
def plot_all_data(filepath='./python/mysql_get.csv'):
    import pandas as pd
    import matplotlib.pyplot as plt
    data = pd.read_csv(f'{filepath}', sep=';')
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.scatter(data.x, data.y, data.z, color='red')
    ax.set_xlabel('X-axis', fontweight ='bold')
    ax.set_ylabel('Y-axis', fontweight ='bold')
    ax.set_zlabel('Z-axis', fontweight ='bold')
    ax.set_title('All data', fontweight='bold', fontsize=16)
    plt.show()

# Writes the center points identified by k_means.py into an h-file for use on the Arduino
def write_h_file(array):
    import numpy as np
    with open('./arduino_main/centerpoints.h', 'w') as file:
        file.write('#ifndef CENTERPOINTS_H\n#define CENTERPOINTS_H\n\ndouble center_points[4][4] = {')
        i = 0
        for row in array:
            file.write('{')
            for element in row:
                file.write(str(int(element)) + ',')
            file.write(f'{i}}}')
            if i < 3:
                file.write(', ')
            i+=1
        file.write('};\n\n#endif')
        file.close()

# Plots the data used by k_means.py and the center points found into 3D scatter plot
def plot_results(data, center_points):
    import numpy as np
    import matplotlib.pyplot as plt
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

# Makes a confusion matrix from the results of running the algorithm on the Arduino
def plot_cm():
    from sklearn import metrics
    import matplotlib.pyplot as plt
    import pandas as pd
    df = pd.read_csv("./etc/alignment_data.csv")
    true = df['true']
    predicted = df['predicted']

    cm_display = metrics.ConfusionMatrixDisplay.from_predictions(y_true=true, y_pred=predicted, cmap='hot')
    cm_display.plot()
    plt.show()
    

if __name__ == '__main__':
    None
    