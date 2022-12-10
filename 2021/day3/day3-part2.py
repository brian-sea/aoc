
with open("input", 'r') as f:
    O2List = []
    CO2List = []

    numSpots = 0
    for line in f:
        line = line.strip()
        
        numSpots = max(numSpots, len(line))
        O2List.append(line)
        CO2List.append(line)

    spot = 0
    while spot < numSpots:

        numOnesO2 = 0
        numOnesCO2 = 0
        for digit in O2List:
            if digit[spot] == '1':
                numOnesO2 += 1
            else:
                numOnesO2 -= 1

        for digit in CO2List:
            if digit[spot] == '1':
                numOnesCO2 += 1
            else:
                numOnesCO2 -= 1


        filterO2 = '1'
        filterCO2 = '0'
        if numOnesO2 >= 0:
            filterO2 = '0'

        if numOnesCO2 >= 0:
            filterCO2 = '1'


        fspot = 0
        while len(O2List) > 1 and fspot < len(O2List):
            if O2List[fspot][spot] == filterO2:
                O2List.pop(fspot)
                fspot -= 1

            fspot += 1

        fspot = 0
        while len(CO2List) > 1 and fspot < len(CO2List):
            if CO2List[fspot][spot] == filterCO2:
                CO2List.pop(fspot)
                fspot -= 1
            fspot += 1

        spot += 1

    O2 = 0
    CO2 = 0
    power = 0
    spot = numSpots - 1
    while spot >= 0:
        if O2List[0][spot] == '1':
            O2 += pow(2, power)
        if CO2List[0][spot] == '1':
            CO2 += pow(2, power)
        
        power += 1
        spot -= 1
    print(O2*CO2)