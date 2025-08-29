import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > number:
            print("Too large!")
        elif number > guess:
            print("Too small!")
        else:
            print("Just right!")
            break
    except:
        pass
