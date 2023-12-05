import re
import datetime
import sys

f = open("finalinput")

lines = [line.strip() for line in f.readlines()]
s = 0

#start = datetime.datetime.now()
seedRanges = [int(x) for x in re.findall("\d+", lines[0])]

sIdx = 0
seeds = []
while sIdx < len(seedRanges):
    seeds.append([seedRanges[sIdx], seedRanges[sIdx] + seedRanges[sIdx+1]])
    sIdx += 2

maps = [
    list(), # seed-to-soil
    list(), # soil-to-fertilizer
    list(), # fertilizer-to-water
    list(), # water-to-light
    list(), # light-to-temp
    list(), # temp-to-humidity
    list()  # humidity-to-location
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
    MAP.append([s,d,r])

    lineCount += 1

maps = maps[::-1]

location = 0
while True:
    
    loc = location
    for m in maps:
        for l in m:
            if l[1] <= loc <= l[1]+l[2]:
                loc = l[0]+(loc-l[1])
                break   

    # Check Seeds
    for l in seeds:
        if l[0] <= loc <= l[1]:
            print(location)
            sys.exit(0)

    location += 1

#endTime = datetime.datetime.now()

#print(end - start)

# Guess: 52210645 (too high)
# Answer: 52210644