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

rockPlacment = set()

rockCreation = 0
maxHeight = 0
numRocks = 2022
windIndex = 0
while numRocks > 0:
    
    # Create Rock
    drawDirections = peices[rockCreation]
    adjustment = placementAdjustment[rockCreation]
    rockCreation = (rockCreation+1) % len(peices)
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
        windIndex = (windIndex+1) % len(winds)

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
            rockResting = True
            for r in rock:
                rockPlacment.add(tuple(r))
                if r[1] + 1 > maxHeight:
                    maxHeight = r[1] + 1

    numRocks -= 1

print(maxHeight)