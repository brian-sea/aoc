
with open("input", 'r') as f:
    horizontal = 0
    depth = 0
    for line in f:
        parts = line.split(' ')

        num = int(parts[1])
        if( parts[0] == 'forward' ):
            horizontal += num
        else:
            if parts[0] == 'up':
                num *= -1
            depth += num
    print( horizontal*depth)