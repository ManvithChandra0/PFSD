# program to demonstrate CV File Handling - 5 (Displaying Total Salary)
import csv

with open("demo.csv", "r") as fileobj:
    readerobj = csv.reader(fileobj)
    next(readerobj)  # to skip first row (fields row)
    totalsal = 0.0
    for row in readerobj:
        totalsal = totalsal + float(row[3])
        print("Total Salary:", totalsal)