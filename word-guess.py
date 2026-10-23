from words import get_random_word

NUM_ATTEMPTS = 6

def main():
    print("Welcome to Wordle!")
    secret_word = get_random_word()

    for attempt in range(NUM_ATTEMPTS):
        # Keep asking until the guess is exactly 5 letters
        while True:
            user_guess = input("Enter your guess: ").lower()
            if len(user_guess) == 5:
                break
            print("Please enter a 5-letter word.")

        result = []
        remaining_letters = []

        for letter in secret_word:
            remaining_letters.append(letter)

        # Pass 1: greens
        for i in range(len(secret_word)):
            if secret_word[i] == user_guess[i]:
                result.append("G")
                remaining_letters.remove(user_guess[i])
            else:
                result.append("B")

        # Pass 2: yellows
        for i in range(len(secret_word)):
            if result[i] == "B" and user_guess[i] in remaining_letters:
                result[i] = "Y"
                remaining_letters.remove(user_guess[i])

        # Pass 3: build the display
        display = ""
        for i in range(len(user_guess)):
            if result[i] == "G":
                display += "[" + user_guess[i] + "] "
            elif result[i] == "Y":
                display += "(" + user_guess[i] + ") "
            else:
                display += user_guess[i] + " "

        print(f'Result: {display}')

        # Check for a win
        if user_guess == secret_word:
            print("Congratulations! You guessed the word in " + str(attempt + 1) + " tries!")
            return

    print("Better luck next time! The correct word was '" + secret_word + "'.")


if __name__ == "__main__":
    main()