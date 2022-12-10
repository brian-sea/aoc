f = open("finalinput")

lines = f.readlines()
maxTotals = []

total = 0
for line in lines:
    if len(line) == 1:
        maxTotals.append(total)
        maxTotals.sort(reverse=True)
        while len(maxTotals) > 3:
            maxTotals.pop()
        total = 0
    else:
        total += int(line)

print(sum(maxTotals))