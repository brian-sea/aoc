f = open('inputfinal')

execLength = {
    'addx': 2,
    'noop': 1
}

checkpoints = []
cycle = 0
X = 1
for line in f:
    parts = line.strip().split(' ')
    
    cycle += execLength[parts[0]]
    if len(parts) > 1:
        X += int(parts[1])

    checkpoints.append({
        'cycle': cycle,
        'x' : X
    })

CRT = [' '] * 240
spritePosition = 0
cycle = 0
CRTWidth = 40
while len(checkpoints) > 0:

    # Time to change the placement of the sprite
    if cycle >= checkpoints[0]['cycle']:
        spritePosition = checkpoints[0]['x']
        checkpoints.pop(0)

    # Check if sprite (WHOLE SCREEN) is within one pixel
    if abs(spritePosition-cycle%CRTWidth) <= 1:
        CRT[cycle] = '#'

    cycle += 1

CRTHeight = 6
for row in range(CRTHeight):
    print(''.join(CRT[row*CRTWidth: (row+1)*CRTWidth]))