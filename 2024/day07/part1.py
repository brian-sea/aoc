import sys
import re

filename = sys.argv[1] if len(sys.argv) > 1 else 'test-input.dat'
f = open(filename)

s = 0
for line in f:
    testValue, values = line.strip().split(":")
    testValue = int(testValue)
    values = list(map(int, values.split()))
    
    qCalc = set()
    checkCalc = set()

    qCalc.add(values[0])
    idx = 1
    while idx < len(values):
        for val in qCalc:

            calcs = [
                val + values[idx],
                val * values[idx]
            ]
            for calc in calcs:
                if calc <= testValue:
                    checkCalc.add(calc)

        qCalc = checkCalc
        checkCalc = set()
        idx += 1

    if testValue in qCalc:
        s += testValue
    
print(s)