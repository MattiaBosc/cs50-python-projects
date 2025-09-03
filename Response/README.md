# Response Validation

This project implements a Python program that validates whether a user-provided email address is syntactically correct, using a library from PyPI rather than regular expressions.

## Description

The program `response.py`:

- Prompts the user for an email address via `input()`.
- Uses a library such as `validator-collection` or `validators` to check the email’s syntax.
- Prints `Valid` if the email is syntactically correct.
- Prints `Invalid` if the email is syntactically incorrect.
- Does **not** validate whether the domain actually exists.

