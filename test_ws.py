import unittest
import requests
import json

class TestReset(unittest.TestCase):

    PORT_NUM = '51024'
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    RESET_URL = SITE_URL + '/reset/'
    PLAYERS_URL = SITE_URL + '/players/'

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, data = json.dumps(m))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_movies_index_get(self):
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

if __name__ == "__main__":
    unittest.main()

