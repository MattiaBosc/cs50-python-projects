months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if date.find("/") != -1:
        try:
            month, day, year = date.split("/")
        except:
            continue
    elif date.find(",") != -1:
        try:
            month, day, year = date.split(" ")
            day = day.strip(",")
            month = months.index(month) + 1
        except:
            continue
    else:
        continue
    try:
        day = int(day)
        month = int(month)
        year = int(year)
        if 1 <= day <= 31 and 1 <= month <= 12 and year >= 0:
            break
    except:
        pass

print(str(year) + "-" + f"{month:02}" + "-" + f"{day:02}")

