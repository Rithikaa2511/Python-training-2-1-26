import csv

with open("day-10/StudentsData.csv",'r')as Data:
    reader = csv.reader(Data)
    for row in reader:
        print(row)
