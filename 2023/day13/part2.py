import re
import datetime
from collections import defaultdict


def find_reflections(line, change=None):
    rtn = []

    for left,char in enumerate(line):
        mid = left
        right = left + 1
        while right < len(line):

            # Create Smudge
            if change != None and (left == change[1] or right == change[1]):
                if line[left] == line[right]:
                    break   
            else:    
                if line[left] != line[right]:
                    break

            if left == 0 or right == len(line)-1:
                rtn.append(mid+1)
                break

            left -= 1
            right += 1

    return rtn

def reflect_cols(pattern, change=None):
    mids = None
    for idx,p in enumerate(pattern):
        r = None
        if change != None and idx == change[0]:
            r = find_reflections(p, change)
            print("CHANGE:", change, r)
        else:
            r = find_reflections(p, None)

        if mids == None:
            mids = set()
            mids.update(r)
        else:
            remove = []
            for m in mids:
                if m not in r:
                    remove.append(m)
            for r in remove:
                mids.remove(r)

    return mids

def reflect_rows(pattern, change=None):
    transpose = list(zip(*pattern))
    return reflect_cols(transpose,change)
    



f = open("input2")
lines = [line.strip() for line in f.readlines()]

s = 0
pattern = []
for line in lines:
    if len(line) != 0:
        pattern.append(line)
    else:
        c = reflect_cols(pattern)
        r = reflect_rows(pattern)
        
        added = set()
        for row in range(len(pattern)):
            for col in range(len(pattern[row])):
                cnew = reflect_cols(pattern, (row,col))
                rnew = reflect_rows(pattern, (row,col))

                if cnew != c or rnew != r:
                    for l in cnew:
                        if l not in c and l not in added:
                            s += l
                            added.add(l)

                    for l in rnew:
                        if l not in r and l not in added:
                            s += l*100
                            added.add(l)
                    
                    

        pattern.clear()


c = reflect_cols(pattern)
r = reflect_rows(pattern)

added = set()
for row in range(len(pattern)):
    for col in range(len(pattern[row])):
        cnew = reflect_cols(pattern, (row,col))
        rnew = reflect_rows(pattern, (row,col))

        #print(c,cnew, r, rnew)
        if cnew != c or rnew != r:
            print("RRRRRRRR:", rnew)
            for l in cnew:
                if l not in c and l not in added:
                    print("ADDC:", l)
                    s += l
                    added.add(l)
            for l in rnew:
                if l not in r and l not in added:
                    print("ADDR:", l)
                    s += l*100
                    added.add(l)
            
print(s)

# Guess: 6220 (too low)
# Guess: 6228 (too low)