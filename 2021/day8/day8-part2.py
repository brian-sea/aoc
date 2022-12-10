import sys 

with open("input", 'r') as f:
    sumNumbers = 0
    for line in f:

        line = line.strip()
        parts = line.split(' | ')
        signals = parts[0].split(' ')
        digits = parts[1].split(' ')

        # signals -> digit
        numSignals = {
            2 : 1,
            4 : 4,
            3: 7,
            7: 8
        }
        digitSignals = dict()
        digitMap = dict()
        
        # 1, 4, 7, 8 have unique number of symbols
        # Put the rest in the unknown pile
        unknowns = []
        for digit in signals:

            # Sort the signal to remove permutations
            digit = ''.join(sorted(digit))
            c = len(digit)
            if c in numSignals:
                digitSignals[ numSignals[c] ] = digit
                digitMap[digit] = numSignals[c]
            else:
                unknowns.append(digit)

        # All other symbols are made up of 1, 4, and 7 signals
        for unknown in unknowns:
            
            # Sort the unknown to permutations
            unknown = ''.join(sorted(unknown))

            # Count common signals with 1, 4, and 7
            OneSigs = len(set(unknown).intersection(set(digitSignals[1])))
            FourSigs = len(set(unknown).intersection(set(digitSignals[4])))
            SevenSigs = len(set(unknown).intersection(set(digitSignals[7])))

            # 2, 3, 5 have length 5
            if( len(unknown) == 5 ):                
                # 3 -- All of 1's signals
                if OneSigs == 2 :
                    digitMap[unknown] = 3
                # 2 - 2 of 4's signals
                elif FourSigs == 2:
                    digitMap[unknown] = 2
                # 5 - 3 of 4's signals + 1 of 1's signal
                elif FourSigs == 3 and OneSigs == 1:
                    digitMap[unknown] = 5
            
            # 0, 6, 9
            if len(unknown) == 6:
                # 9 - has 4 and 7 signals
                if SevenSigs == 3 and FourSigs == 4:
                    digitMap[unknown] = 9
                # 3 of 4's Signals and 1 of 1's signal
                elif FourSigs == 3 and OneSigs == 1:
                    digitMap[unknown] = 6
                else:
                    # Odd symbol out!
                    digitMap[unknown] = 0

        num = ''
        for digit in digits:
            # Sort the digit to remove permutations
            digit = ''.join(sorted(digit))
            num += str(digitMap[digit])
        sumNumbers += int(num)

    print( sumNumbers )
        


    