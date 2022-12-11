import re

f = open('inputfinal')

LCM = 1
monkeys = []
lines = list(map(str.strip, f.readlines()))
spot = 1    
while spot < len(lines):
    startingItems = list(map(int, re.findall("\d+", lines[spot])))
    worryOp, worryMod = re.findall("old\s(\D)\s(\w+)", lines[spot+1])[0]
    condTest = int(re.findall("\d+", lines[spot+2])[0])
    ifTrue = int(re.findall("\d+", lines[spot+3])[0])
    ifFalse = int(re.findall("\d+", lines[spot+4])[0])

    monkey = {
        'items': startingItems,
        'worryMod': (worryOp, worryMod),
        'condTest': condTest,
        'true': ifTrue,
        'false': ifFalse,
        'numInspected': 0
    }

    # Find LCM of all the condition tests (see below)
    # The LCM is the largest possible number which can exist across all monkeys
    LCM *= monkey['condTest']

    monkeys.append(monkey)
    spot += 7

rnd = 0
while rnd < 10000:
    for monkey in monkeys:

        monkey['numInspected'] += len(monkey['items'])
        while len(monkey['items']) > 0:
            lvl = monkey['items'].pop(0)

            val = int(monkey['worryMod'][1]) if monkey['worryMod'][1] != 'old' else lvl    

            # Also a%LCM == a+val%LCM and a%LCM == a*val%LCM
            lvl = lvl % LCM

            if monkey['worryMod'][0] == '+':
                lvl += val
            else:
                lvl *= val

            toWhom = monkey['false']
            if lvl % monkey['condTest'] == 0:
                toWhom = monkey['true']

            monkeys[toWhom]['items'].append(lvl)
    rnd += 1

sort_m = sorted(monkeys, reverse=True, key=lambda x: x['numInspected'])
print( sort_m[0]['numInspected']*sort_m[1]['numInspected'])