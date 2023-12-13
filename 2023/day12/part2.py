import re
import datetime
from collections import defaultdict
        
f = open("input2")
lines = [line.strip() for line in f.readlines()]

# Not optimized - Not Complete
# Need to implement Sliding Window Dynamic Programming... 

s = 0
for line in lines:
    [p,n] = line.split(' ')
    pattern = p
    nums = n
    for x in range(4):
        pattern += "?" + p
        nums += ","+n

    nums = [ int(x) for x in nums.split(',')]

    # Each element is array of integers of contiguous brokens
    # Fixed adds a zero
    # Element 0 is the spot in nums we're on
    arrangements = [
        [0,0] # Initial
    ]

    memory = {}
    foundEarly = 0
    for idx,ch in enumerate(pattern):

        additions = []
        for arrange in arrangements:

            if arrange[0] == len(nums)-1 and arrange[-1] == nums[-1]:
                foundEarly += 1
                continue

            # Start chunk
            if ch == '#':
                if arrange[-1] > 0:
                    arrange.append(0)
                    arrange[0] += 1
                arrange[-1] -= 1

                if arrange[0] < len(nums) and nums[arrange[0]] >= abs(arrange[-1]):
                    additions.append(arrange)

            elif ch == '.' and arrange[-1] != 0:
                arrange[-1] = abs(arrange[-1])

                if arrange[-1] == nums[arrange[0]]:
                   additions.append(arrange)

            elif ch == '?':

                # Place a .
                if nums[ arrange[0] ] == abs(arrange[-1]) or arrange[-1] == 0:
                    nl = arrange.copy()
                    nl[-1] = abs(nl[-1])
                    additions.append(nl)
                
                # Place a #
                if arrange[-1] > 0:
                    arrange.append(0)
                    arrange[0] += 1
                arrange[-1] -= 1
            
                if arrange[0] < len(nums) and nums[arrange[0]] >= abs(arrange[-1]):
                    additions.append(arrange)
            else:
                additions.append(arrange)


        arrangements = additions

    for arr in arrangements:
        arr[-1] = abs(arr[-1])

    possible = 0
    for arr in arrangements:
        if arr[-1] == 0 or arr[-1] == nums[-1]:
            if arr[0]+1 == len(nums):
                possible += 1

    s += possible + foundEarly

print(s)