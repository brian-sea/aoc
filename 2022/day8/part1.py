f = open('inputfinal')

trees = list(map(str.strip, f.readlines()))
visible = []
for i in range(len(trees)):
    row = []
    for j in range(len(trees[0])):
        row.append(0)
    visible.append(row)

for i in range(len(trees)):
    height = -1
    spot = 0
    while spot < len(trees[i]):
        if ord(trees[i][spot]) > height:
            visible[i][spot] += 1
            height = max(height, ord(trees[i][spot]))
        spot += 1

    height = -1
    spot = len(trees[i])-1
    while spot >= 0:
        if ord(trees[i][spot]) > height:
            visible[i][spot] += 1
            height = max(height, ord(trees[i][spot]))
        spot -= 1
    
for i in range(len(trees[0])):
    height = -1
    spot = 0
    while spot < len(trees):
        if ord(trees[spot][i]) > height:
            visible[spot][i] += 1
            height = max( height, ord(trees[spot][i]))
        spot += 1
            
    height = -1
    spot = len(trees)-1
    while spot >= 0:
        if ord(trees[spot][i]) > height:
            visible[spot][i] += 1
            height = max(height, ord(trees[spot][i]))
        spot -= 1

v = 0
for i in range(len(visible)):
    for j in range(len(visible[i])):
        if visible[i][j] >= 1:
            v += 1

print(v)