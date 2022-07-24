#! python3
'''
tablePrint.py - prints a table in a nicer format, with each column right-justified.
'''

tableData = [['apples','bananas','cherries','duran'],
			['Alice','Bob','Carol','David'],
			['aardvarks','bears','cats','dogs']]

# Create an array to hold the lenght of the table data.

colWidths = [0] * len(tableData)

for listData in list(enumerate(tableData)): # iterate through each list of the table, enumerate gives the index of each item.
	# Check through the list of items for the one with the longest length.

	for listItem in listData[1]:
		if len(listItem) > colWidths[listData[0]]:
			colWidths[listData[0]] = len(listItem)

# Create a loop for printing the table.


for index in list(enumerate(tableData[0])):
	for listData in list(enumerate(tableData)):
		print(listData[1][index[0]].rjust(colWidths[listData[0]] + 2,' '), end = ' ')
	print()