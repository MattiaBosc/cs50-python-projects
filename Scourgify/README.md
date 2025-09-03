# Scourgify

This project implements a Python program that cleans and reformats student data from a CSV file, splitting full names into first and last names.

## Description

The program `scourgify.py`:

- Expects **exactly two command-line arguments**:
  1. The name of an existing CSV file to read as input (assumed columns: `name` and `house`).
  2. The name of a new CSV file to write as output (columns: `first`, `last`, `house`).
- Reads the input CSV, splits each student’s full name into first and last names.
- Writes the cleaned data to the output CSV in the correct column order.
- Exits with an error message if:
  - The number of command-line arguments is not exactly two.
  - The input file cannot be read.
