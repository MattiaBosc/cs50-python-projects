import sys

if len(sys.argv) != 2:
    sys.exit("One command-line argument expected")

if sys.argv[1].find(".py") == -1:
    sys.exit("Python file expected")

count = 0
try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if len(line) != 0 and line.startswith("#") == False:
                count += 1
except FileNotFoundError:
    sys.exit("File not found")

print("Lines: ", count)
