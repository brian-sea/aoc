f = open('inputfinal')
grid = list(map(str.strip, f.readlines()))

startLocations = []
elocation = None
maxPathSize = len(grid)*len(grid[0]) + 1
for ridx, row in enumerate(grid):
    for cidx, col in enumerate(row):
        if col == 'S':
            grid[ridx] = grid[ridx].replace('S', 'a')
        elif col == 'E':
            grid[ridx] = grid[ridx].replace('E', 'z')
            elocation = (ridx, cidx)
        
        if grid[ridx][cidx] == 'a':
            startLocations.append((ridx,cidx))

pathSizes = {}
minPath = maxPathSize
minLoc = None
for location in startLocations:

    pathSizes.clear()
    pathSizes[location] = 0
    VISITED = {location:0}
    
    search = set()
    search.add(location)
    while location != None and location != elocation:
        search.remove(location)
        looks = [
            (location[0]-1, location[1]),
            (location[0]+1, location[1]),
            (location[0], location[1]-1),
            (location[0], location[1]+1)
        ]

        for look in looks:
            if 0 <= look[0] < len(grid) and 0 <= look[1] < len(grid[look[0]]):
                stepdiff = ord(grid[look[0]][look[1]]) - ord(grid[location[0]][location[1]])
                
                if look not in VISITED and stepdiff <= 1:
                    search.add(look)    
                    
                    pSize = pathSizes[look] if look in pathSizes else maxPathSize
                    if pathSizes[location]+1 < pSize:
                        pathSizes[look] = pathSizes[location]+1
        
        minLocation = None
        for s in search:
            if minLocation == None or pathSizes[s] < pathSizes[minLocation]:
                minLocation = s

        location = minLocation
        if location != None:
            VISITED[location] = pathSizes[location]

    if elocation in VISITED and VISITED[elocation] < minPath:
        minLoc = elocation
        minPath = VISITED[elocation]

print(minPath)