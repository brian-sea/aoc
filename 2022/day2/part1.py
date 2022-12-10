scores = {
    "Z": 3,
    "Y": 2,
    "X": 1
}
wins = {
    "X":"C",
    "Y":"A", 
    "Z":"B",
    "B":"X",
    "A":"Z",
    "C":"Y" 
}

f = open("inputfinal")
lines = f.readlines()

totalScore = 0
for line in lines:
    parts = line.strip().split(" ")
    totalScore += scores[parts[1]]
    
    if wins[parts[1]] == parts[0]:
        totalScore += 6
    elif wins[parts[0]] != parts[1]:
        totalScore += 3

print("Total:", totalScore)