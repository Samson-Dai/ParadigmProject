#Tong Zhao, tzhao2
#Songcheng Dai, sdai2
import datetime
__version__ = '1.1.1'

class _kof97_database:
	"""A database that records a ranking system for King of Fighters '97"""
	def __init__(self):
		self.players 	= dict()
		self.games 		= dict()
		self.scores 	= dict()

	def load_files(self, filePath):
		"""Load the records from files"""
		self.players = dict()
		file = open(filePath + 'players.csv')
		for line in file:
			m = line.split(",")
			self.players[int(m[0])] = [m[1], int(m[2])]
		file.close()

		self.games = dict()
		file = open(filePath + 'games.csv')
		for line in file:
			m = line.split(",")
			self.games[int(m[0])] = [m[1], int(m[2]), int(m[3]), int(m[4])]
		file.close()

		self.scores = dict()
		file = open(filePath + 'scores.csv')
		for line in file:
			m = line.split(",")
			self.scores[int(m[0])] = int(m[1])
		file.close()

	def reset_all_data(self):
		"""Reset all data to the original data. 
		
		The original data contains 10000 players and 1000 games.
		"""
		self.load_files('data_original/')

	def write_to_files(self):
		"""Write all data to the files in data_saved/ so that we can access them next time"""
		path = 'data_saved/'
		file = open(path + 'players.csv','w')
		for key in self.players:
			file.write("{},{},{}\n".format(key, self.players[key][0], self.players[key][1]))
		file.close()

		file = open(path + 'games.csv','w')
		for key in self.games:
			file.write("{},{},{},{},{}\n".format(key, 
											  self.games[key][0], 
											  self.games[key][1], 
											  self.games[key][2], 
											  self.games[key][3]))
		file.close()

		file = open(path + 'scores.csv','w')
		for key in self.scores:
			file.write("{},{}\n".format(key, self.scores[key]))
		file.close()
		
	def get_all_players(self):
		"""Returns a list of all players with their information and score"""
		output = list()
		for playerID in self.players:
			output.append(self.get_player(playerID))
		return output

	def get_all_games(self):
		"""Returns a list of all games"""
		output = list()
		for gameID in self.games:
			output.append(self.get_game(gameID))
		return output

	def get_player(self, playerID):
		"""Returns the information and score of a player"""
		if playerID in self.scores:
			output = dict()
			output['id'] = int(playerID)
			output['name'] = self.players[playerID][0]
			output['age'] = self.players[playerID][1]
			output['score'] = self.scores[playerID]
			return output
		else:
			return None

	def get_game(self, gameID):
		"""Returns the game record according to the given game ID"""
		if gameID in self.games:
			output = dict()
			output['gameID'] = int(gameID)
			output['date'] = self.games[gameID][0]
			output['player1'] = self.games[gameID][1]
			output['player2'] = self.games[gameID][2]
			output['score'] = self.games[gameID][3]
			return output
		else:
			return None

	def get_highest_100(self):
		"""Returns the information and score of best 100 players"""
		sortedscores = list()
		best100 = dict()
		sortedscores = list(sorted(self.scores, key = self.scores.__getitem__, reverse = True))
		for i in range(100):
			rank = i + 1
			best100[rank] = self.get_player(sortedscores[i])
		return best100

	def add_player(self, name, age):
		"""Add a new player to the database and set default ranking score of 2000"""
		playerID = 1
		if len(self.players.keys()) > 0:
			playerID = max(self.players.keys()) + 1
		self.players[playerID] = [name, int(age)]
		self.scores[playerID] = 2000
		return playerID

	def record_game(self, player1ID, player2ID, winner):
		"""Record a game and change the scores of two players according to the game result.
		
		A record will be saved to self.games and the ranking scores of the two players 
		will be updated.
		"""
		if player1ID in self.scores and player2ID in self.scores:
			now = datetime.datetime.now()
			score = self.cal_score(player1ID, player2ID, winner)
			gameID = 1
			if len(self.games.keys()) > 0:
				gameID = max(self.games.keys()) + 1
			self.games[gameID] = [str(now)[:10], player1ID, player2ID, score]
			self.scores[player1ID] = self.scores[player1ID] + score
			self.scores[player2ID] = self.scores[player2ID] - score
			return gameID
		else:
			return None

	def cal_score(self, player1ID, player2ID, winner):
		"""A helper function that calculate the score change of this game.

		When the ranking score of winner is higher than the ranking score of loser,
			the result score will be smaller according to the difference of their
			ranking score.
		When the ranking score of winner is lower than the ranking score of loser,
			the result score will be larger according to the difference of their
			ranking score.
		"""
		score1 = self.scores[player1ID]
		score2 = self.scores[player2ID]
		diff = int((score1 - score2) / 100)
		if diff > 10:
			diff = 10
		if diff < -10:
			diff = -10
		if winner == 1:
			return 25 - diff
		else:
			return -25 - diff

	def delete_game(self, gameID):
		"""If this game does exist, delete this game record 
		and change the corresponding ranking scores"""
		if gameID in self.games:
			player1ID = self.games[gameID][1]
			player2ID = self.games[gameID][2]
			scoreChange = self.games[gameID][3]
			del self.games[gameID]
			self.scores[player1ID] = self.scores[player1ID] - scoreChange
			self.scores[player2ID] = self.scores[player2ID] + scoreChange


if __name__ == '__main__':
	kof = _kof97_database()
	kof.reset_all_data()
	kof.add_player("tong", 23)
	kof.write_to_files()
	pass