import random
class Hangman():
    '''Runs an instance of the hangman game.'''
    def __init__(self):
        self.word_list = ['apple', 'banana', 'grape', 'kiwi', 'strawberry']
        self.word = random.choice(self.word_list)
    
    def guess_letter(self):
        while True:
            guess = input('Guess a letter: ')
            if guess != 1 and guess.isalpha() == False:
                print('Oops that\'s not a valid input')
                continue
            else:
                print('Good guess')
                break
            

