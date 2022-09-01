import atexit
from flask import Flask
from configPack import mongo, scheduler
from models.utils.Scheduler import scrapDaily
from flask_restful import Api
from flask_cors import CORS
import os
from configPack import mail
from routes import initialize_routes


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
mongo.init_app(app)
mail.init_app(app)
api = Api(app)
initialize_routes(api)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
scheduler.add_job(func=scrapDaily, trigger="interval",
                  seconds=int(os.environ["SCRAPING_HOURS"]))
scheduler.start()
atexit.register(lambda: scheduler.shutdown())
if __name__ == '__main__':
    app.run()
