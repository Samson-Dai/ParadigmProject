import cherrypy
import re,json
from _kof97_database import _kof97_database

class LoadController(object):
    def __init__(self, mdb = None):
        self.mdb = mdb

    def LOAD(self):
        output = {'result':'success'}
        try:
            self.mdb.load_files("data_saved/")
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output)

