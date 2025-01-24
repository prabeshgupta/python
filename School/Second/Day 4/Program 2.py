grades = {
    "ram" : 85,
    "shyam": 62,
    "hari": 56,
    "ramesh": 25
    }

name = input("What is your name? ").lower()

if name in grades:
    marks = grades[name]
    if marks >= 80:
        print(f"Hi, {name.capitalize()}. Congrats, your marks is {marks} and scored Distinction")
    elif marks <80 and marks >=60:
        print(f"Hi, {name.capitalize()}. Congrats, your marks is {marks} and scored First Divison")
    elif marks <60 and marks >=50:
        print(f"Hi, {name.capitalize()}. Congrats, your marks is {marks} and scored Second Divison")
    else:
        print(f"Mom's flying chappal approaching at {marks}km/hr.")
else:
    print(f"{name.capitalize()} not found.")
