import json

def compare(l, r):
    # Turn the integers into lists
    if isinstance(l, int):
        l = [l]
    if isinstance(r, int):
        r = [r]

    rtn = True
    spot = 0
    while spot < len(l):

        # Right Side runs out, wrong order
        if spot == len(r):
            return False
        # one of them is a list, so compare them
        elif isinstance(l[spot], list) or isinstance(r[spot], list):
            rtn = compare(l[spot], r[spot])
            # Got an answer
            if rtn != None:
                return rtn
        elif l[spot] < r[spot]:
            return True
        elif l[spot] > r[spot]:
            return False
        spot += 1

    # Left ran out but right didn't, correct order
    if spot == len(l) and spot != len(r):
        return True

    # Keep Going!
    return None

f = open('inputfinal')
pairs = []
while True:
    left = f.readline().strip()
    right = f.readline().strip()
    f.readline()
    
    # End of File, stop the loop
    if len(left) == 0:
        break

    left, right = json.loads(left), json.loads(right)
    pairs.append(left)
    pairs.append(right)

dividers = [ [[2]], [[6]] ]
for d in dividers:
    pairs.append(d)

# Bubble Sort... 
for i in range(len(pairs)):
    for j in range(i, len(pairs)):
        if compare(pairs[i], pairs[j]) == False:
            tmp = pairs[i]
            pairs[i] = pairs[j]
            pairs[j] = tmp

# Find the dividers
s = 1
d = 0
for idx, pair in enumerate(pairs):  
    if d == len(dividers):
        break
    if pair == dividers[d]:
        s *= idx+1
        d += 1
print(s)