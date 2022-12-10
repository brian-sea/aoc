scores = {
    "A": 1,
    "B": 2,
    "C": 3,
}
wins = {
    "A": "C",
    "B": "A",
    "C": "B"
}

f = open("inputfinal")
lines = f.readlines()

totalScore = 0
for line in lines:
    parts = line.strip().split(" ")
    
    val = ord(parts[0]) - ord("A")
    if parts[1] == "X":
        val = ( val - 1) % 3
    elif parts[1] == "Z":
        val = (val + 1) % 3
    parts[1] = chr(val + ord("A"))

    totalScore += scores[parts[1]]
    if wins[parts[1]] == parts[0]:
        totalScore += 6
    elif wins[parts[0]] != parts[1]:
        totalScore += 3

print("Total:", totalScore)