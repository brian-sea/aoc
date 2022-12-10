f = open('inputfinal')
lines = f.readlines()

root = {
    "name": '/',
    'type': 'd',
    'children': {},
    'parent': None,
    'size' : 0
}
location = root

spot = 0
while spot < len(lines):
    line = lines[spot].strip()

    if line[0] == '$':
        commands = line.split(' ')
        if commands[1] == 'cd':
            d = commands[-1]
            if d == '..':
                location = location['parent']
            elif d == '/':
                location = root
            else:
                location = location['children'][d]
    else:
        parts = line.split(' ')
        s = 0
        if parts[0] == 'dir' and parts[-1] not in location['children']:
            location['children'][parts[-1]] = {
                'name': parts[-1],
                'type': 'd',
                'children': {},
                'parent': location,
                'size': 0
            }
        else:
            s += int(parts[0])

        p = location
        while p != None:
            p['size'] += s
            p = p['parent']
            
    spot += 1

parents = [root]
s = 0
while len(parents) > 0:
    loc = parents.pop()
    if loc['size'] <= 100000:
        s += loc['size']
    for c in loc['children']:
        parents.append(loc['children'][c])

print(s)

# Guess: 1005501