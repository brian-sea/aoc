f = open('inputfinal')
winds = f.read().strip()

WIDTH = 7
START_LEFT = 2
START_UP = 3

# Draw each peice (use addition from prev coordinate)
# (0,0) is the bottom left (right and up are x and y increasing)
peices = (
    ((0,0), (1,0), (1,0),(1,0)),            # horz line
    ((0,-1), (1,0), (0,1), (0,-2), (1,1)),  # cross
    ((0,-2), (1,0), (1,0), (0,1), (0,1)),  # l to the left
    ((0,0), (0,1), (0,1), (0,1)),         # vert line
    ((0,0), (0,-1), (1,0), (0, 1))          # square
)
# Adjust placement (left, up)
placementAdjustment = (
    (0,0),
    (0, 2),
    (0, 2),
    (0,0),
    (0, 1)
)

# Memozation
memory = {}

rockPlacment = set()

rockCreation = 0
maxHeight = 0
heightDropped = 0
numRocks = 1000000000000
windIndex = 0
while numRocks > 0:
    
    # Create Rock
    drawDirections = peices[rockCreation]
    adjustment = placementAdjustment[rockCreation]
    rock = []

    x,y = adjustment
    for d in drawDirections:
        x += d[0]
        y += d[1]
        rock.append([x,y])

    for r in rock:
        r[0] += START_LEFT
        r[1] += START_UP + maxHeight
    
    GRAVITY = -1
    rockResting = False
    while not rockResting:

        # Move By Wind
        xAdd = -1 if winds[windIndex] == '<' else 1

        canMove = True
        for r in rock:
            if (r[0]+xAdd, r[1]) in rockPlacment or r[0]+xAdd < 0 or r[0]+xAdd >= WIDTH:
                canMove = False
        if canMove:
            for r in rock:
                r[0] += xAdd
        
        # Move By Gravity
        canMove = True
        for r in rock:
            if (r[0], r[1]+GRAVITY) in rockPlacment or r[1]+GRAVITY < 0:
                canMove = False
        
        if canMove:
            for r in rock:
                r[1] += GRAVITY
        else:
            # Rock comes to rest
            rockResting = True
            for r in rock:
                rockPlacment.add(tuple(r))
                if r[1] + 1 > maxHeight:
                    maxHeight = r[1] + 1

            # Detect a complete line
            dropAt = 0
            for r in rock:
                completeLine = True
                for i in range(WIDTH):
                    if (i,r[1]) not in rockPlacment:
                        completeLine = False

                if completeLine:
                    dropAt = r[1]

            # Full Row, so move the floor (limits the set size)
            if dropAt > 0:
                newboard = set()
                for r in rockPlacment:
                    if r[1] >= dropAt:
                        newboard.add( (r[0], r[1]-dropAt))
                rockPlacment = newboard
                maxHeight -= dropAt
                heightDropped += dropAt
            
            # Cycle Detection
            # Get a height map of the current placement
            heights = [0]*WIDTH
            for p in rockPlacment:
                if p[1] > heights[ p[0] ]:
                    heights[ p[0] ] = p[1]

            sig = (rockCreation, windIndex, tuple(heights))
            if( sig in memory):
                # Cycle Detected
                oldMaxHeight, oldNumRocks = memory[sig]
                numInCycle = oldNumRocks - numRocks
                heightDiff = (maxHeight+heightDropped) - oldMaxHeight
                numCycles = numRocks // numInCycle
                heightDropped += numCycles * heightDiff
                numRocks -= numCycles*numInCycle
            memory[sig] = (maxHeight+heightDropped, numRocks)

        windIndex = (windIndex+1) % len(winds)
    rockCreation = (rockCreation+1) % len(peices)
    numRocks -= 1

print(maxHeight+heightDropped)


# Guess: 574717187 (too low)
# Guess: 1302348627560 (too low)