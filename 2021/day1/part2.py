from os import WNOHANG


inFile = 'input'
with open(inFile, 'r') as f:
    increases = 0
    oldMeasure = None

    WINDOW_SIZE = 3
    windowMeasures = []
    for line in f:
        measure = int(line.strip())
        
        # Add measure to everything in our window
        spot = 0
        while spot < len(windowMeasures):
            windowMeasures[spot] += measure
            spot+=1            
        windowMeasures.append(measure)

        # If the Window size is correct, then the 
        # first element is a WINDOW_SIZE sum
        if len(windowMeasures) == WINDOW_SIZE:
            m = windowMeasures.pop(0)
            if oldMeasure != None and m > oldMeasure:
                increases += 1
            oldMeasure = m

    print( increases)