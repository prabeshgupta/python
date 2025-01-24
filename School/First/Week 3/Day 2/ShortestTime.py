#Runner shortest time
from cmath import inf


with open("C:\\Users\gamerzchoices\Documents\CODING\python\School\Week 3\Day 2\\times.txt","r") as info:
    player = {}
    for data in info.readlines():
        time = data.strip().split()
        name = time[0]
        timeList = []
        for total in time[1:]:
            timeList.append(int(total))
        player[name]= sum(timeList)
    print(player)

with open("C:\\Users\gamerzchoices\Documents\CODING\python\School\Week 3\Day 2\\totals.txt","w") as race:
   temp = float(inf)
   winner = ''
   for key, val in player.items():
      race.write(f"{key}: {val}\n")
      if val < temp:
          temp = player[key]
          winner = key
   print(f"{winner}: {temp}")
      
         


      


    