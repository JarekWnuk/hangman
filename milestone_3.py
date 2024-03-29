import random
word_list = ["watermelon", "nectarine", "strawberry", "kiwi", "raspberry"]
word = random.choice(word_list)

def check_guess(guess):
    if guess.lower() in word:
        print(f"Good guess! {guess.lower()} is in the word.")
    else:
        print(f"Sorry, {guess.lower()} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess one letter!: ")
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()