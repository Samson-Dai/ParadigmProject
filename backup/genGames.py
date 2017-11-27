from _kof97_database import _kof97_database
import random

kof = _kof97_database()
kof.reset_all_data()

playerList = range(1,501)
result = [1,2]
random_generator = random.SystemRandom()
for i in range(1,1001):
    gameID = int(str(i).zfill(5))
    player1 = random_generator.choice(playerList)
    player2 = random_generator.choice(playerList)
    while (player2==player1):
        player2 = random_generator.choice(playerList)
    kof.record_game(int(str(player1).zfill(5)), int(str(player2).zfill(5)), random_generator.choice(result))

kof.write_to_files()
