import re
f = open("finalinput")

lines = [line.strip() for line in f.readlines()]
s = 0

for line in lines:
    parts = line.split(":")
    cardID = int(re.findall("\d+", parts[0])[0])

    cards = parts[1].split("|")
    winning = re.findall("\d+", cards[0])
    got = re.findall("\d+", cards[1])

    matches = set()
    for w in winning:
        matches.add(w)

    match = False
    points = 1
    for g in got:
        if( g in matches ):
            match = True
            points *= 2

    if match:
        s += points // 2

print(s)
