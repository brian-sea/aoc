
with open("input", 'r') as f:
    gamma = 0
    epsilon = 0
    
    numOnes = []
    count = 0
    for line in f:
        line = line.strip()
        while len(numOnes) < len(line):
            numOnes.append(0)

        for idx,digit in enumerate(line):
            if digit == '1':
                numOnes[idx] += 1

        count += 1

    power = 0
    spot = len(numOnes) - 1
    while spot >= 0:
        if numOnes[spot] >= count//2:
            gamma += pow(2, power)
        else:
            epsilon += pow(2, power)
        
        power += 1
        spot -= 1

    print(gamma*epsilon)