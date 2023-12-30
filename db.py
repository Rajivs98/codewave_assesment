from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from contextlib import contextmanager

db = SQLAlchemy()
migrate = Migrate()


def init_app_(app):
    db.init_app(app)
    migrate.init_app(app, db)
    
