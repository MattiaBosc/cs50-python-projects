# Lines of Code (LOC)

This project implements a Python program that counts the number of lines of code in another Python file, **excluding comments and blank lines**. 

## Description

The program `lines.py`:

- Expects **exactly one command-line argument**: the path to a Python file.
- Outputs the **number of lines of code** in that file, ignoring:
  - Lines starting with `#` (comments, optionally preceded by whitespace)
  - Blank lines (lines containing only whitespace)
- Does **not** count docstrings as comments.
- Exits with an error message if:
  - The number of command-line arguments is not exactly one.
  - The file does not have a `.py` extension.
  - The file does not exist.
