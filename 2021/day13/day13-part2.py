import sys
import re

paper = []
maxX = -1
maxY = -1
with open('input','r') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            pass
        elif line[0] != 'f':
            line = line.strip()
            dot = [int(x) for x in line.split(',')]

            col = dot[0]
            row = dot[1]

            for y in range(len(paper), row+1):
                paper.append([])

            for x in range(len(paper[row]), col+1):
                paper[row].append(' ')

            if maxX < col:
                maxX = col
            if maxY < row:
                maxY = row

            paper[row][col] = '#'
        else:
            for row in paper:
                while len(row) <= maxX:
                    row.append(' ')

            m = re.match(r'fold along (\w)=(\d+)', line)
            axis = m[1]
            coord = int(m[2])
            
            if axis == 'y':
                for row in range(coord+1, maxY+1):
                    for col in range(0, maxX+1):
                        if( paper[row][col] == '#'):
                            paper[maxY-row][col] = paper[row][col]
                maxY = coord-1
            elif axis == 'x':
                for col in range(coord+1, maxX+1):
                    for row in range(0, maxY+1):
                        if(paper[row][col] == '#'):
                            paper[row][maxX-col] = paper[row][col]
                maxX = coord-1

    count =0
    print()
    for row in range(0,maxY+1):
        for col in range(0,maxX+1):
            print(paper[row][col], end=' ')
        print()
    print(count)