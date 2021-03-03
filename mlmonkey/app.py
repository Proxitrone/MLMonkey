# from __future__ import absolute_import

import flask 
from api import view
#import scheduler
#import mlmonkey.api.view
#from mlmonkey import scheduler


#scheduler = scheduler.Scheduler()
app = flask.Flask(__name__)
app.register_blueprint(view.blueprint)


def main():
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
