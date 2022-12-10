
with open("input", 'r') as f:
    horizontal = 0
    depth = 0
    aim = 0

    for line in f:
        parts = line.split(' ')

        num = int(parts[1])
        if( parts[0] == 'forward' ):
            horizontal += num
            depth += aim*num
        else:
            if parts[0] == 'up':
                num *= -1
            aim += num
    print( horizontal*depth)