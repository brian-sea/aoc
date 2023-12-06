import re
import datetime

f = open("finalinput")

lines = [line.strip() for line in f.readlines()]
time = [ int(x) for x in re.findall("\d+", lines[0])]
distance = [ int(x) for x in re.findall("\d+", lines[1])]

error = 1
idx = 0
while idx < len(time):
    t = time[idx]

    wins = [0, distance[idx]]
    hold = 1
    while hold <= t // 2:
        if( hold * (t-hold) > distance[idx]):
            wins[0] = hold
            break
        hold += 1

    hold = distance[idx] -1
    while hold >= t // 2:
        if( hold * (t-hold) > distance[idx]):
            wins[1] = hold
            break
        hold -= 1

    error *= wins[1]-wins[0] + 1
    idx += 1

print(error)


