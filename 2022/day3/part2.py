f = open("inputfinal")
lines = f.readlines()

s = 0
lineSpot = 0
contains = None
for line in lines:   
    line = line.strip()

    lineSpot += 1
    if lineSpot % 3 == 1:
        contains = set(line)
    else:
        contains = contains.intersection(set(line))
        if lineSpot % 3 == 0 and len(contains) == 1:
            letter = contains.pop()
            val = ord('a')-1
            if letter.isupper():
                val = ord('A')-27
            s += ord(letter) - val
print(s)