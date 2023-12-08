import random

word_list = ['apple', 'banana', 'grape', 'kiwi', 'strawberry']

word = random.choice(word_list)

guess = input('Guess a letter: ')
if len(guess) == 1 and guess.isalpha():
	print('Good guess')
else: 
	print('Oops that\'s not a valid input')

print(word)
