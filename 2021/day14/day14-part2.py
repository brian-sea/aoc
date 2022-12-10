import sys

'''
 ATTEMPT #5  !@#$@!$@!$#@$
 What I attempted:
    (1) Manual Expansion (HAHAHAHAHA)
    (2) Linked List Expansion (HAHAHAHHAHA)
    (3) Recursive Expansion (too slow)
    (4) Sliding Window (too slow)
    (5) Derive the next step's count from previous... UGH!
'''

with open('input','r') as f:

    template = f.readline().strip()
    f.readline()

    countElements = dict()
    rules = dict()
    for line in f:
        line = line.strip().split(' -> ')
        rules[line[0]] = line[1]

    # Count starting pairs in template
    for i in range(len(template)-1):
        s = template[i]+template[i+1]
        if s in countElements:
            countElements[s] += 1
        else:
            countElements[s] = 1


    step = 0
    while step < 40:

        tempCount = dict()

        # AB->C, means AC and AB exists (per step)
        for pair in countElements:
            fp = pair[0]+rules[pair]
            sp = rules[pair]+pair[1]

            # Create the First Pair or add to it the number of times the original pair happens
            if fp in tempCount:
                tempCount[fp] += countElements[pair]
            else:
                tempCount[fp] = countElements[pair]

            # Create the Second Pair or add to it the number of times the original pair happens
            if sp in tempCount:
                tempCount[sp] += countElements[pair]
            else:
                tempCount[sp] = countElements[pair]       

        # The next step builds off the new count
        countElements = tempCount
        step += 1

    # Count the number of times each element occurs
    # We only need to look at the first element of each pair, because the second
    # element will be the first of another pair... 
    elementCount = dict()
    for pair in countElements:
        if pair[0] in elementCount:
            elementCount[pair[0]] += countElements[pair]
        else:
            elementCount[pair[0]] = countElements[pair]

    #  Except the last element... add it in
    elementCount[template[-1]] += 1

    leastElement = min(elementCount.values())
    mostElement = max(elementCount.values())
    print(mostElement-leastElement)