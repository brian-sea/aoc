import re
import datetime
from collections import defaultdict
        
f = open("finalinput")
lines = [line.strip() for line in f.readlines()]

# (y,x)
# S and E are positive
directions = {
    "|" : [ [-1,0],  [1,0] ],                # NS
    "-" : [ [0,-1],  [0,1] ],                # WE
    "L" : [ [-1,0], [0, 1] ],                # NE
    "J" : [ [-1,0], [0,-1] ],                # NW
    "7" : [ [1,0],  [0,-1] ],                # SW
    "F" : [ [1,0],  [0, 1] ],                # SE
    "." : [ [float('inf'),float('inf')] ],   # Ground
    "S" : [ ],                               # Start
}

start = [0,0]
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == 'S':
            start = [y,x]
            # Figure out starting piece 
            for gy in range(y-1,y+2):
                if( 0 <= gy < len(lines)):
                    for gx in range(x-1,x+2):
                        if( 0 <= gx < len(lines[gy]) ):
                            gSym = lines[gy][gx]
                            search = directions[gSym]

                            for s in search:
                                if( gy + s[0] == y and gx + s[1] == x):
                                    directions['S'].append([-s[0],-s[1]])


# (y,x) : (numSteps, cameFrom)
visited = {
}
visited[str(start)] = (-1,start)

start.append(start)
queue = [start]         
s = 0
while len(queue) > 0:

    # Handle next element
    loc = queue.pop(0)
    if(str(loc) in visited):
        continue

    cameFrom = loc.pop()
    steps = visited[str(cameFrom)][0] + 1
    visited[str(loc)] = (steps, cameFrom)
    if( steps > s ):
        s = steps

    # Scan around me for connections
    connections = directions[ lines[loc[0]][loc[1]] ]
    going = [0,0]
    for c in connections:
        going = [loc[0]+c[0], loc[1]+c[1]]
        
        if 0 <= going[1] < len(lines):
            if 0 <= going[0] < len(lines[y]):
                pipeSym = lines[going[0]][going[1]]
                pipe = directions[pipeSym]

                for p in pipe:
                    if going[0]+p[0] == loc[0] and going[1]+p[1] == loc[1]:
                        if( str(going) not in visited ):
                            queue.append([going[0], going[1], loc])
                    

print(s)

