# Wordle in Python

A command-line version of Wordle, built in Python. A random 5-letter word is chosen, and you get 6 guesses to figure it out.

## How to play

1. Run the program: `python word-guess.py`
2. Type a 5-letter guess and press Enter.
3. Read the feedback for each letter:
   - `[a]` means the letter is correct and in the right spot.
   - `(a)` means the letter is in the word but in a different spot.
   - `a` means the letter isn't in the word (or all copies are already accounted for).
4. Keep guessing until you win or run out of the 6 attempts.

**Example**

```
Welcome to Wordle!
Enter your guess: crane
[c] r (a) (n) e
Enter your guess: candy
[c] [a] [n] [d] [y]
Congratulations! You guessed the word in 2 tries!
```

## Features

- A different secret word every game, using `get_random_word()`
- Case-insensitive input (`CRANE`, `Crane`, and `crane` all work)
- Input validation: guesses that aren't 5 letters are rejected without costing an attempt
- Correct handling of repeated letters, using two passes (greens first, then yellows)
- Readable output with brackets and parentheses instead of raw marks

## How it works

The game marks each guess in two passes:

1. **Exact matches:** compare the guess to the secret word position by position and mark matches `G`. Matched letters are removed from a `remaining_letters` list.
2. **Misplaced letters:** for each position still marked `B`, check whether the letter is still in `remaining_letters`. If so, mark it `Y` and remove it.

Keeping these as separate passes means a green match always gets priority over a yellow one, which is how real Wordle handles duplicate letters.


## What I learned

- Using `for` and `while` loops together, including a `while` loop nested inside a `for` loop
- Tracking state with lists and updating them as the program runs
- Why the order of operations matters when handling duplicate letters
- Validating user input without breaking the flow of the game

## Author

Sadew Chamika
