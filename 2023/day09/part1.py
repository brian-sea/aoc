import re
import datetime
from collections import defaultdict
        
f = open("finalinput")
lines = [line.strip() for line in f.readlines()]

s = 0
for line in lines:
    pattern = [ int(x) for x in re.findall("-?\d+", line) ]
    allZeros = False
    lasts = []
    
    while not allZeros:
        allZeros = True
        pos = 1
        while pos < len(pattern):
            diff = pattern[pos] - pattern[pos-1]
            pattern[pos-1] = diff
            if diff != 0:
                allZeros = False
            pos += 1

        lasts.insert(0, pattern[-1])
        pattern.pop(-1)

    s += sum(lasts)

print(s)

#Answer: 1993300041