import cherrypy
import re,json
from _kof97_database import _kof97_database

class GamesController(object):
    def __init__(self, mdb = None):
        self.mdb = mdb

    def GET(self): 
        output = {'result':'success'}
        try:
            entities = self.mdb.get_all_games()
            output['games'] = entities
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output)

    def POST(self):
        output = {'result':'success'}
        body_input = cherrypy.request.body.read().decode('utf8')  # Use decode to convert into string 
        body_input = json.loads(body_input)
        try:
            player1 = body_input["player1"]
            player2 = body_input["player2"]
            result = body_input["result"]
            gameID = self.mdb.record_game(player1,player2,result)
            if (gameID):
                output["gameID"] = gameID
            else:
                output['result'] = 'error'
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'cannot be post'
        return json.dumps(output)


    def GET_A_GAME(self,gid):
        output = {'result':'success'}
        try:
            gid = int(gid)
            output['gameID'] = gid
            if gid in self.mdb.games:
                game_info = self.mdb.get_game(gid)
                output['date'] = game_info['date']
                output['player1'] = game_info['player1']
                output['player2'] = game_info['player2']
                output['score'] = game_info['score']
            else:
                output = {'result':'error'}
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output)

    def DELETE_A_GAME(self,gid):
        output = {'result':'success'}
        try:
            gid = int(gid)
            self.mdb.delete_game(gid)
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output)

    def OPTIONS(self, *args, **kargs):
        return ""