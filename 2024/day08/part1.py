import sys
import re
from collections import defaultdict

filename = sys.argv[1] if len(sys.argv) > 1 else 'test-input.dat'
f = open(filename)


locations = dict()

width = 0
y = 0
for line in f:
    line = line.strip()
    width = len(line)
    for x in range(width):
        if line[x] != '.':
            if line[x] not in locations:
                locations[line[x]] = []
            locations[line[x]].append( (y,x) )
    y += 1

antiNodes = set()
for attena,loc in locations.items():

    for first in range(len(loc)):
        first = loc[first]

        for sec in range(1,len(loc)):
            sec = loc[sec]

            if first == sec:
                continue

            ySlope = abs(first[0]-sec[0])
            xSlope = abs(first[1]-sec[1])

            tempAntiNodes = [ [0,0],[0,0] ]
            if first[0] < sec[0]:
                tempAntiNodes[0][0] = -ySlope
                tempAntiNodes[1][0] = ySlope
            else:
                tempAntiNodes[0][0] = ySlope
                tempAntiNodes[1][0] = -ySlope

            if first[1] < sec[1]:
                tempAntiNodes[0][1] = -xSlope
                tempAntiNodes[1][1] = xSlope
            else:
                tempAntiNodes[0][1] = xSlope
                tempAntiNodes[1][1] = -xSlope


            tf = list(first)
            ts = list(sec)
            
            tf[0] += tempAntiNodes[0][0]
            tf[1] += tempAntiNodes[0][1]
            if 0 <= tf[0] < y and 0 <= tf[1] < width:
                antiNodes.add((tf[0], tf[1]))

            ts[0] += tempAntiNodes[1][0]
            ts[1] += tempAntiNodes[1][1]
            if 0 <= ts[0] < y and 0 <= ts[1] < width:
                antiNodes.add((ts[0], ts[1]))

print(len(antiNodes))