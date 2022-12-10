import sys 

with open("input", 'r') as f:
    line = f.readline()
    positions = [int(x) for x in line.split(',')]

    fuelCost = []
    for pos in positions:
        spot = len(fuelCost)
        while spot <= pos:
            fuelCost.append(0)
            spot += 1

        toMoveHere = 0
        spot = 0
        while spot < len(fuelCost):
            # Movement cost is one per space
            fuelCost[spot] = fuelCost[spot] + abs(pos-spot)
            toMoveHere += abs(pos-spot)
            spot += 1
        
        if fuelCost[pos] == 0:
            fuelCost[pos] += toMoveHere

    min = None
    for val in fuelCost:
        if min == None or val < min:
            min = val

    print(min)