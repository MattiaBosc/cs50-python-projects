# Pizza Py

This project implements a Python program that formats Pinocchio’s Pizza & Subs menu CSV files as an ASCII table.

## Description

The program `pizza.py`:

- Expects **exactly one command-line argument**: the path to a CSV file containing pizza data.
- Reads the CSV file and prints it as a **nicely formatted ASCII table** using the `tabulate` Python library.
- Uses the `grid` format of `tabulate` to create table borders.
- Exits with an error message if:
  - The number of command-line arguments is not exactly one.
  - The file does not have a `.csv` extension.
  - The file does not exist.

