list = {}
while True:
    try:
        item = input("").upper()
        if item in list:
            list[f"{item}"] += 1
        else:
            list[f"{item}"] = 1
    except EOFError:
        print()
        break

sorted_list = sorted(list)
for i in range(len(sorted_list)):
    item = sorted_list[i]
    print(list[f"{item}"], item)


