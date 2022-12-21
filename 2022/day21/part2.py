f = open("inputfinal")

monkeys = {}
missingMonkey = 'humn'
def calculate(left, op, right, test):
    global missingMonkey

    if left == missingMonkey:
        left = test
    elif monkeys[left]['num'] == None:
        lname = left
        left = calculate(monkeys[left]['left'], monkeys[left]['op'], monkeys[left]['right'], test)
        monkeys[lname]['num'] = left
    elif not isinstance(left, int):
        left = monkeys[left]['num']

    if right == missingMonkey:
        right = test
    elif monkeys[right]['num'] == None:
        rname = right
        right = calculate(monkeys[right]['left'], monkeys[right]['op'], monkeys[right]['right'], test)
        monkeys[rname]['num'] = right
    elif not isinstance(right, int):
        right = monkeys[right]['num']

    # We hit the undefined variable without a test
    if left == None or right == None:
        raise ValueError

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


lessThan = int.__gt__
greaterThan = int.__lt__

rLeft = monkeys['root']['left']
rRight = monkeys['root']['right']

test = rRight
try:
    target = calculate(monkeys[rLeft]['left'],monkeys[rLeft]['op'], monkeys[rLeft]['right'], None)
except:
    target = calculate(monkeys[rRight]['left'], monkeys[rRight]['op'], monkeys[rRight]['right'], None)
    test = rLeft

lo = 0
high = int(1e20)
found = None

if calculate(monkeys[test]['left'], monkeys[test]['op'], monkeys[test]['right'], (lo+high)//2) > 0:
    lessThan, greaterThan = greaterThan, lessThan

while lo < high:
    mid = (lo + high) // 2
    val = calculate(monkeys[test]['left'], monkeys[test]['op'], monkeys[test]['right'], mid)
    
    if lessThan(val,target):
        lo = mid + 1
    elif greaterThan(val, target):
        high = mid - 1
    else:
        found = mid
        break

    # Reset the DP memory
    for m in monkeys:
        if monkeys[m]['op'] != None:
            monkeys[m]['num'] = None    

print(found)