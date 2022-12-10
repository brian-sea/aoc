import sys 
import re

numbers = []
called = dict()
AlreadyWon = dict()

def checkBoard( board, row, col):
    c = 0
    while c < len(board[row]):
        if board[row][c] not in called:
            break
        c += 1

    r = 0
    while r < len(board):
        if board[r][col] not in called:
            break
        r += 1
    
    return r == len(board) or c == len(board[row])

def scoreBoard(board):
    score = 0
    for row in board:
        for col in row:
            if col not in called:
                score += col

    return score

    
with open('input','r') as f:
    numbers = f.readline()
    # Split the line and turn them into integers
    numbers = [int(num) for num in numbers.split(',')]

    boards = []
    board = []
    for line in f:
        line = line.strip()
        if len(line) == 0: 
            if len(board) != 0:
                boards.append(board)
                board = []
            continue

        row = [int(num) for num in re.split('\s+', line)]
        board.append(row)

    # Append the last board
    board.append(board)

lastScore = -1
for num in numbers:
    called[num] = True

    for board in boards:
        for rownum,row in enumerate(board):
            try:
                col = row.index(num)
                win = checkBoard(board, rownum, col)
                if win == True and str(board) not in AlreadyWon:
                    score = scoreBoard( board )
                    lastScore = score * num
                    AlreadyWon[str(board)] = True
            except Exception as e:
                pass

print(lastScore)