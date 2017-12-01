import unittest
import requests
import json

class TestReset(unittest.TestCase):

    PORT_NUM = '51024'
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    RESET_URL = SITE_URL + '/reset/'
    PLAYERS_URL = SITE_URL + '/players/'
    GAMES_URL = SITE_URL + '/games/'
    RANK_URL = SITE_URL + '/rank/'
    SAVE_URL = SITE_URL + '/save/'
    LOAD_URL = SITE_URL + '/load-saved/'

    def reset_data(self):
        """Reset all data to original data"""
        m = {}
        r = requests.put(self.RESET_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_get_all_players(self):
        """Testing get all players"""
        self.reset_data()
        r = requests.get(self.PLAYERS_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        players = resp['players']
        for player in players:
            if player['id'] == 10:
                testplayer = player

        self.assertEqual(testplayer['name'], 'Karen Washington')
        self.assertEqual(testplayer['age'], 75)
        self.assertEqual(testplayer['score'], 2000)

    def test_get_player(self):
        """Testing get a single players"""
        self.reset_data()
        player_id = 10
        r = requests.get(self.PLAYERS_URL + str(player_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        self.assertEqual(resp['name'], 'Karen Washington')
        self.assertEqual(resp['age'], 75)
        self.assertEqual(resp['score'], 2000)

    def test_post_player(self):
        """testing of registering a player to the database"""
        self.reset_data()
        m = {}
        m['name'] = 'Tong'
        m['age'] = 23
        r = requests.post(self.PLAYERS_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        player_id = resp['id']

        r = requests.get(self.PLAYERS_URL + str(player_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        self.assertEqual(resp['name'], 'Tong')
        self.assertEqual(resp['age'], 23)
        self.assertEqual(resp['score'], 2000)

    def test_get_all_games(self):
        """Testing get all games"""
        self.reset_data()
        r = requests.get(self.GAMES_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        games = resp['games']
        for game in games:
            if game['gameID'] == 10:
                testgame = game

        self.assertEqual(testgame['player1'], 363)
        self.assertEqual(testgame['player2'], 250)
        self.assertEqual(testgame['score'], -25)

    def test_get_game(self):
        """Testing get a game"""
        self.reset_data()
        gameID = 10
        r = requests.get(self.GAMES_URL + str(gameID))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        self.assertEqual(resp['player1'], 363)
        self.assertEqual(resp['player2'], 250)
        self.assertEqual(resp['score'], -25)

    def test_delete_game(self):
        """Testing of deleting a game record"""
        self.reset_data()
        gameID = 10
        m = {}
        r = requests.delete(self.GAMES_URL + str(gameID), data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        #after deleting the game, result should be error when geting it again
        r = requests.get(self.GAMES_URL + str(gameID))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'error')

    def test_post_game(self):
        """testing of posting a game record to the database"""
        self.reset_data()
        m = {}
        m['player1'] = 3000
        m['player2'] = 3001
        m['result'] = 2
        r = requests.post(self.GAMES_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        gameID = resp['gameID']
        #checking if the game record exist
        r = requests.get(self.GAMES_URL + str(gameID))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['player1'], 3000)
        self.assertEqual(resp['player2'], 3001)
        self.assertEqual(resp['score'], -25)
        #checking the ranking score change of the two players
        #player1
        player_id = 3000
        r = requests.get(self.PLAYERS_URL + str(player_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['score'], 1975)
        #player2
        player_id = 3001
        r = requests.get(self.PLAYERS_URL + str(player_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['score'], 2025)

    def test_rank(self):
        """Testing of geting the 100 players with highest ranking scores"""
        self.reset_data()
        r = requests.get(self.RANK_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        #checking the players with rank 1 and 50
        players = resp['rank']
        testplayer1 = players['1']
        testplayer2 = players['50']
        self.assertEqual(testplayer1['id'], 88)
        self.assertEqual(testplayer1['name'], 'Isabelle Ponce')
        self.assertEqual(testplayer1['score'], 2149)
        self.assertEqual(testplayer2['id'], 445)
        self.assertEqual(testplayer2['name'], 'Jose Garza')
        self.assertEqual(testplayer2['score'], 2074)

    def test_save_and_load(self):
        """Testing of saving current records to files and load them"""
        #register a new player
        self.reset_data()
        m = {}
        m['name'] = 'Tong'
        m['age'] = 23
        r = requests.post(self.PLAYERS_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        player_id = resp['id']

        #post a game record
        m = {}
        m['player1'] = 3000
        m['player2'] = 3001
        m['result'] = 2
        r = requests.post(self.GAMES_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        gameID = resp['gameID']

        #save current database to files and reload from saved data
        m = {}
        r = requests.put(self.SAVE_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.put(self.LOAD_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        #check if the player record still exist
        r = requests.get(self.PLAYERS_URL + str(player_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['name'], 'Tong')
        self.assertEqual(resp['age'], 23)
        self.assertEqual(resp['score'], 2000)
        #check if the game record still exist
        r = requests.get(self.GAMES_URL + str(gameID))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['player1'], 3000)
        self.assertEqual(resp['player2'], 3001)
        self.assertEqual(resp['score'], -25)
        #checking the ranking score change of the two players in the game record
        #player1
        player_id = 3000
        r = requests.get(self.PLAYERS_URL + str(player_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['score'], 1975)
        #player2
        player_id = 3001
        r = requests.get(self.PLAYERS_URL + str(player_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['score'], 2025)


if __name__ == "__main__":
    unittest.main()

