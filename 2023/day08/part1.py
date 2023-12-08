import re
import datetime
from collections import defaultdict
        

network = {}

f = open("finalinput")
lines = [line.strip() for line in f.readlines()]

directions = lines.pop(0)
lines.pop(0)
for line in lines:
    node,left,right = re.findall("[A-Z]{3}", line)
    network[node] = {"L":left, "R":right}

steps = 0
strPos = 0
location = "AAA"
while location != "ZZZ":
    location = network[location][directions[strPos]]

    steps += 1
    strPos = (strPos+1)%len(directions)

print(steps)
