# Regular, um, Expressions

This project implements a Python program that counts occurrences of the word "um" in a line of text, ignoring case and ensuring it is matched as a standalone word.

## Description

The program `um.py`:

- Implements a function `count(s)` that:
  - Accepts a string `s` as input.
  - Returns an integer representing the number of times `"um"` appears in the input as a word by itself.
  - Matches `"um"` case-insensitively.
  - Does **not** count `"um"` when it appears as part of another word (e.g., `"yummy"` counts as 0).

- Uses regular expressions (optional) to detect word boundaries.

