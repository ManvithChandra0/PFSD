# program to demonstrate CV File Handling - 8
import csv

with open ("demo2.csv", "w", newline="") as outputfileobj:
    writerobj = csv.writer(outputfileobj)
    with open("demo1.csv","r") as inputfileobj:
        readerobj = csv.reader(inputfileobj)
        for row in readerobj:
            writerobj.writerow(row)
print("Write Operation done Successfully ... !! ")