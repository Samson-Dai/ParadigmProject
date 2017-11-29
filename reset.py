import cherrypy
import re,json
from _kof97_database import _kof97_database

class ResetController(object):
    def __init__(self, mdb = None):
        self.mdb = mdb

    def RESET(self):
        output = {'result':'success'}
        try:
            self.mdb.reset_all_data()
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output)

