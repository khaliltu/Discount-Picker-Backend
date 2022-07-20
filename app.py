from distutils.command.config import config
import imp
from flask import Flask
from configPack import mongo
from resources.routes import initialize_routes
from flask_restful import Api
from flask_cors import CORS
import os
from configPack import mail


app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/discount-picker"
app.config.from_object(os.environ['APP_SETTINGS'])
mongo.init_app(app)
mail.init_app(app)
api = Api(app)
initialize_routes(api)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run()
