f = open('inputfinal')
lines = f.readlines()

s = 0
for line in lines:
    line = line.strip()

    a,b,c,d = map(int, line.replace(',','-').split('-'))
    sections = set(range(a, b+1))
    sections2 = set(range(c, d+1))
    if len(sections & sections2) > 0:
        s += 1

print(s)
