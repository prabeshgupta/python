#List is group of data. It's also known as array.

games = ['Pubg', 'Freefire', 'Mobile Legends']

#Add single element
games.append('Clash Of Clans')

print(games)

#Add multiple elements
games.extend(['Clash Royale', 'Subway Surfer'])

print(games)

'''Remove item of specified index
Default removes last element'''
games.pop(1)

print(games)

#Find index of an element
print(games.index('Pubg'))

#Copy
cpGames = games.copy()
print(cpGames)

#Length of list counts from 1
pcGames =  ['GTA 5', 'FIFA 24', 'Street Fighter 6', 'WWE 2k23']
print(len(pcGames))

#Insert element in specified index
pcGames.insert(3,'Naruto Storm 4')
print(pcGames)

#Remove element
pcGames.remove('Naruto Storm 4')
print(pcGames)

#Count number of repeated item
count =  pcGames.count('games')
print(count)

#Sort in ascending
pcGames.sort()

#Reverse in descending
pcGames.reverse()
print(pcGames)

#Clear
pcGames.clear()
print(pcGames)