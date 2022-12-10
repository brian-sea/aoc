import sys 

'''
    Propogate a flash
'''
def flash(map, y, x ):

    # Base Case: The creature has already flashed
    if map[y][x] == -1:
        return 0

    # Mark the creature flashed    
    map[y][x] = -1
    flashes = 1

    # All adjacent creatures gain energy and may flash if they
    # haven't yet.  Ignore creatures that have flashed already
    for s in range(y-1, y+2):
        for t in range(x-1, x+2):
            if s >= 0 and s < len(map):
                if t >=0 and t < len(map[s]):
                    if map[s][t] != -1:
                        map[s][t] += 1
                        if map[s][t] > 9:
                            flashes += flash(map, s,t)
    return flashes

'''
    Debug: Print the map to the screen
'''
def printMap(map):
    for row in map:
        for col in row:
            print(col, end='')
        print()


map = []
with open("input", 'r') as f:
    for line in f:
        line = line.strip()
        row = [int(x) for x in line]
        map.append(row)
 
    maxSteps = 100
    step = 0

    numFlashes = 0
    while step < maxSteps:
        for y in range(len(map)):
            for x in range(len(map[y])):

                # If the creature hasn't flashed this turn
                # increase the energy and flash it if over nine
                if map[y][x] != -1:
                    map[y][x] += 1
                    if map[y][x] > 9:
                        numFlashes += flash(map, y, x)

        # Reset creatures that have flashed
        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[y][x] < 0:
                    map[y][x] = 0
        step += 1

    print(numFlashes)