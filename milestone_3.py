import random
word_list = ["watermelon", "nectarine", "strawberry", "kiwi", "raspberry"]
word = random.choice(word_list)
while True:
    guess = input("Guess one letter!: ")
    if guess.isalpha() and len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")