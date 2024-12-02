import math
import re
f = open("final-input.dat")

safe = 0
lines = f.readlines()
for line in lines:
    nums = list(map(int, re.split(r'\s+',line.strip())))

    prevNum = nums[0]
    increasing = None
    valid = True
    for idx in range(1, len(nums)):
        diff = abs(prevNum-nums[idx])
        inc = prevNum < nums[idx]
        if diff < 1 or diff > 3:
            valid = False
            break
        
        if increasing == None:
            increasing = inc
        elif increasing != inc:
            valid = False
            break

        prevNum = nums[idx]

    if valid:
        safe += 1

print(safe)