import requests

data = requests.get("http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=70")
string = data.text
#print(string)
with open("./python/accelerometer_data.csv", "w") as file:
    file.write(string)