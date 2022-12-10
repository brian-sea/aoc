f = open("inputfinal")
lines = f.readlines()

s = 0
for line in lines:    
    line = line.strip()
    comps = [line[:len(line)//2], line[len(line)//2:]]

    contains = set(comps[1]).intersection(set(comps[0]))
    if len(contains) == 1:
        letter = contains.pop()
        val = ord('a')-1
        if letter.isupper():
            val = ord('A')-27
        s += ord(letter) - val
print(s)