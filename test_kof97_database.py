from _kof97_database import _kof97_database
import unittest

class TestMovieDatabase(unittest.TestCase):
        """unit tests for kof'97 ranking database"""

        #@classmethod
        #def setUpClass(self):
        kof = _kof97_database()

        def reset_data(self):
            "reset data is required because we cannot promise an order of test case execution"
            self.kof.reset_all_data()

        def test_get_player(self):
            self.reset_data()
            player = self.kof.get_player(1)
            self.assertEqual(player['name'], 'Craig Creager')
            self.assertEqual(player['score'], 2025)

        def test_get_game(self):
            self.reset_data()
            game = self.kof.get_game(1)
            self.assertEqual(game['gameID'], 1)
            self.assertEqual(game['date'], '2017-11-26')
            self.assertEqual(game['player1'], 139)
            self.assertEqual(game['score'], 25)

        def test_get_highest_100(self):
            self.reset_data()
            best = self.kof.get_highest_100()
            first = {'id': 88, 'name': 'Isabelle Ponce', 'score': 2149}
            last = {'id': 8, 'name': 'Victoria Bilderback', 'score': 2049}
            self.assertEqual(best[1], first)
            self.assertEqual(best[100], last)

        def test_add_player(self):
            self.reset_data()
            self.kof.add_player('Tong', 23)
            player = self.kof.get_player(10001)
            self.assertEqual(player['name'], 'Tong')
            self.assertEqual(player['score'], 2000)

        def test_record_game(self):
            self.reset_data()
            self.kof.record_game(2000, 2001, 1)
            game = self.kof.get_game(1001)
            self.assertEqual(game['gameID'], 1001)
            self.assertEqual(game['player1'], 2000)
            self.assertEqual(game['score'], 25)
            player1 = self.kof.get_player(2000)
            self.assertEqual(player1['score'], 2025)
            player2 = self.kof.get_player(2001)
            self.assertEqual(player2['score'], 1975)

        def test_write_to_files(self):
            self.reset_data()
            self.kof.record_game(2000, 2001, 1)
            self.kof.write_to_files()
            self.kof.load_files('data_saved/')
            game = self.kof.get_game(1001)
            self.assertEqual(game['gameID'], 1001)
            self.assertEqual(game['player1'], 2000)
            self.assertEqual(game['score'], 25)
            player1 = self.kof.get_player(2000)
            self.assertEqual(player1['score'], 2025)
            player2 = self.kof.get_player(2001)
            self.assertEqual(player2['score'], 1975)

if __name__ == "__main__":
    unittest.main()
