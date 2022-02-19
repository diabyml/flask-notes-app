from flask import Flask
from config import config
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

sess = Session()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # config extensions
    sess.init_app(app)
    db.init_app(app)

    # register routes
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .note import note as note_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(note_blueprint)
    
    return app