import json

def compare(l, r):
    if isinstance(l, int):
        l = [l]
    if isinstance(r, int):
        r = [r]

    rtn = True
    spot = 0
    while spot < len(l):
        if spot == len(r):
            return False
        elif isinstance(l[spot], list) or isinstance(r[spot], list):
            rtn = compare(l[spot], r[spot])
            if rtn != None:
                return rtn
        elif l[spot] < r[spot]:
            return True
        elif l[spot] > r[spot]:
            return False
        spot += 1

    if spot == len(l) and spot != len(r):
        return True

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

dividers = [ [[2]], [[6]]]
for d in dividers:
    pairs.append(d)

for i in range(len(pairs)):
    for j in range(i, len(pairs)):
        if compare(pairs[i], pairs[j]) == False:
            tmp = pairs[i]
            pairs[i] = pairs[j]
            pairs[j] = tmp

s = 1
d = 0
for idx, pair in enumerate(pairs):  
    if d == len(dividers):
        break
    if pair == dividers[d]:
        s *= idx+1
        d += 1
print(s)