from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_restplus import Api


app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)
api = Api(
    version='1.0',
    description='TEST API',
    doc='/docs/',
    default='mapi',
    default_label='Super API')



from application import routes

