import random

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

if __name__ == '__main__':
    fruit_list = ['apple', 'banana', 'grape', 'kiwi', 'strawberry']
    game = Hangman(fruit_list)
    print(game.word)
    print(game.num_letters)
    print(game.word_guessed)