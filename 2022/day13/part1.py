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
s = 0
idx = 1
while True:
    left = f.readline().strip()
    right = f.readline().strip()
    f.readline()
    
    # End of File, stop the loop
    if len(left) == 0:
        break

    # JSON lists! Use the pre-made parser
    left, right = json.loads(left), json.loads(right)
    if compare(left, right):
        s += idx
    idx += 1

print(s)

# Guess: 6795 (too high)
# Guess: 756 (too low)