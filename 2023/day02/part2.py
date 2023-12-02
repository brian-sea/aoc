import re
f = open("finalinput")

power = 0
lines = [line.strip() for line in f.readlines()]
for line in lines:

    colon = line.find(':')
    gameId = int(re.findall("\s\d+", line[:colon])[0])

    possible = True
    games = line[colon:].split(";")
   
    gems = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }
    for game in games:     
        rnds = re.findall("(\d+)\s(red|green|blue)", game)
        for rnd in rnds:
            if( gems[rnd[1]] < int(rnd[0])):
                gems[rnd[1]] = int(rnd[0])
    mul = 1
    for k in gems:
        mul *= gems[k]
    power += mul

print(power)