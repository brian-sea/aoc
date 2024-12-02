import math
import re
f = open("final-input.dat")

def valid(nums):
    prevNum = nums[0]
    increasing = None
    valid = True
    for idx in range(1, len(nums)):
        diff = abs(prevNum-nums[idx])
        inc = prevNum < nums[idx]
        if diff < 1 or diff > 3:
            return False
        
        if increasing == None:
            increasing = inc
        elif increasing != inc:
            return False

        prevNum = nums[idx]
    return True


safe = 0
lines = f.readlines()
for line in lines:
    nums = list(map(int, re.split(r'\s+',line.strip())))
    for idx in range(len(nums)):
        if valid(nums[:idx] + nums[idx+1:]):
            safe += 1
            break
print(safe)
