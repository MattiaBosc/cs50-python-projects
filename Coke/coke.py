coke = 50

while coke > 0:
    coin = 0
    while coin not in [25, 10, 5]:
        print(f"Amount Due: {coke}")
        coin = int(input("Insert Coin: "))
    coke -= coin

print(f"Change Owed: {coke * -1}")
