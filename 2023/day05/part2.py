# Brute Force... ewww; find a better way

import re
import datetime

f = open("finalinput")

lines = [line.strip() for line in f.readlines()]

#start = datetime.datetime.now()
seedRanges = [int(x) for x in re.findall("\d+", lines[0])]

sIdx = 0
seeds = []
while sIdx < len(seedRanges):
    # Intervals -- [include, exclude)
    seeds.append([seedRanges[sIdx], seedRanges[sIdx] + seedRanges[sIdx+1]])
    sIdx += 2

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
    
    NM = [ [s[0], s[1]] ]
    for m in maps:
        
        # Seeds adjusted for next map
        AdjustedSeeds = []
        for r in m:

            # Storage of unadjusted elements
            nextMap = []
            for nm in NM:
                before = None
                after = None
                overlap = None
            
                adjustInterval = [nm[0], nm[1]]
    
                # before - untouched
                if adjustInterval[0] < r[1]:
                    before = [ adjustInterval[0], min(adjustInterval[1], r[1])]
                    adjustInterval[0] = r[1]
                    nextMap.append(before)
                
                # after - untouched
                if adjustInterval[1] > r[1] + r[2]:
                    after = [ max(adjustInterval[0], r[1]+r[2]), adjustInterval[1] ] 
                    adjustInterval[1] = r[1]+r[2]
                    nextMap.append(after)
                
                # overlap - adjusted
                if( adjustInterval[1] - adjustInterval[0] > 0):
                    adjustedStart = r[0] + (adjustInterval[0]-r[1])
                    adjustedEnd = r[0] + (adjustInterval[1]-r[1]) 
                    overlap = [ adjustedStart, adjustedEnd ]
                    AdjustedSeeds.append(overlap)
                
            NM = nextMap

        # Add adjusted seeds for the next map
        for a in AdjustedSeeds:
            NM.append(a)  

    # Check current seed interval for min
    for s in NM:
        if s[0] < minLoc:
            minLoc = s[0]

#end = datetime.datetime.now()
#print(end - start)

print(minLoc)

# Answer: 52210644
