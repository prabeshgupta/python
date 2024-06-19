print(not True)
print(not False)

if 10>5 and 2<3:
    print(True)

print(False) if (10>5 and 38<3) else print(True)

print(True) if (10>5 and 38>3) else print(False)

print(True) if 10<5 or 2<3 else print(False)

print(True) if 10<5 or 2>3 else print(False)


data= not True or (False and True) or (not False) or True or (not True or False and False)
print(data)
    