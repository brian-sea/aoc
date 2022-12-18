f = open('inputfinal')

def isOutside(p, bounds):
    inside = True
    for i in range(len(bounds)):
        if p[i] <= bounds[i][0] or p[i] >= bounds[i][1]:
            inside = False
    return not inside

def reachOutside(p, pockets, ash, bounds, OUT, IN):
    visited = set()
    if p in OUT:
        return True, visited
    if p in IN:
        False, visited

    lookAt = [p]
    while len(lookAt) > 0:
        look = lookAt.pop()

        if look in ash:
            continue

        if look in visited:
            continue

        if isOutside(look, bounds):
            return True, visited

        visited.add(look)    
    
        (x,y,z) = look
        lookAt.append( (x+1, y, z))
        lookAt.append( (x-1, y, z))
        lookAt.append( (x, y+1, z))
        lookAt.append( (x, y-1, z))
        lookAt.append( (x, y, z+1))
        lookAt.append( (x, y, z-1))

    return False, visited


bounds = [ [None,None], [None,None], [None,None]]
numExposed = 0
ash = set()
pockets = set()
for line in f:
    p = list(map(int, line.split(",")))
    
    numExposed += 6
    for i in range(len(p)):
        add = [-1,1]
        for a in add:
            p[i] += a
            if tuple(p) in ash:
                numExposed -= 2
            else:
                pockets.add(tuple(p))
            p[i] -= a

    p = tuple(p)
    ash.add( p )
    if p in pockets:
        pockets.remove( p )

    for i in range(len(bounds)):
        if bounds[i][0] == None or p[i] < bounds[i][0]:
            bounds[i][0] = p[i]
        if bounds[i][1] == None or p[i] > bounds[i][1]:
            bounds[i][1] = p[i]

IN = set()
OUT = set()
for p in pockets:
    out, v = reachOutside(p, pockets, ash, bounds, OUT, IN)
    if not out:   
        IN.update(v)
    else:
        OUT.update(v)

for p in IN:
    p = list(p)
    for i in range(len(p)):
        add = [-1,1]
        for a in add:
            p[i] += a
            if tuple(p) in ash:
                numExposed -= 1
            p[i] -= a

print(numExposed)

# GUESS: 264 (too low)
# GUESS: 4300 (too high)
# GUESS: 2927 (too high)