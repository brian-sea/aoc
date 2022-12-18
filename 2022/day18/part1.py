f = open('inputfinal')

numExposed = 0
ash = set()
for line in f:
    p = list(map(int, line.split(",")))
    ash.add( tuple(p) )

    numExposed += 6
    for i in range(len(p)):
        add = [-1,1]
        for a in add:
            p[i] += a
            if tuple(p) in ash:
                numExposed -= 2
            p[i] -= a

print(numExposed)