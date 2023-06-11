# Conway's Game of Life
import random, time, copy

WIDTH = 79
HEIGHT = 20
ALIVE = 'O'
DEAD = ' '

# create a list of lists for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
        #if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):            
            column.append(ALIVE)  # add a living cell
        else:
            column.append(DEAD)  # add a dead cell
    nextCells.append(column)  # nextCells is a list of column lists

while True: # main program loop
    print('\n\n\n\n\n')  # separate each step with newlines
    currentCells = copy.deepcopy(nextCells)

    # print currentCells on screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end=' ') # print hash or space
        print()   # print newline at the end of the row

    # calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighboring coordinates
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord]=='#':
                numNeighbors += 1 # top-left neighbor alive
            if currentCells[x][aboveCoord]=='#':
                numNeighbors += 1 # top neighbor alive
            if currentCells[rightCoord][aboveCoord]=='#':
                numNeighbors += 1 # top-right neighbor alive
            if currentCells[leftCoord][y]=='#':
                numNeighbors += 1 # left neighbor alive
            if currentCells[rightCoord][y]=='#':
                numNeighbors += 1 # right neighbor alive
            if currentCells[leftCoord][belowCoord]=='#':
                numNeighbors += 1 # bottom-left neighbor alive
            if currentCells[x][belowCoord]=='#':
                numNeighbors += 1 # bottom neighbor alive
            if currentCells[rightCoord][belowCoord]=='#':
                numNeighbors += 1 # bottom-right neighbor alive

            # set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors==2 or numNeighbors==3):
                # living cells with 2-3 neighbors live:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
    # add a 1-sec pause to reduce flickering
    time.sleep(1)
