f = open('inputfinal')
lines = f.readlines()

s = 0
for line in lines:
    line = line.strip()
    
    a,b,c,d = map(int, line.replace(',','-').split('-'))
    set1, set2 = set(range(a,b+1)), set(range(c,d+1))
    if len(set1|set2) == len(set1) or len(set2|set1) == len(set2):
        s += 1

print(s)
