f = open("finalinput")

lines = f.readlines()
maxTotal = 0

total = 0
maxElf = -1

spot = 0
for line in lines:
    if len(line) == 1:
        if total > maxTotal:
            maxTotal = total
            maxElf = spot
        total = 0
    else:
        total += int(line)
    spot += 1

print( maxTotal)