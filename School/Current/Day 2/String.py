#String is a sequence of characters.

greet = " Hello World"

print(len(greet))

print(greet.upper())
print(greet.lower())
print(greet.capitalize())
print(greet.title())

print(greet.replace("World", "Developer"))

print(greet.strip())

print(" ".join(greet))

print(greet.endswith("d"))

print(greet.isdigit())

print(greet.find("d"))
print(greet.index("e"))

print(greet[1:6:1])

print(greet.center(40,"x"))

info = "I am {0} {1} from {2}"
print(info.format("Prabesh","Gupta","Kathmandu"))


#Raw string
print(r"Hello\n Me")

#Multiline
multi_greet = """I am Prabesh
from Kathmandu"""
print(multi_greet)

#Fstring
game = "T20"
print(f"\"{game}\" was not so good.")


print(help(str))
