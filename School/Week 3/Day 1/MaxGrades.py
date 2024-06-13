#Topper Name

from cmath import inf

grades = {
    "A":93,
    "B": 40,
    "C": 44,
    "D": 93,
    "E": 63,
    "F": 93
}

def top(grades):
    temp = float(-inf)
    names = []
    for val in grades.values():
      if val > temp:
         temp = val
        
    [names.append(key) for key, val in grades.items() if val == temp]
    return names

print(top(grades))