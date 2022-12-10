import sys

# Stores each location
class Location:
    def __init__(self, name):
        self.name = name
        self.exits = set()
        self.visited = False

    def __repr__(self):
        return str(self.outs)

# Map of the cave
caveMap = dict()

# Counts the number of paths through a location
# location - current place in the map
# Rules:
#   (1) Small caves (lowercase) can only be visited once
#   (2) Big caves (uppercase) can be visted as many times as possible
def countPaths(location):

    # Base Case: Stop at the end    
    if location.name == 'end':
        return 1
    
    # Base Case: We've visited this location already
    if location.visited == True:
        return 0

    # Mark the visit to a small cave
    if location.name.islower():
       location.visited = True

    numPaths = 0
    for exit in location.exits:
        numPaths += countPaths(caveMap[exit])
    
    # Undo our visit
    location.visited = False

    return numPaths

with open('input','r') as f:
    for line in f:
        line = line.strip()
        caves = line.split('-')

        # Build map of the cave
        for cave in caves:
            if cave not in caveMap:
                caveMap[cave] = Location(cave)
        
        caveMap[caves[0]].exits.add(caves[1])
        caveMap[caves[1]].exits.add(caves[0])

    print( countPaths(caveMap['start']) )