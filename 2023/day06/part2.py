import re
import datetime
import sys

f = open("finalinput")

lines = [line.strip() for line in f.readlines()]
time = int(''.join(re.findall("\d+", lines[0])))
distance = int(''.join(re.findall("\d+", lines[1])))

timeStart = datetime.datetime.now()

error = 1

hold = [1, distance-1]
while hold[0] < hold[1]:
    if( hold[0] * (time-hold[0]) > distance):
        while hold[0] * (time-hold[0]) > distance:
            hold[0] -= 1

        hold[0] += 1
        break
    hold[0] *= 2

while hold[1] > hold[0]:
    if( hold[1] * (time-hold[1]) > distance):
        while hold[1] * (time-hold[1]) > distance:
            hold[1] += 1
        break
    hold[1] //= 2


timeEnd = datetime.datetime.now()
print(hold[1] - hold[0])
print(timeEnd-timeStart)


# Answer: 39594072
# Time: 2.59s