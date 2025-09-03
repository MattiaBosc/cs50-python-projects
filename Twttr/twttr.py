input = input("Input: ")
output = ""

for letter in input:
    if letter.upper() not in ["A", "E", "I", "O", "U"]:
        output += letter

print("Output: " + output)
