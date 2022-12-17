import re

def djikstra(tunnels, start, end):
    visited = set()
    visited.add(start)

    paths = {}
    for each in tunnels:
        # Current distance, Coming From (for backtracking)
        paths[each] = (float('inf'), None)
    
    origStart = start
    paths[start] = (0, None)
    while start != end:
        leads = tunnels[start]['leadsTo']
        traveled = paths[start][0]
        for p in leads:
            if p not in visited and traveled + 1 < paths[p][0]:
                paths[p] = (traveled + 1 , start)

        minPath = None
        for each in paths:
            if each not in visited:
                if minPath == None or paths[each] < paths[minPath]:
                    minPath = each

        visited.add( minPath )
        start = minPath

    path = []
    while start != origStart:
        path.insert(0,paths[start][1])
        start = paths[start][1]

    return path, paths[end][0]


# Brute force (BLAH!!!)
# Need to switch to DP
def doBranch(tunnels, minutes, released, start, opened):
    maxReleased = released
    if minutes > 0:
        for end in tunnels:
            if tunnels[end]['rate'] > 0 and end not in opened:
                path, dist = djikstra(tunnels, start, end)
                
                if len(path) > 0 and minutes > len(path)+1:                  
                    released += tunnels[end]['rate'] * (minutes-len(path)-1)
                    opened.add(end)            
                    rtn = doBranch( tunnels, minutes-len(path)-1, released, end, opened)
                    released -= tunnels[end]['rate'] * (minutes-len(path)-1)
                    opened.remove(end)

                    if rtn > maxReleased:
                        maxReleased = rtn

    return maxReleased

f = open('input')
tunnels = {}
for line in f:  
    label, rate, paths = re.findall("Valve\s([A-Z]+).+=(\d+).+valves?\s([^\n]+)", line)[0]    
    tunnels[label] = {
        'name':label,
        'rate': int(rate),
        'leadsTo': list(map(str.strip, paths.split(',')))
    }

opened = set()
minutes = 30
released = 0
start = 'AA'
opened.add(start)

print(doBranch(tunnels, minutes, 0, "AA", opened))

# Guess: 1372 (too low)
# Guess: 1651 (too low)