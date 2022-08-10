from flask_pymongo import PyMongo
from flask_mail import Mail
from apscheduler.schedulers.background import BackgroundScheduler

mongo = PyMongo()
mail = Mail()
scheduler = BackgroundScheduler()
