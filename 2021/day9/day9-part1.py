import sys 

with open("input", 'r') as f:
    depths = []
    for line in f:
        line = line.strip()
        depth = [int(x) for x in line]
        depths.append(depth)

    sum = 0
    for y in range(len(depths)):
        for x in range(len(depths[y])):

            countIt = True
            dirs = [
                (0,-1), (0,1), (1,0), (-1,0)
            ]
            for i, j in dirs:
                if x+j >= 0 and x+j < len(depths[y]):
                    if y+i >=0 and y+i < len(depths):
                        if depths[y+i][x+j] <= depths[y][x]:
                            countIt = False

            if countIt == True:
                sum += depths[y][x]+1
    print(sum)