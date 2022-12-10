import sys
import re
import math

with open('input', 'r') as f:
    line = f.readline().strip()
    matches = re.match('target area: x=(\S+), y=(\S+)', line)
    
    targetX = [ int(i) for i in matches[1].split('..')]
    targetY = [ int(i) for i in matches[2].split('..')]

    #print( targetX, targetY)
    maxYOverall = None
    for velX in range(0, 201):
        for velY in range(0, 200):
            currVelX = velX
            posX = 0
            posY = 0

            maxY = None
            while posY >= targetY[0] or velY > 0:
                posX += currVelX
                posY += velY

                if currVelX != 0:
                    currVelX -= int(math.copysign(1, currVelX))
                velY -= 1

                if maxY == None or posY > maxY:
                    maxY = posY

                if targetX[0] <= posX <= targetX[1]:
                    if targetY[0] <= posY <= targetY[1]:
                        if maxYOverall == None or maxY > maxYOverall:
                            maxYOverall = maxY
                            break

    print("MAX:", maxYOverall)