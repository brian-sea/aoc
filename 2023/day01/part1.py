import re
f = open("finalinput")

s = 0
lines = f.readlines()
for line in lines:
    first = None
    last = None

    idx = 0
    while idx < len(line):
        if( '0' <= line[idx] <= '9'):
            first = line[idx]
            break
        idx += 1

    idx = len(line) - 1
    while idx >= 0:
        if( '0' <= line[idx] <= '9'):
            last = line[idx]
            break
        idx -= 1

    s += int( first + last )

print(s)