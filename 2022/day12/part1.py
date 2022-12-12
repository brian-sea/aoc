f = open('inputfinal')
grid = list(map(str.strip, f.readlines()))

pathSizes = {}
location = None
elocation = None
maxPathSize = len(grid)*len(grid[0]) + 1
for ridx, row in enumerate(grid):
    for cidx, col in enumerate(row):
        pathSizes[(ridx,cidx)] = maxPathSize
        if col == 'S':
            location = (ridx, cidx)
            grid[ridx] = grid[ridx].replace('S', 'a')
            pathSizes[(ridx,cidx)] = 0
        elif col == 'E':
            grid[ridx] = grid[ridx].replace('E', 'z')
            elocation = (ridx, cidx)

VISITED = {location:0}
search = set()
search.add(location)
while location != elocation:
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
                if pathSizes[location]+1 < pathSizes[look]:
                    pathSizes[look] = pathSizes[location]+1
    
    minLocation = None
    for s in search:
        if minLocation == None or pathSizes[s] < pathSizes[minLocation]:
            minLocation = s

    location = minLocation
    VISITED[location] = pathSizes[location]

print(VISITED[elocation])

# Guess: 521 (too high)
# Guess: 449 (too low)