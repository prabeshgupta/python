#Write a program that takes user input in number and print if the number is odd or even

num = int(input("Enter a number "))

print(f"{num} is even") if num % 2 == 0 else print(f"{num} is Odd")