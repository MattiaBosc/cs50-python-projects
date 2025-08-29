from datetime import date
import re
import inflect
import sys


def main():
    birth_date = input("Date of Birth: ")
    minutes = convert(birth_date) * 60 * 24
    print(sing(minutes))



def convert(birth_date):
    if matches := re.match(r"(\d\d\d\d)-(\d\d)-(\d\d)", birth_date):
        try:
            birth_date = date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))
            today = date.today()
            return (today - birth_date).days
        except ValueError:
            raise ValueError("Invalid Date")
    else:
        sys.exit("Invalid Date Format")


def sing(minutes):
    p = inflect.engine()
    minutes = p.number_to_words(minutes, andword="")
    return minutes.capitalize() + " minutes"


if __name__ == "__main__":
    main()
