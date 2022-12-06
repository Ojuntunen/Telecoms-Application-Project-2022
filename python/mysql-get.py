import mysql.connector
import authentication

db = mysql.connector.connect(user=authentication.USER,
                             password=authentication.PASSWORD,
                             host='172.20.241.9',
                             database='measurements')

cursor = db.cursor()

query = '''SELECT id, sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_e FROM rawdata WHERE groupid = 70 ORDER BY id DESC'''

cursor.execute(query)

for id in cursor:
    print(id, "\n")

cursor.close()
db.close()
