#from api import app
from flask import Flask, make_response, jsonify
from api.views.user import user_router
from flask_cors import CORS
from api.database import db
import config

def create_app():

  app = Flask(__name__)
  CORS(app)
  app.config.from_object('config.Config') # configの追加
  db.init_app(app) #configを使ってDB接続初期化　
  app.register_blueprint(user_router, url_prefix='/api') #userブループリントの追加

  return app

if __name__=='__main__':
    app = create_app()
    app.run()