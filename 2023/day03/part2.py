import re
f = open("finalinput")

lines = [line.strip() for line in f.readlines()]
row = 0

gears = {}
while row < len(lines):
    nums = re.finditer("\d+", lines[row])
    for num in nums:
        added = False
        for r in range(row-1, row+2):
            for c in range(num.start()-1, num.end()+1):
                if not added:
                    if 0 <= r < len(lines) and 0 <= c < len(lines[r]):
                        if lines[r][c] == '*':
                            if f'{r},{c}' not in gears:
                                gears[f'{r},{c}'] = [int(num.group())]
                            else:
                                gears[f'{r},{c}'].append(int(num.group()))
                            added = True

    row += 1

ans = 0
for gear in gears:
    if len( gears[gear] ) == 2:
        ans += gears[gear][0] * gears[gear][1]
print(ans)
