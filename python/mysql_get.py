import mysql.connector
import authentication

def get_data():
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


if __name__ == '__main__':
    get_data()