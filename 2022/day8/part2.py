f = open('inputfinal')

trees = list(map(str.strip, f.readlines()))
visible = []
for i in range(len(trees)):
    row = []
    for j in range(len(trees[0])):
        row.append(0)
    visible.append(row)

for row in range(1, len(trees)-1):
    for col in range(1, len(trees[i])-1):
        score = 1

        # Up
        count = 1
        spot = row-1
        while spot > 0 and ord(trees[spot][col]) < ord(trees[row][col]):
            spot -= 1
            count += 1                
        score *= count

        # Down
        count = 1
        spot = row+1
        while spot < len(trees)-1 and ord(trees[spot][col]) < ord(trees[row][col]):
            spot += 1
            count += 1
        score *= count

        # Right
        count = 1
        spot = col+1
        while spot < len(trees[0])-1 and ord(trees[row][spot]) < ord(trees[row][col]):
            spot += 1
            count += 1
        score *= count

        # Left
        count = 1
        spot = col-1
        while spot > 0 and ord(trees[row][spot]) < ord(trees[row][col]):
            spot -= 1
            count += 1                
        score *= count

        visible[row][col] = score

v = -1
for i in range(len(visible)):
    for j in range(len(visible[i])):
        if visible[i][j] > v:
            v = visible[i][j]

print(v)

# Guess: 144