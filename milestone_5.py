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
        '''Checks if guessed letter is in the generated word'''
        guess = guess.lower()
        if guess in self.word:
            print( f"Good guess! {guess} is in the word.")
            for letter in enumerate(self.word):
                if letter[1] == guess:
                    self.word_guessed[letter[0]] = guess
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        '''Takes single alphabetic character as input, checks it is valid, or hasn't been used before, and uses it in the check_guess method'''
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
                
            elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    '''Initialises an instance of Hangman and tracks the win or lose condition
    '''
    #TODO Create better docstrings
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

if __name__ == '__main__':
    fruit_list = ['apple', 'banana', 'grape', 'kiwi', 'strawberry']
    play_game(fruit_list)