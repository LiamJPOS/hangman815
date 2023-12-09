import random
class Hangman():
    '''Runs an instance of the hangman game.'''
    def __init__(self):
        self.word_list = ['apple', 'banana', 'grape', 'kiwi', 'strawberry']
        self.word = random.choice(self.word_list)
    
    def check_guess(self, guess):
        '''Checks if user input is in the word to be guessed.''' 
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
                
    def ask_for_input(self):      
        '''Asks user for input and checks if input is a single alphabetical character. It then runs check_guess'''
        while True:   
            guess = input('Guess a letter: ')
            if guess.isalpha():
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
        self.check_guess(guess)

if __name__ == "__main__":
    new_game = Hangman()
    new_game.ask_for_input()
