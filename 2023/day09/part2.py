import re
import datetime
from collections import defaultdict
        
f = open("finalinput")
lines = [line.strip() for line in f.readlines()]

s = 0
for line in lines:
    pattern = [ int(x) for x in re.findall("-?\d+", line) ]
    allZeros = False
    firsts = []
    
    while not allZeros:
        allZeros = True
        pos = 1

        firsts.insert(0, pattern[0])
        while pos < len(pattern):
            diff = pattern[pos] - pattern[pos-1]
            pattern[pos-1] = diff
            if diff != 0:
                allZeros = False
            pos += 1
        pattern.pop(-1)

    sumSeq = 0
    for l in firsts:
        sumSeq = l - sumSeq
    s += sumSeq

print(s)

#Answer: 1038