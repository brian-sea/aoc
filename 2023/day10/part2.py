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
            start = (y,x)
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
visited = { }

# Add a fake start (removed later)
visited["start"] = (-1,"start")
start = (start, "start")

queue = [start]         
s = 0
while len(queue) > 0:

    # Handle next element
    loc = queue.pop(0)
    cameFrom = loc[-1]
    loc = loc[0] 
    
    if(loc in visited):
        continue

    steps = visited[cameFrom][0] + 1
    visited[loc] = (steps, cameFrom)
    if( steps > s ):
        s = steps


    # Scan around me for connections
    connections = directions[ lines[loc[0]][loc[1]] ]
    for c in connections:
        going = (loc[0]+c[0], loc[1]+c[1])

        if 0 <= going[0] < len(lines):
            if 0 <= going[1] < len(lines[y]):
                pipeSym = lines[going[0]][going[1]]
                pipe = directions[pipeSym]

                for p in pipe:
                    if going[0]+p[0] == loc[0] and going[1]+p[1] == loc[1]:
                        if( going not in visited ):
                            queue.append(( going, loc ))
del visited['start']


# Sort by row then column
cycle = list(visited.keys())
cycle = sorted(cycle, key=lambda k: k[0]*len(lines[0])+k[1])

area = 0
row = -1
interval = [-1, -1]
inside = False
up = False

pos = 0
while pos < len(cycle):

    # Find interval on the new row    
    if( cycle[pos][0] != row ):
        row = cycle[pos][0]
        inside = False
        up = False

        interval[0] = cycle[pos][1]
        while pos < len(cycle):
            if( cycle[pos][0] != row):
                interval[1] = cycle[pos-1][1]
                pos -= 1
                break
            pos += 1        

    if pos >= len(cycle):
        interval[1] = cycle[-1][1]
    
    # Horizontal line test for inside/outside
    # Moving Left to Right
    # Allow riding of pipes (need up/down direction)
    # 
    # Another Option: Reduce scale to 0.5 and flood fill
    for x in range(interval[0], interval[1]+1):
        # Count errant pipes inside the loop
        if (row,x) not in visited and inside:
            area += 1
        elif (row,x) in visited:
            if lines[row][x] == "|":    # Always intersects   
                inside = not inside     
            elif lines[row][x] == 'L':  # Going Down
                up = False              
            elif lines[row][x] == 'F':  # Going Up
                up = True               
            elif lines[row][x] == '7':  # Going Down
                if not up:              # Was going down, so intersect
                    inside = not inside
                up = False
            elif lines[row][x] == 'J':  # Going Down
                if up:                  # Was going up, so intersect
                    inside = not inside
                up = False  
    pos += 1

print(s)    
print(area)

# Answer: 493
