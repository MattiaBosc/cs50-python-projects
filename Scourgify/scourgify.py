import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Two command-line arguments expected")

try:
    file_1 = open(sys.argv[1], "r")
    reader = csv.DictReader(file_1)
except:
    sys.exit("File not found")

with open(sys.argv[2], "w") as file_2:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(file_2, fieldnames = fieldnames)
    writer.writeheader()
    for dict in reader:
        last, first = dict["name"].strip("\"").split(",")
        writer.writerow({"first": first.strip(), "last": last, "house": dict["house"]})

file_1.close()
