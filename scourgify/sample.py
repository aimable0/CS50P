import csv

name = "Aimable"
house  = "Gisenyi"

with open("sample.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(["Didier", "Gisenyi"])
    writer.writerow([name, house])
