# Conway's Game of Life
import random, sys, time, copy
WIDTH = 40
HEIGHT = 20

# Create a list for the cells:
nextCells = []
for x in range(WIDTH):
	column = [] # create a new column
	for y in range(HEIGHT):
		if random.randint(0,1)==0:
			column.append('#') # Add a living cell
		else:
			column.append(' ') # Add a dead cell
	nextCells.append(column) # nextCells is a list of column lists

while True: # Main program loop
	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n') # clears the board for the next step.
	currentCells = copy.deepcopy(nextCells)

	# Print currentCells on the screen:
	for y in range(HEIGHT):
		for x in range(WIDTH):
			print(currentCells[x][y], end='')
		print() #prints a newline at the end

	# Calculates the next step's cells based on current cells.
	for x in range(WIDTH):
		for y in range(HEIGHT):
			# Get neighboring coordinates:
			# '%WIDTH' ensures that leftCoord is always between 0 and WIDTH-1
			leftCoord = (x-1)% WIDTH
			rightCoord = (x+1)% WIDTH
			aboveCoord = (y-1)% HEIGHT
			belowCoord = (y+1)% HEIGHT

			# Count the number of living neighbors
			numNeighbors = 0
			if currentCells[leftCoord][aboveCoord] == '#':
				numNeighbors += 1 
			if currentCells[x][aboveCoord] == '#':
				numNeighbors += 1 
			if currentCells[rightCoord][aboveCoord] == '#':
				numNeighbors += 1 
			if currentCells[leftCoord][y] == '#':
				numNeighbors += 1 
			if currentCells[rightCoord][y] == '#':
				numNeighbors += 1 
			if currentCells[leftCoord][belowCoord] == '#':
				numNeighbors += 1 
			if currentCells[x][belowCoord] == '#':
				numNeighbors += 1 
			if currentCells[rightCoord][belowCoord] == '#':
				numNeighbors += 1 

		# Set cell based on Conway's Game of Life rules:
			if currentCells[x][y]=='#' and (numNeighbors ==2 or numNeighbors == 3):
				# Living cells with 2 or 3 neighbors stay alive.
				nextCells[x][y] = '#'
			elif currentCells[x][y] == ' ' and numNeighbors == 3:
				# Dead cells with 3 neighbors become alive.
				nextCells[x][y] = '#'
			else:
				nextCells[x][y] = ' '
	time.sleep(.05) # 1 second delay between cells.