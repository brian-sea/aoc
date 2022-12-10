import sys

# Stores each location
class Location:
    def __init__(self, name):
        self.name = name
        self.exits = set()
        self.visited = False

    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self.exits)

# Map of the cave
caveMap = dict()

# We're allowed to visit one small cave twice
visit2 = None

# Counts the number of paths through a location
# location - current place in the map
# Rules:
#   (1) Small caves (lowercase) can only be visited once
#   (2) Big caves (uppercase) can be visted as many times as possible
#   (3) Exception to Rule 1: one small cave can be visited twice
def countPaths(location):
    global visit2

    # Base Case: Stop at the end    
    if location.name == 'end':
        return 1

    # Base Case: We've visited this location twice already
    if location.visited == True and visit2 != None:
        return 0

    # Mark the second visit
    if location.visited == True:
        visit2 = location

    # Mark the visit to a small cave
    if location.name.islower():
       location.visited = True

    numPaths = 0
    for exit in location.exits:
        numPaths += countPaths(caveMap[exit])
    
    # Undo our visit
    if visit2 == location:
        visit2 = None
    else:
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
    
        # 'start' is not allowed to an exit
        if caves[1] != 'start':
            caveMap[caves[0]].exits.add(caves[1])
        
        # 'start' is not allowed to be an exit
        if caves[0] != 'start':
            caveMap[caves[1]].exits.add(caves[0])
    
    print( countPaths(caveMap['start']) )