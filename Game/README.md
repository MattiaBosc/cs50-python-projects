# Guessing Game

**Description:**  
`game.py` implements a number guessing game. The program chooses a random integer between 1 and a user-specified level `n`. The user then guesses the number, and the program provides feedback whether the guess is too small, too large, or correct.

**Behavior:**
1. Prompts the user for a level `n` (positive integer).
2. Randomly generates an integer between 1 and `n`, inclusive.
3. Prompts the user to guess the number:
   - If the guess is smaller: `Too small!`
   - If the guess is larger: `Too large!`
   - If the guess is correct: `Just right!` and exits.
4. Reprompts if the input is not a positive integer.

