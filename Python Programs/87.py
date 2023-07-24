# program to demonstrate CV File Handling - 2 ((Displaying rows with index)
import csv

with open("demo.csv", "r") as fileobj:
    readerobj = csv.reader(fileobj)
    print("***Employee Records****")
    next(readerobj)  # to skip first row (fields row)
    for row in readerobj:
        print(row[0], row[1], row[2], row[3], row[4])