import re
f = open("finalinput")

possibleGames = set()
lines = [line.strip() for line in f.readlines()]
for line in lines:
    colon = line.find(':')
    gameId = int(re.findall("\s\d+", line[:colon])[0])

    possible = True
    games = line[colon:].split(";")
    for game in games:
        gems = {
            'red' : 12,
            'green' : 13,
            'blue' : 14
        }

        rnds = re.findall("(\d+)\s(red|green|blue)", game)
        for rnd in rnds:
            gems[rnd[1]] -= int(rnd[0])
            if( gems[rnd[1]] < 0 ):
                possible = False
                break

    if possible:
        possibleGames.add(gameId)

print(sum(possibleGames))