# Fuel Gauge

**Description:**  
This project is a Python program called `fuel.py` that calculates the amount of fuel in a tank based on a fraction input by the user. The user inputs a fraction `X/Y` (both positive integers), and the program outputs the fuel level as a percentage, rounded to the nearest integer. Special cases:

- `E` if 1% or less remains (essentially empty)  
- `F` if 99% or more remains (essentially full)  

The program ensures valid input: X and Y must be integers, Y cannot be 0, and X cannot exceed Y. Exceptions like `ValueError` or `ZeroDivisionError` are handled, and invalid input prompts the user again.

