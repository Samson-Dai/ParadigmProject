import sys
from random import randint
import names


playersFile = open("players.csv","w")

for i in range(1,10001):
    playersFile.write(str(i).zfill(5))
    playersFile.write(","+ names.get_full_name()+",")
    playersFile.write(str(randint(12,75)))
    playersFile.write("\n")

playersFile.close()