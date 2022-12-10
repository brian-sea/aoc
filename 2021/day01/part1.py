
inFile = 'input'
with open(inFile, 'r') as f:
    increases = 0
    
    oldMeasure =  None
    for line in f:
        measure = int(line.strip())
        
        if oldMeasure != None and measure > oldMeasure:
            increases += 1

        oldMeasure = measure

    print( increases)