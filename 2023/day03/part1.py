import re
f = open("finalinput")

lines = [line.strip() for line in f.readlines()]
row = 0
s = 0

while row < len(lines):
    nums = re.finditer("\d+", lines[row])
    for num in nums:
        added = False
        for r in range(row-1, row+2):
            for c in range(num.start()-1, num.end()+1):
                if not added:
                    if 0 <= r < len(lines) and 0 <= c < len(lines[r]):
                        if( lines[r][c] != '.' and not lines[r][c].isdigit()):
                            s += int(num.group())
                            added = True

    row += 1
    
print(s)
