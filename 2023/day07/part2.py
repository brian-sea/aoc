import re
import datetime
from collections import defaultdict
        
class sameDict(dict):
    def __init__(self, d={}):
        for i in d:
            self[i] = d[i]
    
    def __missing__(self, k):
        return k

rank = sameDict({
    'A':'E',
    'K':'D',
    'Q':'C',
    'J':'1',
    'T':'A'
})

rankedHands = [{
    "hand": "1",
    "kind" : 0,
    "score": 0,
    "bid" : 0
}]

f = open("finalinput")
lines = [line.strip() for line in f.readlines()]
for line in lines:
    hand,bid = line.split(' ')

    counts = defaultdict( lambda: 0)
    for h in hand:
        counts[h] += 1

    jokers = counts['J']
    del counts['J']
    counts['Z'] = 0

    vals = list(counts.values())
    vals.sort(reverse=True)
    vals = sum(vals[:2])
    twoPair = 3 if (vals + jokers >= 4) else 0
    fullHouse = 5 if( vals + jokers >= 5) else 0

    ofAKind = max(counts.values()) + jokers
    if ofAKind >= 3:
        ofAKind += 1
    if ofAKind >= 5:
        ofAKind += 1

    handRank = max(ofAKind, twoPair, fullHouse)
    counts['J'] = jokers
    del counts['Z']

    score = []
    for h in hand:
        score.append(rank[h])
    score = ''.join(score)

    pos = 1
    while pos < len(rankedHands):
        ranked = rankedHands[pos]
        if( ranked['kind'] < handRank ):
            break
        elif( ranked['kind'] == handRank and ranked['score'] < score):
            break
        pos += 1

    rankedHands.insert(pos, {
        "hand": hand,
        "score": score,
        "kind": handRank,
        "bid": int(bid)
    })

rankedHands.reverse()

sumWinnings = 0
pos = 0 
while pos < len(rankedHands):
    sumWinnings += rankedHands[pos]['bid']*(pos+1)
    pos += 1
print(sumWinnings)

# Answer: 248750248