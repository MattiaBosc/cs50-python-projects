def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[:2].isalpha() and s.isalnum():
        for i in range(len(s)):
            if s[i] == '0':
                return False
            elif s[i].isdecimal():
                s_1 = s[i:]
                return s_1.isdecimal()
        return True
    else:
        return False


main()
