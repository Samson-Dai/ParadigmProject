import cherrypy
import re,json
from _kof97_database import _kof97_database

class SaveController(object):
    def __init__(self, mdb = None):
        self.mdb = mdb

    def SAVE(self):
        output = {'result':'success'}
        try:
            self.mdb.write_to_files()
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output)

