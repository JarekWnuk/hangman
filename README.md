# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone 2

In this phase of the game creation the initial variables are created. These will hold important information like the words available to guess and the user input.
The random guess word selection is also implemented.
Description of the code is listed below:  

- Variable word_list contains a list of the creator's 5 favourite fruits.

- Python's random module is used to randomly pick one of the fruits from the word_list. Output is stored in the variable word.

The following code is executed:

word = random.choice(word_list)

- User is asked for an input using Python's input() function.

- The input is stored in a variable called guess.

The following code is executed:

guess = input("Guess one letter!: ")

- The code checks the user input, which needs to be one letter. 

This is done using an if statement that checks the following conditions:

guess.isalpha()    # verifies that the input is alphabetical

len(guess) == 1    # verifies that the input is only one character

If the output from both statements is True, then the follwoing code is executed:

print("Good guess!")

Otherwise the program executes:

print("Oops! That is not a valid input.")

# Conclusion

The game needs a way to handle incorrect user input. Currently the code stops with a message to the user.
The correct way to improve this would be to set up a loop that asks for user input until it is valid.

# Milestone 3

In this milestone two functions are added to the game that improve the logic and make the code more tidy. Details are described below:

- function ask_for_input() adds a while loop to the existing code used to check user input in Milestone 2. Now, if the input is invalid the code loops to the input request until a valid input is received.
This is achieved by adding a infinite while loop and breaking out once the required condition is met. See the explained code below:

While True: # While loop with condition True is infinite 
  get user input
  if user input is valid
    break out of infinite While loop
  otherwise 
    print message to user and loop

- the check_guess function takes the letter guessed by the player as an argument and does the following:

uses .lower() string function on guess in case a capital letter has been enetered



checks if the guessed letter is in the secret word
 
