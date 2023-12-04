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
    cardsWon[cardID] = points
    process.append(cardID)

idx = 0
while idx < len(process):
    points = cardsWon[process[idx]]
    for e in range(process[idx]+1, process[idx]+points+1):
        process.append(e)
    idx += 1

print(len(process))
