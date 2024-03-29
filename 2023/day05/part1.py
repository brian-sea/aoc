import re
import datetime

f = open("finalinput")

lines = [line.strip() for line in f.readlines()]
s = 0

start = datetime.datetime.now()
seeds = [int(x) for x in re.findall("\d+", lines[0])]

maps = [
    list(), # seed-to-soil
    list(), # soil-to-fertilizer
    list(), # fertilizer-to-water
    list(), # water-to-light
    list(), # light-to-temp
    list(), # temp-to-humidity
    list() # humidity-to-location
]

onMap = 0
MAP = maps[0]
lineCount = 3
while lineCount < len(lines):
    if( len(lines[lineCount]) == 0 ):
        onMap += 1
        lineCount += 2
        MAP = maps[onMap]
    
    nums = [int(x) for x in re.findall("\d+", lines[lineCount])]
    
    [d,s,r] = nums
    MAP.append([d,s,r])

    lineCount += 1

minLoc = float('inf')
for s in seeds:
    loc = s
    for m in maps:
        for l in m:
            if l[1] <= loc <= l[1]+l[2]:
                loc = l[0]+(loc-l[1])
                break
        
    if loc < minLoc:
        minLoc = loc

end = datetime.datetime.now()

print(end - start)
print(minLoc)

