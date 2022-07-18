# From page 49, creating a guess the number game.  Will give the players 7 guesses, and when it ends will tell the players how many guesses they got it in.

import random

secretNumber = random.randint(1,20)

print('I am thinking of a number between 1 and 20.')

# Ask the player for 7 guesses.
for guessesTaken in range (0,7):
	print('Take a guess.')
	guess = int(input())

	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your guess is too high.')
	else:
		break # This condition happens when the correct guess is chosen.

if guess == secretNumber:
	print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('Sorry, the number I was thinking of was ' + str(secretNumber))
