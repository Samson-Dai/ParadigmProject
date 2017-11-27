import sys
from random import randint
import names


scoresFile = open("scores.csv","w")

for i in range(1,10001):
    scoresFile.write(str(i).zfill(5))
    scoresFile.write(",2000\n")

scoresFile.close()