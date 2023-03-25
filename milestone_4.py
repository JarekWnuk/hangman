import random
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.word_guessed = []
        for letter in self.word:
            self.word_guessed.append("_")
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess.lower() in self.word:
            print(f"Good guess! {guess.lower()} is in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Guess one letter!:")
            if guess.isalpha() and len(guess) > 1:
                print("Invalid letter. Please, enter a single alphabetical character.")            
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break