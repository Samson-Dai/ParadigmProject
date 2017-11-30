import cherrypy
import re,json
from _kof97_database import _kof97_database

class PlayersController(object):
    def __init__(self, mdb = None):
        self.mdb = mdb

    def GET(self): 
        output = {'result':'success'}
        try:
            entities = self.mdb.get_all_players()
            output['players'] = entities
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output)

    def POST(self):
        output = {'result':'success'}
        body_input = cherrypy.request.body.read().decode('utf8')  # Use decode to convert into string 
        body_input = json.loads(body_input)
        try:
            name =  body_input['name']
            age =  body_input['age']
            uid = self.mdb.add_player(name, age)
            if (uid):
                output["id"] = uid
            else:
                output['result'] = 'error'
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output)


    def GET_A_PLAYER(self,uid):
        output = {'result':'success'}
        try:
            uid = int(uid)
            output['id'] = uid
            user_info = self.mdb.get_player(uid)
            if user_info != None:
                output['name'] = user_info['name']
                output['age'] = user_info['age']
                output ['score'] = user_info['score']
            else:
                output['result'] = 'error'
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output)
