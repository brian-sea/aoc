import sys

def binStringToDec(s):
    rtn = 0

    power = len(s) - 1
    spot = 0
    while spot < len(s):
        if s[spot] == '1':
            rtn += pow(2, power)
        spot += 1
        power -= 1
    return rtn

with open('input', 'r') as f:
    enhancement = f.readline().strip()
    f.readline()

    image = []
    for line in f:
        line = '.'+line.strip()+'.'
        image.append(line)
    
    line = '.'*len(image[0])
    image.insert(0,line)
    image.append(line)


    for i in range(2):
        outputImage = []
        for y in range(len(image)):
            outputRow = []
            for x in range(len(image[y])):  
                binString = ''
                for row in range(y-1, y+2):
                    if 0 <= row < len(image):
                        for col in range(x-1,x+2):
                            if 0 <= col < len(image[row]):
                                if image[row][col] == '#':
                                    binString += '1'
                                else:
                                    binString += '0'
                            else:
                                binString += '0'
                    else:
                        binString += '000'

                enhanceIdx = binStringToDec(binString)
                outputRow.append(enhancement[enhanceIdx])
            outputImage.append(outputRow)
        
        image = outputImage

        for row in image:
            row.insert(0,'.')
            row.append('.')

        '''print('\n----------\n')
        for row in image:
            for col in row:
                print( col, end='')
            print()
        '''
        line = '.'*len(image[0])
        image.insert(0,line)
        image.append(line)


    countLight = 0
    for row in image:
        for col in row:
           if col == '#':
               countLight += 1

    print(countLight)