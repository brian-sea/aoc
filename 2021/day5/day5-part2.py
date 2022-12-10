import math

map = dict()
with open("input", 'r') as f:
    for line in f:
        coords = line.strip().split(' ')
        start = [int(x) for x in coords[0].split(',')]
        end = [int(x) for x in coords[2].split(',')]

        # Get unit direction of the line
        dx = ((end[0]-start[0])>0) - ((end[0]-start[0])<0)
        dy = ((end[1]-start[1])>0) - ((end[1]-start[1])<0)

        px = start[0]
        py = start[1]
        while px != end[0] or py != end[1]:
            if (px,py) in map:
                map[(px,py)] += 1
            else:
                map[(px,py)] = 1

            px += dx
            py += dy

        # Add End Point
        if (px,py) in map:
            map[(px,py)] += 1
        else:
            map[(px,py)] = 1


count = 0
for key, val in map.items():
    if val >= 2:
        count += 1

print(count)