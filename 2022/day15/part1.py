import re
import math
f = open('inputfinal')

yCheck = 2000000
noBeacons = set()
beacons = set()

for line in f:
    (sensor, beacon) = [ tuple(map(int,p)) for p in re.findall(r"(\d+)\, y=(\d+)", line) ]
    beacons.add(beacon)


    dx = abs(sensor[0] - beacon[0])
    dy = abs(sensor[1] - beacon[1])
    totalDistance = dx + dy
    
    distanceToY = abs(sensor[1]-yCheck)
    wingspan = totalDistance - distanceToY
    for x in range(sensor[0]-wingspan, sensor[0]+wingspan+1):
        if (x, yCheck) not in beacons:
            noBeacons.add( (x,yCheck) )
        
print(len(noBeacons))
