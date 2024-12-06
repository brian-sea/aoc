import sys
import re

filename = sys.argv[1] if len(sys.argv) > 1 else 'test-input.dat'
f = open(filename)

locations = []
guardDir = 0
guardLoc = None
for line in f:
    line = list(line.strip())
    
    try:
        x = line.index('^')
        guardLoc = [len(locations),x]
    except:
        pass
    
    locations.append(line)

dirs = [
    (-1,0),  # Up
    (0,1),  # Right
    (1,0), # Down
    (0,-1)  # Left
]
visited = set()
while 0<= guardLoc[0] < len(locations) and 0 <= guardLoc[1] < len(locations[0]):
    visited.add((guardLoc[0], guardLoc[1]))

    d = dirs[guardDir]
    if 0 <= guardLoc[0]+d[0] < len(locations) and 0 <= guardLoc[1]+d[1] < len(locations[0]):
        spot = locations[guardLoc[0]+d[0]][guardLoc[1]+d[1]]
        if spot != '#':
            guardLoc[0] += d[0]
            guardLoc[1] += d[1]
        else:
            guardDir = (guardDir+1) % len(dirs)
    else:
        guardLoc[0] += d[0]
        guardLoc[1] += d[1]

print(len(visited))