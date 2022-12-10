f = open('inputfinal')

head = [0,0]
tail = (0,0)
locations = {(0,0):0}

# Map directions
directions = {
    ord("L") : "-1,0",
    ord("R") : "1,0",
    ord("U") : "0,1",
    ord("D") : "0,-1"
}

for line in f:
    dir, amt = line.split(' ')
    amt = int(amt)

    dx, dy = map(int, dir.translate(directions).split(","))

    for i in range(amt):
        head = [ x + y for x,y in zip(head, [dx, dy])]

        move = list(tail)
        for j in range(2):
            if abs(head[j]-move[j]) == 2:
                move[j] = (head[j]+move[j])//2
                move[(j+1)%2] = head[(j+1)%2]
        tail = tuple(move)
        locations[tail] = 0

print(len(locations))