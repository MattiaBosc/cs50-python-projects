# Working 9 to 5

This project implements a Python program that converts times from 12-hour clock formats commonly used in the U.S. to 24-hour (military) time.

## Description

The program `working.py`:

- Implements a function `convert(s)` that:
  - Accepts a string in one of the following 12-hour formats:
    - `9:00 AM to 5:00 PM`
    - `9 AM to 5 PM`
    - `9:00 AM to 5 PM`
    - `9 AM to 5:00 PM`
  - Returns a string in 24-hour format, e.g., `09:00 to 17:00`.
  - Raises a `ValueError` if the input format is invalid or the times themselves are invalid (e.g., `12:60 AM`, `13:00 PM`, etc.).

- Supports conversions where the end time might be before the start time (e.g., `10:30 PM to 8 AM`).
