import sys 

# Valid Directions 
dirs = [
    (0,-1), (0,1), (1,0), (-1,0)
]

# Flood Fill to find the size of the basin
# map - current cave map
# lp - current location (y,x)
def measureBasin(map, lp):

    # Unpack the tuple for ease of coding
    y,x = lp

    # Base Case: Outside of map
    if y < 0 or y >= len(map):
        return 0

    # Base Case: Outside the map
    if x < 0 or x >= len(map[y]):
        return 0
    
    # Base Case: Hit a ridge
    if map[y][x] == 9:
        return 0 

    # Base Case: Hit a spot already checked
    if map[y][x] < 0:
        return 0

    # Mark spot as checked (make it negative)
    map[y][x] = -1

    # Start our flood fill
    size = 0
    for j,i in dirs:
        size += measureBasin(map, (y+j, x+i))

    # Our size is ourselves plus those around us
    return size+1


with open("input", 'r') as f:
    depths = []
    for line in f:
        line = line.strip()
        depth = [int(x) for x in line]
        depths.append(depth)

    # Find the low points
    lowPoints = []
    for y in range(len(depths)):
        for x in range(len(depths[y])):
            countIt = True
            for i, j in dirs:
                if x+j >= 0 and x+j < len(depths[y]):
                    if y+i >=0 and y+i < len(depths):
                        if depths[y+i][x+j] <= depths[y][x]:
                            countIt = False

            if countIt == True:
                lowPoints.append( (y,x) )
    
    # From each low point, flood fill to find the basin size
    largest3Basins = []
    for lp in lowPoints:
        size = measureBasin(depths, lp)

        # Only allow the largest three basins
        if len(largest3Basins) == 3:
            m = largest3Basins.index(min(largest3Basins))
            
            if largest3Basins[m] < size:
                largest3Basins[m] = size
        else:
            largest3Basins.append(size)

    mult = 1
    for s in largest3Basins:
        mult *= s

    print( mult )
