def main():
    name = input("camelCase: ")
    print("snake_case: ", end="")
    snake_case(name)

def snake_case(string):
    for letter in string:
        if 'A' <= letter <= 'Z':
            print("_" + letter.lower(), end="")
        else:
            print(letter, end="")
    print()

main()
