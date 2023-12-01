f = open("finalinput")

spelled = {
    '0' : '0',
    '1' : '1',
    '2' : '2', 
    '3' : '3', 
    '4' : '4', 
    '5' : '5', 
    '6' : '6',
    '7' : '7',
    '8' : '8', 
    '9' : '9',
    "zero" : '0',
    "one" : '1',
    "two" : '2',
    "three" : '3',
    "four" : '4',
    "five" : '5',
    "six" : '6',
    "seven" : '7',
    "eight" : '8',
    "nine" : '9'
}

s = 0
lines = f.readlines()
for line in lines:
    first = None
    last = None

    firstFoundAt = len(line)
    lastFoundAt = -1

    for k in spelled.keys():
        f = line.find(k)
        l = line.rfind(k)

        if f != -1 and f < firstFoundAt:
            first = spelled[k]
            firstFoundAt = f
        if l > lastFoundAt:
            last = spelled[k]
            lastFoundAt = l

    s += int( first + last )

print(s)
