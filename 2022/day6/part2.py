f = open("inputfinal")

line = f.readline()
found = {}

spot = 0
start = 0
while spot < len(line) and len(found) != 14:

    letter = line[spot]
    if letter in found:
        while line[start] != letter:
            del found[ line[start] ]
            start += 1
        start+= 1
    found[letter] = spot
    spot += 1

print(spot)