import sys

with open('input','r') as f:

    template = f.readline().strip()
    f.readline()

    rules = dict()
    for line in f:
        line = line.strip().split(' -> ')

        rules[line[0]] = line[1]

    step = 0
    while step < 10:
        
        newTemp = ''
        pos = 0
        while pos < len(template)-1:
            fl = template[pos]
            sl = template[pos+1]

            newTemp += fl+rules[fl+sl]
            pos += 1

        template = newTemp + template[-1]
        step += 1
    
    countElements = dict()
    for letter in template:
        if letter in countElements:
            countElements[letter] += 1
        else:
            countElements[letter] = 1

    leastElement = min(countElements.values())
    mostElement = max(countElements.values())
    print(mostElement-leastElement)