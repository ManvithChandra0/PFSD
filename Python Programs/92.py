# program to demonstrate CV File Handling - 7 (writing data into existing CSV file)
import csv

with open("demo1.csv", "a", newline="") as fileobj:
    writerobj = csv.writer(fileobj)
    writerobj.writerow([3, "charan", 1111.50])
    writerobj.writerow([4, "nithya", 4000])
print(" Write Operation done Successfully ... ! ")
