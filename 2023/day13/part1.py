import re
import datetime
from collections import defaultdict


def find_reflections(line):
    rtn = []

    for left,char in enumerate(line):
        mid = left
        right = left + 1
        while right < len(line):
            if line[left] != line[right]:
                break

            if left == 0 or right == len(line)-1:
                rtn.append(mid+1)
                break

            left -= 1
            right += 1

    return rtn

def reflect_cols(pattern):
    mids = None
    for p in pattern:
        r = find_reflections(p)
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

def reflect_rows(pattern):
    transpose = list(zip(*pattern))
    return reflect_cols(transpose)
    



f = open("finalinput")
lines = [line.strip() for line in f.readlines()]

s = 0
pattern = []
for line in lines:
    if len(line) != 0:
        pattern.append(line)
    else:
        c = reflect_cols(pattern)
        for l in c:
            s += l
    
        r = reflect_rows(pattern)
        for l in r:
            s += l*100

        pattern.clear()


c = reflect_cols(pattern)
for l in c:
    s += l

r = reflect_rows(pattern)
for l in r:
    s += l*100
print(s)