import requests
import csv

data = requests.get("http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=70")
'''

file = open("./python/accelerometer_data.csv", "w")
writer = csv.writer(file)



string.replace(old='"', new='')
for i in string:
    writer.writerows(i)
   
'''
string = data.text
print(string)
with open("./python/accelerometer_data.csv", "w") as out:
    out.write(string)     
