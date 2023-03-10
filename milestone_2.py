import random
word_list = ["watermelon", "nectarine", "strawberry", "kiwi", "raspberry"]
word = random.choice(word_list)
guess = input("Guess one letter!: ")
if guess.isalpha() and len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")