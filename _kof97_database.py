#Tong Zhao, tzhao2
#Songcheng Dai, sdai2

class _kof97_database:
	"""A database that records a ranking system for King of Fighters '97"""
	def __init__(self):
		self.players 	= dict()
		self.games 		= dict()
		self.scores 	= dict()

	def load_files(self, filePath):
		"""Load the records from files"""
		pass
		
	def get_score(self, playerID):
		"""Returns the ranking score of a player"""
		pass

	def record_game(self, player1ID, player2ID, winner):
		"""Record a game"""
		score = cal_score(player1ID, player2ID, winner)

	def cal_score(self, player1ID, player2ID, winner):
		"""Calculate the score change of this game"""
		pass