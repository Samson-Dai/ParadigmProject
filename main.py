import cherrypy
import re,json
from reset import ResetController
from save import SaveController
from load_saved import LoadController
from rank import RankController
from players import PlayersController
from games import GamesController
from _kof97_database import _kof97_database

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"

def start_service():
    kof = _kof97_database()
    resetController = ResetController(kof)
    saveController = SaveController(kof)
    loadController = LoadController(kof)
    rankController = RankController(kof)
    playersController = PlayersController(kof)
    gamesController = GamesController(kof)

    resetController.RESET()

    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    
    # do connection here
    dispatcher.connect('reset',
        '/reset/',
        controller = resetController ,
        action = 'RESET',
        conditions = dict(method=['PUT'])
    )
    dispatcher.connect('save',
        '/save/',
        controller = saveController ,
        action = 'SAVE',
        conditions = dict(method=['PUT'])
    )
    dispatcher.connect('load_saved',
        '/load-saved/',
        controller = loadController ,
        action = 'LOAD',
        conditions = dict(method=['PUT'])
    )
    dispatcher.connect('get_rank',
        '/rank/',
        controller = rankController ,
        action = 'GET',
        conditions = dict(method=['GET'])
    )
    dispatcher.connect('get_players',
        '/players/',
        controller = playersController ,
        action = 'GET',
        conditions = dict(method=['GET'])
    )
    dispatcher.connect('add_a_player',
        '/players/',
        controller = playersController ,
        action = 'POST',
        conditions = dict(method=['POST'])
    )
    dispatcher.connect('get_a_player',
        '/players/:uid',
        controller = playersController ,
        action = 'GET_A_PLAYER',
        conditions = dict(method=['GET'])
    )
    dispatcher.connect('get_games',
        '/games/',
        controller = gamesController ,
        action = 'GET',
        conditions = dict(method=['GET'])
    )
    dispatcher.connect('add_a_game',
        '/games/',
        controller = gamesController ,
        action = 'POST',
        conditions = dict(method=['POST'])
    )
    dispatcher.connect('get_a_game',
        '/games/:gid',
        controller = gamesController ,
        action = 'GET_A_GAME',
        conditions = dict(method=['GET'])
    )
    dispatcher.connect('delete_a_game',
        '/games/:gid',
        controller = gamesController ,
        action = 'DELETE_A_GAME',
        conditions = dict(method=['DELETE'])
    )
    dispatcher.connect('options',
        '/games/:gid',
        controller = gamesController ,
        action = 'OPTIONS',
        conditions = dict(method=['OPTIONS'])
    )


    #cofiguration for server
    conf = {
        'global':{
            'server.socket_host':'student04.cse.nd.edu',
            'server.socket_port': 51024
        },
        '/':{'request.dispatch': dispatcher,
             'tools.CORS.on': True
        }
    }

    #starting the server
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config = conf)
    cherrypy.quickstart(app)


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()