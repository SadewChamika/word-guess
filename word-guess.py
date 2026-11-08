from words import get_random_word

NUM_ATTEMPTS = 6
word_length = 4

result = []
remaining_letters = []

#comparing user input with the secret word
 
def get_feedback(secret_word, user_guess ):
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

    



def main():
    print("Welcome to Wordle!")
    secret_word = get_random_word(word_length)
    
    for attempt in range(NUM_ATTEMPTS):
        
        while True:
            user_guess = input("Enter your guess: ").lower()
            if len(user_guess) == word_length:
                break
            print(f"Please enter a {word_length}-letter word.")

        get_feedback(secret_word, user_guess)

        display = format_result(user_guess, result)

        print(f'Result: {display}')

        # Check for a win
        if user_guess == secret_word:
            print("Congratulations! You guessed the word in " + str(attempt + 1) + " tries!")
            input("Press Enter to exit...")
            return

    print("Better luck next time! The correct word was '" + secret_word + "'.")
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()