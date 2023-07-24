# program to demonstrate CV File Handling - 1 (Display all rows)
import csv

with open("demo.csv", "r") as fileobj:
    readerobj = csv.reader(fileobj)
    print("***Employee Records****")
    next(readerobj)  # to skip first row (fields row)
    for row in readerobj:
        print(row)
