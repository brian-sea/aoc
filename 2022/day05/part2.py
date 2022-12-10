import re 

f = open('inputfinal')
stacks = []
for line in f:
    if len(line.strip()) == 0:
        break

    crates = [line[i:i+3] for i in range(0, len(line), 4)]
    spot = 0
    while spot < len(crates):
        if crates[spot][0] == '[':
            while len(stacks) <= spot:
                stacks.append([])
            stacks[spot].insert(0, crates[spot][1])
        spot += 1
        
for line in f:
    line = line.strip()
    m,f,t = map(int, re.findall('\d+', line))
    
    move = []
    for i in range(m):
        move.append(stacks[f-1].pop())
    while len(move) > 0:
        stacks[t-1].append(move.pop())

for stack in stacks:
    print(stack.pop(), end='')