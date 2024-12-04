import sys
import re

filename = sys.argv[1] if len(sys.argv) > 1 else 'test-input.dat'
f = open(filename)

pattern = "MAS"

lines = f.readlines()
dirs = []
for x in range(-1,2,2):
    for y in range(-1,2,2):
        dirs.append( (x,y) ) 

aPlacements = set()
XMASCount = 0
for y in range(len(lines)):
    line = lines[y].strip()
    for x in range(len(line)):
        for dir in dirs:
            combo = 0
            nX = x
            nY = y
            while( combo < len(pattern) and lines[nY][nX] == pattern[combo] ):
                combo += 1
                nX += dir[0]
                nY += dir[1]
                if nX < 0 or nX >= len(line) or nY < 0 or nY >= len(lines):
                    break

            if combo == len(pattern):
                aPlace = (x+dir[0], y+dir[1])
                if aPlace in aPlacements:
                    XMASCount += 1
                else:
                    aPlacements.add(aPlace)

print(XMASCount)