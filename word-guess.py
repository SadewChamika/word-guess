from words import get_random_word
from words import MAX_LENGTH
from art import TITLE


NUM_ATTEMPTS = 6
START_LENGTH = 3


#comparing user input with the secret word
def get_feedback(secret_word, user_guess ):

    result = []
    remaining_letters = []

    for letter in secret_word:
        remaining_letters.append(letter)

    for i in range(len(secret_word)):
        if secret_word[i] == user_guess[i]:
            result.append("G")
            remaining_letters.remove(user_guess[i])
        else:
            result.append("B")

    for i in range(len(secret_word)):
        if result[i] == "B" and user_guess[i] in remaining_letters:
            result[i] = "Y"
            remaining_letters.remove(user_guess[i])
    return result

#display function 
def format_result(user_guess, result):
    display = ""
    for i in range(len(user_guess)):
            if result[i] == "G":
                display += "[" + user_guess[i] + "] "
            elif result[i] == "Y":
                display += "(" + user_guess[i] + ") "
            else:
                display += user_guess[i] + " "
    return display

def ask_for_guess(word_length):
    while True:
        user_guess = input("Enter your guess: ").lower()
        if len(user_guess) == word_length:
            return user_guess
        print(f"Please enter a {word_length}-letter word.")

#levels in the game
def play_level(level, word_length):
    print(f"\n=== Level {level} ===")
    print(f"Guess the {word_length}-letter word!")
    secret_word = get_random_word(word_length)

    for attempt in range(NUM_ATTEMPTS):
        user_guess = ask_for_guess(word_length)
        result = get_feedback(secret_word, user_guess)
        print(f"Result: {format_result(user_guess, result)}")

        if user_guess == secret_word:
            print(f"You got it in {attempt + 1} tries!")
            return True

    print(f"Out of attempts! The word was '{secret_word}'.")
    return False

def main():
    print(TITLE)
    max_level = MAX_LENGTH - START_LENGTH + 1
    level = 1
    
    while level <= max_level:
        word_length = START_LENGTH + level - 1
        won = play_level(level, word_length)
        if won:
            level += 1
        else:
            print(f"Game over! You reached level {level}.")
            break
    else:
        print("You beat every level. You win the game!")
    
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()