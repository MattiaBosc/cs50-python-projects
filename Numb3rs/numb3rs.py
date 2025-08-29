import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    numbers = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip.strip())
    if numbers:
        for i in range(len(numbers.groups())):
            number = int(numbers.group(i+1))
            if number < 0 or number > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
