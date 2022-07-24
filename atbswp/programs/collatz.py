import sys

# collatz function
def collatz(userNumber):
	if userNumber == 1:
		return None
	elif userNumber % 2 == 0: # If number is even.
		print(userNumber // 2)
		collatz(userNumber//2)
	else:
		print(3*userNumber+1)
		collatz(3*userNumber+1)


# Main function, 

while True:
	print('Collatz sequence printer.  Enter a number.  Enter q to (q)uit.')

# user input loop.
	userNumber = input()

	if userNumber == 'q':
		sys.exit()
	else:
		collatz(int(userNumber))