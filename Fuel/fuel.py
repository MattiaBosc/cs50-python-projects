def main():
    fraction = get_fraction()
    percentage = int(round( 100.0 * fraction, 0))
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}" + "%")

def get_fraction():
    while True:
        fraction = input("Fraction: ")
        try:
            numerator, denominator = fraction.split("/")
            numerator = int(numerator)
            denominator = int(denominator)
            if numerator <= denominator:
                return numerator/denominator
        except (ValueError, ZeroDivisionError):
            pass

main()
