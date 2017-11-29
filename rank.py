import cherrypy
import re,json
from _kof97_database import _kof97_database

class RankController(object):
    def __init__(self, mdb = None):
        self.mdb = mdb

    def GET(self):
        output = {'result':'success'}
        try:
            output['rank'] = self.mdb.get_highest_100()
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output)

