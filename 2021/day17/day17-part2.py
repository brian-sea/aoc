import sys
import re
import math

with open('input', 'r') as f:
    line = f.readline().strip()
    matches = re.match('target area: x=(\S+), y=(\S+)', line)
    
    targetX = [ int(i) for i in matches[1].split('..')]
    targetY = [ int(i) for i in matches[2].split('..')]

    vels = set()
    #print( targetX, targetY)
    for velX in range(-500, 501):
        for velY in range(-500, 501):
            initVelY = velY
            currVelX = velX
            posX = 0
            posY = 0

            while posY >= targetY[0] or velY > 0:
                posX += currVelX
                posY += velY

                if currVelX != 0:
                    currVelX -= int(math.copysign(1, currVelX))
                velY -= 1

                if targetX[0] <= posX <= targetX[1]:
                    if targetY[0] <= posY <= targetY[1]:
                        vels.add( (velX, initVelY) )
                        break
                        

    print(len(vels))