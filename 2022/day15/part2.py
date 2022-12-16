import re
import sys

f = open('inputfinal')

# Switch to intervals... *sigh*
noBeacons = {}
minY = 0
maxY = 4000000
mult = 4000000

for line in f:
    (sensor, beacon) = [ tuple(map(int,p)) for p in re.findall(r"(\d+)\, y=(\d+)", line) ]

    dx = abs(sensor[0] - beacon[0])
    dy = abs(sensor[1] - beacon[1])
    totalDistance = dx + dy

    for yCheck in range(-totalDistance, totalDistance+1):
        
        actualY = sensor[1] + yCheck
        if actualY not in noBeacons:
            noBeacons[actualY] = []

        wingspan = totalDistance - abs(yCheck)
        minX = sensor[0]-wingspan
        maxX = sensor[0]+wingspan
        
        # Interval of X's on Y line
        noBeacons[actualY].append((minX, maxX))


for y in range(maxY+1):
    
    intervals = noBeacons[y]
    intervals.sort() # Sorts ordered pairs by first coordinate

    openX = intervals[0][0]
    for minX, maxX in intervals:
        if openX < minX:
            print(openX, y, (minX, maxX), end=' ')
            print(openX*mult+y)
            break
        
        openX = max(openX, maxX+1)
        if openX > maxY:
            break

# Guess: 3383812 (too low)