def count_u(word):
    temp = 0
    for char in word.lower():
        if char == "u":
            temp +=1
    return temp

print(count_u("I love Upahar. You are so beautiful."))