# This program says hello and asks for my name.  Follows instructions from page 11.

# Say "Hello, world!", using the print function.
print('Hello, world!')

print('What is your name?') # asks for name

myName = input()

print('It is good to meet you, ' + myName) # concats the printed string with the input from myName

print('The length of your name is:')

print(len(myName)) # len returns the length of a string of text

print('What is your age?')

myAge=input() # Allows the user to enter age, hopefully they enter an int

print('You will be ' + str(int(myAge) + 1) + ' in a year.') # doesn't matter if they don't enter an int, this will force it to be an int.

