# KOF'97 Ranking System

The purpose of King of Fighters '97 ranking system is to keep track of the result of each game and generate an updated ranking score for all registered players. Other than normal getting functions. Users can register new players, add new games, delete existing games and get the rank. When a new player is added, he or she will have a initial score of 2000. When a new game and its result is added to the database, these two players' ranking score will be updated accordingly. Similarly for game deletions. With the ranking function, users can see the information of the best 100 player in the system. Our database initially have 10000 players and 1000 games happened among the first 500 players as original data. To avoid data-loss, we have a function that can save all current database information to files so that we can load them if the server is closed and reopened. We also have the original data saved separately in case we want to reset the database.

## Stored Data

Data are stored in two different folders: data_original and data_saved. data_saved is empty at the first time and data_original saves all of the original data.

### Data format

players.csv:
PlayerID, PlayerName, PlayerAge

games.csv:
GameID, Date, Player1ID, Player2ID, Result

scores.csv
PlayerID, RankingScore

Note: in game.csv, Result is a integer that saves the score change of the two players. After this game is recorded, player1 will add this number to his ranking score and player2 will subtract this number to his ranking score.


## Authors

Tong Zhao, tzhao2
Songcheng Dai, sdai2

## Versioning

We use GitHub and SemVer