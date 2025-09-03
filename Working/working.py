import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.match(r"(\d+:?\d* [APM]+) to (\d+:?\d* [APM]+)", s.strip())
    if matches:
        return am_pm(matches, 1) + " to " + am_pm(matches, 2)
    else:
        raise ValueError

def am_pm(matches, part):
        hour, letter = matches.group(part).split(" ")
        if ":" in hour:
            hour, minute = hour.split(":")
        else:
            minute = "00"
        try:
            hour = int(hour)
            minute = int(minute)
            if (hour > 12 or hour <= 0) or (minute >= 60 or minute < 0):
                raise ValueError
            if "A" in letter and hour == 12:
                hour = 0
            elif "P" in letter:
                if hour != 12:
                    hour += 12
        except:
            raise ValueError
        return "{:02d}".format(hour) + ":" + "{:02d}".format(minute)



if __name__ == "__main__":
    main()
