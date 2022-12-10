import sys 

with open("input", 'r') as f:

    count = 0    
    for line in f:

        line = line.strip()
        parts = line.split(' | ')
        signals = parts[0].split(' ')
        digits = parts[1].split(' ')

        # signals -> digit
        digitSignals = {
            2 : 1,
            4 : 4,
            3: 7,
            7: 8
        }

        for digit in digits:
            countSymbols = dict()
            for signal in digit:
                if signal in countSymbols:
                    countSymbols[signal] += 1
                else:
                    countSymbols[signal] = 1

            c = len(countSymbols.keys())
            if c in digitSignals:
                count += 1

    print( count )
        


    