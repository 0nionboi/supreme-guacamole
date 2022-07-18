name = '' #double single quotes equals the empty string, which is considered a falsey value. 

while not name: # equals while not false, so it will ask until name has a value, prevents the user from entering a zero value
	print('Enter name:')
	name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests: #if this variable gets put in as zero it will skip the following print
	print('Be sure to have enough room for all your guests.')

print('Done.')