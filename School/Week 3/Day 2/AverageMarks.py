from cmath import inf

with open("/home/aayushgupta/Documents/Python/School/Week 3/Day 2/input.txt", "r") as txt:
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

with open("/home/aayushgupta/Documents/Python/School/Week 3/Day 2/output.txt","w") as out:
    high= float(-inf)
    for key, val in studentScore.items():
        if studentScore[key] > float(high):
            top, high = key, studentScore[key]
    out.write(f"{top}: {high:.2f}\n")
