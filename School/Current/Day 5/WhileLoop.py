#Basic while loop

i = 0
while i<10:
    print(i)
    i+=1


#Looping string

name = "Upahar Basnet"
i=0
while i < len(name):
    print(name[i])
    i+=1


#Looping through list

currencies = ["USD", "NPR", "INR", "GBP"]
i = 0
while i < len(currencies):
    print(currencies[i])
    i+=1

j = len(currencies)-1
while j >= 0:
    print(currencies[j])
    j-=1


#Looping through tuples

yt_channels = ("WWE", "Kali Uchichs", "VTEN")
i =0
while i < len(yt_channels):
    print(yt_channels[i])
    i+=1


#Looping through set
values = {1,3,6,7,4,2,3,63}
i = 0
while i < len(values):
    print(values)
    i+=1


#Looping dictionary
brand = {
    "name": "Rolce Royace",
    "model": "Ghost",
    "price": 10e7
}

i = 0
while i < len(brand):
    print(brand)
    i+=1