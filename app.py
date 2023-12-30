from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from .db import init_app_
from .blueprints import product_blueprint

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Sujanix123@localhost:5432/codewave"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    init_app_(app)
    
    app.register_blueprint(product_blueprint.blueprint, url_prefix='/get')

    return app

