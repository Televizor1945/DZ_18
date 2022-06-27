from flask import Flask
from flask_restx import Api

from config import Config
# from dao.model.directors import Director
# from dao.model.genres import Genre
# from dao.model.movies import Movie
from setup_db import db
from views.genres import genre_ns
from views.movies import movie_ns
from views.directors import director_ns



# функция создания основного объекта app
def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)

app = create_app(Config())
# app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
