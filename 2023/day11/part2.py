import re
import datetime
from collections import defaultdict
        
f = open("finalinput")
lines = [line.strip() for line in f.readlines()]

galaxyLocations = []

galColumns = {}
colInterval = [float('inf'), -1]
row = 0
for line in lines:
    locations = re.finditer("#", line)
    empty = True
    for loc in locations:
        empty = False

        col = loc.span()[0]
        galaxyLocations.append([row, col])    
    
        if col not in galColumns:
            galColumns[col] = []
        if col < colInterval[0]:
            colInterval[0] = col
        if col > colInterval[1]:
            colInterval[1] = col
        galColumns[col].append(len(galaxyLocations) - 1)


    # No galaxies in the row
    if empty:
        row += 999999

    row += 1

# Adjust galaxy columns
colAdd = 0
for x in range(colInterval[0], colInterval[1] + 1):
    if( x not in galColumns ):
        colAdd += 999999
    else:
        for idx in galColumns[x]:
            galaxyLocations[idx][1] += colAdd

s = 0
for i in range(len(galaxyLocations)):
    for j in range(i+1, len(galaxyLocations)):
        dist = abs(galaxyLocations[i][0]-galaxyLocations[j][0])
        dist += abs(galaxyLocations[i][1]-galaxyLocations[j][1])
        s += dist

print(s)

# Answer: 560822911938