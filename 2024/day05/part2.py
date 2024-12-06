import sys
import re

filename = sys.argv[1] if len(sys.argv) > 1 else 'test-input.dat'
f = open(filename)

rules = dict()
for line in f:
    line = line.strip()
    if len(line) == 0:
        break
    
    left,right = list(map(int,line.split("|")))
    if left not in rules:
        rules[left] = set()
    rules[left].add(right)

order = dict()
middlePageSum = 0
for line in f:    
    order.clear()
    line = line.strip()
    nums = list(map( int, line.split(",")))
    for idx in range(len(nums)):
        order[nums[idx]] = idx

    valid = True
    for num in order.keys():
        if num in rules:
            for r in rules[num]:
                if r in order and order[num] > order[r]:
                    valid = False            

    if not valid:
        # Bubble Sort is good enough... 
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x] in rules and nums[y] in rules[nums[x]]:
                    if x >= y:
                        nums[x], nums[y] = nums[y],nums[x]
        middlePageSum += nums[ len(nums) // 2]
            
print(middlePageSum)

# Guess: 4144 (too low)