import random
class Hangman:
    def __init__(self, word_list, num_lives=5):             # class constructor requires a list of words and optionally number of lives, which defaults to 5 if not passed
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)                # chooses a word to guess from word_list
        self.num_letters = len(set(self.word))
        self.word_guessed = []
        for letter in self.word:
            self.word_guessed.append("_")                   # creates a list with underscores for each letter of the secret word
        self.list_of_guesses = []

    def check_guess(self, guess): 
        if guess.lower() in self.word:                      # checks if the guessed letter is in the secret word
            print(f"Good guess! {guess.lower()} is in the word.")
            for count, letter in enumerate(self.word):
                if letter == guess.lower():                 # converts the guessed letter to lowercase
                    self.word_guessed[count] = letter       # replaces the underscore in the secret word list with the guessed letter
            self.num_letters -= 1                           # reduces the number of unique letters that remain hidden
            print(" ".join(self.word_guessed))
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess.lower()} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            print(" ".join(self.word_guessed))

    def ask_for_input(self):        
        while True:
            guess = input("Guess one letter!:")
            if guess.isalpha() and len(guess) > 1:          # checks if input is one letter
                print("Invalid letter. Please, enter a single alphabetical character.")            
            elif guess in self.list_of_guesses:             # checks if the letter has been guessed before
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)          #adds the guessed letter to a list of previous guesses                 
                break
def play_game(word_list):                                   # function that contains logic for running the game
    num_lives = 4
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:                             # if no lives left the game ends
            print("You lost!")
            break
        elif game.num_letters > 0:                          # if the player still has lives left and there are hidden letters remaining: the game continues
            game.ask_for_input()
        else:                                               # player wins the game if they still have lives left and there are no hidden letters remaining
            print("Congratulations. You won the game!")
            break
play_game(["apple", "cherry", "orange", "watermelon"])
