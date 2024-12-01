import re
from collections import defaultdict

f = open("final-input.dat")

left = []
right = defaultdict(int)
lines = f.readlines()
for line in lines:
    nums = list(map(int, re.split(r'\s+',line.strip())))
    left.append(nums[0])
    right[ nums[1] ] += 1

sum = 0
for i in range(0, len(left)):
    sum += left[i] * right[ left[i] ]
print(sum)