import re
import math
f = open('inputfinal')

floorY = -1
rocks = set()
for line in f:
    points = list(re.findall("(\d+)\,(\d+)", line))
    
    start = None
    for point in points:
        # If the point isn't the starting location, then figure out direction
        point = tuple(map(int, point))
        if start == None:
            start = point    
        else:
            dx = 0 if point[0] - start[0] == 0 else int(math.copysign(1, point[0] - start[0]))
            dy = 0 if point[1] - start[1] == 0 else int(math.copysign(1, point[1] - start[1]))

        # Add Rocks to our map and find the floor
        rocks.add(start)
        floorY = max(floorY, start[1])
        while start != point:
            start = (start[0]+dx, start[1]+dy)
            rocks.add(start)
            floorY = max(floorY, start[1])

source = (500,0)
sandMovement = [(0,1), (-1,1), (1,1)]

atRest = 0
endSimulation = False
unitsAtRest = 0
while not endSimulation:
    sand = source

    # Move the sand until settling
    dirSpot = 0
    while dirSpot < len(sandMovement):
        dir = sandMovement[dirSpot]
        loc = (sand[0]+dir[0], sand[1]+dir[1])
        if loc not in rocks:
            sand = loc
            # Sand moved, so start over
            dirSpot = -1

        # Simulate the floor
        if sand[1] > floorY:
            endSimulation = True
            break
        dirSpot += 1
    
    # Sand settled; it's now a rock
    rocks.add(sand)
    atRest += 1

print(atRest - 1)