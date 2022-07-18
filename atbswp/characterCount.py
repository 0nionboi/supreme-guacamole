import pprint

print('Input message.')
message = input()

count = {} # dictionary that is going to hold all of our values.

for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1

pprint.pprint(count)