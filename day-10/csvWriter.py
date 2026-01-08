import csv 

with open("day-10/StudentsData.csv",'w')as Data:
    writer = csv.writer(Data)
    writer.writerow(["S.NO","Name","Dept"])
    writer.writerow([1,"Prasanth","CSE"])
    writer.writerow([2,"Rithanyaa","MSC"])
    writer.writerow([3,"Rithikaa","ECE"])


    