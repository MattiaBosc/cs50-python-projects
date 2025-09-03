# Little Professor

**Description:**  
`professor.py` simulates a “Little Professor” toy that quizzes the user with ten addition problems. The user must solve each problem and gets up to three tries per problem. After three incorrect attempts, the program displays the correct answer.

**Behavior:**
1. Prompts the user for a level `n` (1, 2, or 3). Reprompts if invalid.
2. Randomly generates ten addition problems:
   - Each integer has `n` digits.
   - Each problem is formatted as `X + Y =`.
3. For each problem:
   - User inputs an answer.
   - If incorrect or invalid, outputs `EEE` and reprompts (up to three tries).
   - After three incorrect attempts, displays the correct answer.
4. After all problems, outputs the total score out of 10.

