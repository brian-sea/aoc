with open("input", 'r') as f:
    line = f.readline()

    ages = [int(x) for x in line.split(',')]

    day = 0
    while day < 80:
        fish = 0
        numFish = len(ages)
        while fish < numFish:
            if ages[fish] == 0:
                ages[fish] = 6
                ages.append(8)
            else:
                ages[fish] -= 1
            
            fish += 1

        day += 1

    print(len(ages))