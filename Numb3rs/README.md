# NUMB3RS

This project implements a Python program to validate IPv4 addresses, inspired by a scene in the TV show NUMB3RS.

## Description

The program `numb3rs.py`:

- Implements a function `validate(ip)` that:
  - Takes a string as input representing an IPv4 address.
  - Returns `True` if the string is a valid IPv4 address.
  - Returns `False` otherwise.
- A valid IPv4 address must:
  - Consist of four numeric parts separated by dots (e.g., `192.168.0.1`).
  - Each part must be an integer between 0 and 255, inclusive.
  - Contain no leading zeros (e.g., `192.168.001.1` is invalid).
  - Contain only digits and dots, no extra characters.
- The program prompts the user for an IPv4 address and prints the result of `validate`.
