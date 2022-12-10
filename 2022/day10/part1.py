f = open('inputfinal')

execLength = {
    'addx': 2,
    'noop': 1
}
checkpoints = [ 20, 60, 100, 140, 180, 220 ]

X = 1
cycle = 0
s = 0
for line in f:
    parts = line.strip().split(' ')
    
    cycle += execLength[parts[0]]
    if len(checkpoints) > 0 and cycle >= checkpoints[0]:
        s += X * checkpoints[0]
        checkpoints.pop(0)

    if len(parts) > 1:
        X += int(parts[1])

print(s)