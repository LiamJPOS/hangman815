from milestone_2 import Hangman

def check_guess(guess):
    '''Checks if user input is in the word to be guessed.''' 
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():      
    '''Asks user for input and checks if input is a single alphabetical character. It then runs check_guess'''
    while True:   
        guess = input('Guess a letter: ')
        if guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue
    check_guess(guess)

