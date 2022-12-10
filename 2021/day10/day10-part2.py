import sys 

with open("input", 'r') as f:
    total = 0
    points = {
        ')': ['(',1],
        ']': ['[',2],
        '}': ['{',3],
        '>': ['<',4]
    }
    closings = {
        '(':')',
        '[':']',
        '{':'}',
        '<':'>'
    }

    stack = []
    incomplete = []
    for line in f:
        line = line.strip()

        for letter in line:
            if letter in points:
                if len(stack) > 0:
                    opener = stack.pop()
                    # Invalid lines, throw it away
                    if opener != points[letter][0]:
                        stack = []
                        break
            else:
                # Put the opener onto the stack 
                stack.append(letter)

        # Incomplete line.  Store for the stack for scoring
        if len(stack) > 0:
            incomplete.append(stack)
    
        stack = []

    totals = [] 
    for line in incomplete:
        # Score incomplete lines by finding correct closers
        total = 0
        while len(line) > 0:
            opener = line.pop()
            closer = closings[opener]
        
            total *= 5
            total += points[closer][1]
        totals.append(total)

    # Score is the median of the totals
    totals = sorted(totals)
    print( totals[ len(totals) // 2 ])