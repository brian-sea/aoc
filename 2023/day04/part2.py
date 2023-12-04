import re
f = open("finalinput")

lines = [line.strip() for line in f.readlines()]

process = []
cardsWon = dict()
for line in lines:
    parts = line.split(":")
    cardID = int(re.findall("\d+", parts[0])[0])

    cards = parts[1].split("|")
    winning = re.findall("\d+", cards[0])
    got = re.findall("\d+", cards[1])

    matches = set()
    for w in winning:
        matches.add(w)

    points = 0
    for g in got:
        if( g in matches ):
            points += 1

    if cardID in cardsWon:
        cardsWon[cardID] += 1
    else:
        cardsWon[cardID] = 1

    for e in range(cardID+1, cardID + points + 1):    
        if e in cardsWon:
            cardsWon[e] += cardsWon[cardID]
        else:
            cardsWon[e] = cardsWon[cardID]


print(sum(cardsWon.values()))



