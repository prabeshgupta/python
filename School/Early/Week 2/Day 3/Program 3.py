import os

for i in range(1,101,1):
    f = open(f"/home/aayushgupta/Documents/Python/School/Week 2/Day 3/File {i}.txt",'x')
    f.write(f"File {i}")

f.close()