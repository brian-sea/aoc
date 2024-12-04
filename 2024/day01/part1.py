import re
f = open("final-input.dat")

left = []
right = []
lines = f.readlines()
for line in lines:
    nums = list(map(int, re.split(r'\s+',line.strip())))
    left.append(nums[0])
    right.append(nums[1])    
left.sort()
right.sort()

sum = 0
for i in range(0, len(left)):
    sum += abs(left[i]-right[i])
print(sum)