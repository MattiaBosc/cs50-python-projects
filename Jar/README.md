# Cookie Jar

This project implements a Python class `Jar` to simulate a cookie jar, allowing you to deposit and withdraw cookies, while keeping track of the jar’s capacity.

## Description

The `Jar` class provides the following functionality:

- `__init__(capacity=12)`: Initializes a cookie jar with a maximum number of cookies. Raises a `ValueError` if capacity is not a non-negative integer.
- `__str__()`: Returns a string with 🍪 emojis representing the number of cookies in the jar.
- `deposit(n)`: Adds `n` cookies to the jar. Raises a `ValueError` if this would exceed the jar’s capacity.
- `withdraw(n)`: Removes `n` cookies from the jar. Raises a `ValueError` if there are not enough cookies.
- `capacity`: Property that returns the jar’s maximum capacity.
- `size`: Property that returns the current number of cookies in the jar.

## Requirements

- Python 3

## Usage

You can use the `Jar` class by importing it in your Python script:

```python
from jar import Jar

jar = Jar(capacity=10)
jar.deposit(3)
print(jar)  # Output: 🍪🍪🍪
jar.withdraw(1)
print(jar.size)  # Output: 2
