import math
f = open('inputfinal')

head = [0,0]
tail = []
for i in range(9):
    tail.append( (0,0) )

locations = {(0,0):0}

# Map directions
directions = {
    "L" : (-1,0),
    "R" : (1,0),
    "U" : (0,1),
    "D" : (0,-1)
}

for line in f:
    dir, amt = line.split(' ')
    amt = int(amt)

    dx, dy = directions[dir]

    for i in range(amt):
        head = [ x + y for x,y in zip(head, [dx, dy])]

        spot = 0
        moveHead = tuple(head)
        while spot < len(tail):
            move = list(tail[spot])
            for j in range(2):
                if abs(moveHead[j]-move[j]) == 2:
                    move[j] = (moveHead[j]+move[j])//2
                    
                    if moveHead[(j+1)%2]-move[(j+1)%2] != 0:
                        move[(j+1)%2] += math.copysign(1, (moveHead[(j+1)%2]-move[(j+1)%2]) )
                        
            moveHead = tail[spot] = tuple(move)
            locations[ tail[-1] ] = 0            
            spot += 1

print(len(locations))

# Guess: 2250
# Guess: 2543
# Guess: 2885