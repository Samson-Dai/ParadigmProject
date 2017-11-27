#Tong Zhao, tzhao2
#Songcheng Dai, sdai2
import datetime


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

		self.games = dict()
		file = open(filePath + 'games.csv')
		for line in file:
			m = line.split(",")
			#self.games[int(m[0])] = [m[1], int(m[2]), int(m[3]), int(m(4))]
			self.games[int(m[0])] = [m[1], int(m[2]), int(m[3]), int(m[4])]

		self.scores = dict()
		file = open(filePath + 'scores.csv')
		for line in file:
			m = line.split(",")
			self.scores[int(m[0])] = int(m[1])

	def reset_all_data(self):
		"""Reset all data to the original data, which contains no game records 
		and all players have score of 2000
		"""
		self.load_files('data_original/')

	def write_to_files(self):
		"""Write all data to the files in data_saved/ so that we can access them next time"""
		pass
		
	def get_score(self, playerID):
		"""Returns the ranking score of a player"""
		if playerID in self.scores:
			output = dict()
			output['id'] = int(playerID)
			output['name'] = self.players[playerID][0]
			output['score'] = self.scores[playerID]
			return output
		else:
			return None

	def get_game(self, gameID):
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
		"""Returns the info and score of best 100 players"""
		sortedscores = list()
		best100 = dict()
		sortedscores = list(sorted(self.scores, key = self.scores.__getitem__, reverse = True))
		for i in range(100):
			rank = i + 1
			best100[rank] = self.get_score(sortedscores[i])
		return best100

	def record_game(self, player1ID, player2ID, winner):
		"""Record a game and change the scores of two players accroding to the game result"""
		if player1ID in self.scores and player2ID in self.scores:
			now = datetime.datetime.now()
			score = self.cal_score(player1ID, player2ID, winner)
			if len(self.games.keys()) > 0:
				gameID = max(self.games.keys()) + 1
			else:
				gameID = 1
			self.games[gameID] = [str(now)[:10], player1ID, player2ID, score]
			self.scores[player1ID] = self.scores[player1ID] + score
			self.scores[player2ID] = self.scores[player2ID] - score
		else:
			return None

	def cal_score(self, player1ID, player2ID, winner):
		"""Calculate the score change of this game"""
		score1 = self.scores[player1ID]
		score2 = self.scores[player2ID]
		diff = int((score1 - score2) / 100)
		if diff > 10:
			diff = 10
		if diff < -10:
			diff = -10
		if winner == 1:
			return 25 + diff
		else:
			return -25 + diff

if __name__ == '__main__':
	kof = _kof97_database()
	kof.load_files('data_original/')
	kof.record_game(10, 2000, 1)
	#print(kof.get_game(1), kof.get_score(20))
	print(kof.get_highest_100())