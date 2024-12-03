import sys
import re

filename = sys.argv[1] if len(sys.argv) > 1 else 'test-input.dat'
f = open(filename)

sum = 0
lines = f.readlines()
for line in lines:
    matches = re.findall(r'mul\(\d+\,\d+\)',line.strip())
    for m in matches:
        left,right = list(map(int, m[4:-1].split(',')))
        sum += left * right

print(sum)
    
