import random


def main():
    level = get_level()
    count = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        j = 0
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer != x + y:
                    print("EEE")
                    j += 1
                else:
                    count += 1
                    break
            except:
                print("EEE")
                j += 1
            if j == 3:
                print(f"{x} + {y} = {x+y}")
                break
    print(f"Score: {count}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except:
            pass


def generate_integer(level):
    if level == 1:
        min = 0
    else:
        min = pow(10, level-1)
    n = random.randint(min, pow(10, level)-1)
    return n


if __name__ == "__main__":
    main()
