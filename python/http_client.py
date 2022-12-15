import requests
import csv

# Gets data from database, saves it in a csv file, and returns the file path
def get_data():
    data = requests.get("http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=70")

    string = data.text
    print(string)
    filename = "./python/accelerometer_data.csv"
    with open(f"{filename}", "w") as file:
        file.write(string)
    return filename
        
if __name__ == '__main__':
    get_data()