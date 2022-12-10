import sys 

with open("input", 'r') as f:
    line = f.readline()

    ages = [int(x) for x in line.split(',')]

    intervals = [0,0,0,0,0,0,0,0,0]
    for age in ages:
        intervals[age] += 1

    day = 0
    while day < 256:
        birth = intervals.pop(0)
        intervals.append(0)

        intervals[6] += birth
        intervals[8] += birth

        day += 1

    sum = 0
    for interval in intervals:
        sum += interval
    print( sum)