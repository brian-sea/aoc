import sys
import re
import datetime
from math import gcd
from collections import defaultdict
        

f = open("finalinput")
lines = [line.strip() for line in f.readlines()]

directions = lines.pop(0)
lines.pop(0)

network = {}
paths = []
for line in lines:
    node,left,right = re.findall("[A-Z0-9]{3}", line)
    network[node] = {"L":left, "R":right}

    if node[-1] == 'A':
        paths.append( node )



steps = {}       # Keep track of steps to end node
strPos = 0
step = 0
while len(paths) != len(steps):
    for idx,path in enumerate(paths):
        
        # Move Forward
        curLoc = network[ path ][ directions[strPos] ]
        paths[idx] = curLoc

        # Save the timestep of the end node
        if curLoc[-1] == 'Z':            
            steps[idx] = step + 1

    step += 1    
    strPos = (strPos+1)%len(directions)


# LCM - run the cycles until there's a common timestep
mult = 1
for s in steps:
    mult = mult * steps[s] // gcd(steps[s],mult)
print(mult)

# Guess: 16555262546256037897470293 (too high)
# Guess: 21883 (too low)
# Answer: 10151663816849