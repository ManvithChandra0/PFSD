# program to demonstrate CV File Handling -6 (writing data into new CSV file)
import csv

with open("demo1.csv", "w",newline='') as fileobj:
    writerobj = csv.writer(fileobj)
    writerobj.writerow(["empid", "empname", "empsal"])
    writerobj.writerow([1, "klu", 1234.50])
    writerobj.writerow([2, "surya", 5000])

print("Success")