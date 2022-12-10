import sys 

with open("input", 'r') as f:
    total = 0
    points = {
        ')': ['(',3],
        ']': ['[',57],
        '}': ['{',1197],
        '>': ['<',25137]
    }

    stack = []
    for line in f:
        line = line.strip()

        for letter in line:
            if letter in points:
                if len(stack) > 0:
                    opener = stack.pop()
                    if opener != points[letter][0]:
                        total += points[letter][1]
                        stack = []
                        break
            else:
                stack.append(letter)


    print(total)