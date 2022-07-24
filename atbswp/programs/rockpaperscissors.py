# It's rock, paper, scissors.

import random, sys # sys is used for sys.exit(), which gives us the ability to quit the program.

print('ROCK, PAPER, SCISSORS')

# These variables will track wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop
	print('%s Winds, %s Losses, %s Ties' % (wins,losses,ties)) #uses the % thing to throw those values into the string
	

	while True: # the player input loop
		print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit.')
		playerMove = input()
		if playerMove == 'q':
			sys.exit() #Quit the program.
		if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
			break # breaks out of this input loop.
		print('Type one of r,p,s, or q.')

	# Display the move that the player chose.
	if playerMove == 'r':
		print('ROCK versus ...')
	if playerMove == 'p':
		print('PAPER versus ...')
	if playerMove == 's':
		print('SCISSORS versus ...')

	# Chose a move for the computer and display it.
	randomNumber = random.randint(1,3)
	if randomNumber == 1:
		computerMove = 'r'
		print('ROCK')
	if randomNumber == 2:
		computerMove = 'p'
		print('PAPER')
	if randomNumber == 3:
		computerMove = 's'
		print('SCISSORS')

	# logic out the winner add to the win/loss tracker.
	if playerMove == computerMove:
		print('TIE.')
		ties = ties + 1
	elif playerMove == 'r' and computerMove == 's':
		print('YOU WIN.')
		wins = wins + 1
	elif playerMove == 'p' and computerMove == 'r':
		print('YOU WIN.')
		wins = wins + 1
	elif playerMove == 's' and computerMove == 'p':
		print('YOU WIN.')
		wins = wins + 1
	elif playerMove == 's' and computerMove == 'r':
		print('YOU LOSE.')
		losses = losses + 1
	elif playerMove == 'p' and computerMove == 's':
		print('YOU LOSE.')
		losses = losses + 1
	elif playerMove == 'r' and computerMove == 'p':
		print('YOU LOSE.')
		losses = losses + 1

