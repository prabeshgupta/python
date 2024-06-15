#Topper from file

from cmath import inf

with open("C:\\Users\gamerzchoices\Documents\CODING\python\School\Week 3\Day 2\input.txt", "r") as txt:
    lines =  txt.readlines()

narr = []
studentScore = {}

for line in lines:
    narr = line.strip().split()
    print(narr)
    name = narr[0]
    scores = []
    for score in narr[1:]:
        scores.append(int(score))
    print(scores)
    total = sum(scores)
    lenth = len(scores)
    avg = total / lenth
    studentScore[name] = avg

print(studentScore)

with open("C:\\Users\gamerzchoices\Documents\CODING\python\School\Week 3\Day 2\output.txt","w") as out:
    high = float(-inf)
    for key, val in studentScore.items():
        out.write(f"{key}: {val}\n")
        if studentScore[key] > high:
            top, high = key, studentScore[key]
    print(f"{top}: {high:.2f}\n")
