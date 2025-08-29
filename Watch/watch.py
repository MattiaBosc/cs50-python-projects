import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.match(r"(.+)\"https?://(www\.)?youtube\.com/embed/(.+)\"(.+)", s)
    if matches:
        return "https://youtu.be/" + matches.group(3)
    else:
        return "None"


if __name__ == "__main__":
    main()
