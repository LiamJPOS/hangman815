import random

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print( f"Good guess! {guess} is in the word.")
        else:
            #TODO continue logic of check_guess method.
            print("booooo")
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

if __name__ == '__main__':
    fruit_list = ['apple', 'banana', 'grape', 'kiwi', 'strawberry']
    game = Hangman(fruit_list)
    game.ask_for_input()