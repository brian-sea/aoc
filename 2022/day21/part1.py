f = open("inputfinal")

monkeys = {}
def calculate(left, op, right):
    
    if monkeys[left]['num'] == None:
        lname = left
        left = calculate(monkeys[left]['left'], monkeys[left]['op'], monkeys[left]['right'])
        monkeys[lname]['num'] = left
    elif not isinstance(left, int):
        left = monkeys[left]['num']

    if monkeys[right]['num'] == None:
        rname = right
        right = calculate(monkeys[right]['left'], monkeys[right]['op'], monkeys[right]['right'])
        monkeys[rname]['num'] = right
    elif not isinstance(right, int):
        right = monkeys[right]['num']

    return int(op(left, right))

for line in f:
    parts = line.strip().split(' ')

    name = parts[0][:-1]
    left = op = right = num = None
    if len(parts) == 2:
        num = int(parts[-1])
    else:
        left,op,right = parts[1:]

    op_funcs = {
        '+' : int.__add__,
        '-' : int.__sub__,
        '*' : int.__mul__,
        '/' : int.__truediv__,
        None: None
    }

    monkeys[name] = {
        'num':num,
        'left': left,
        'op' : op_funcs[op],
        'right': right
    }

print(calculate(monkeys['root']['left'], monkeys['root']['op'], monkeys['root']['right']))

