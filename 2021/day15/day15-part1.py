import sys
from collections import Counter 

with open('input', 'r') as f:

    riskLevels = Counter()
    visited = dict()
    map = []
    for line in f:
        line = line.strip()
        map.append( [int(x) for x in line])
    
    riskLevels[(0,0)] = 0

    # Lower right coord
    bY = len(map) - 1
    bX = len(map[bY]) - 1

    curX = 0
    curY = 0
    minRisk = 0
    while curX != bX or curY != bY:

        dirs = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]

        visited[(curY, curX)] = True
        for (dy, dx) in dirs:
            newY = curY + dy
            if 0 <= newY < len(map):
                newX = curX + dx
                if 0 <= newX < len(map[newY]): 
                    np = (newY, newX)
                    if np not in riskLevels:
                        riskLevels[np] = None

                    nr = riskLevels[(curY, curX)] + map[newY][newX]
                    if riskLevels[np] == None or nr < riskLevels[np]:
                        riskLevels[np] = nr

        newMin = None
        minRiskLevel = None
        for pos in riskLevels.keys():
            if pos not in visited:
                if minRiskLevel == None or riskLevels[pos] < minRiskLevel:
                    newMin = pos
                    minRiskLevel = riskLevels[pos]
        
        (curY, curX) = newMin
        minRisk = riskLevels[newMin]

    print(minRisk)
