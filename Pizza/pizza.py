import sys
import csv
import tabulate

if len(sys.argv) != 2:
    sys.exit("One command-line argument expected")

if sys.argv[1].find(".csv") == -1:
    sys.exit("Python file expected")

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File not found")

