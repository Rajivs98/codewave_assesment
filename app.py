from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from .db import init_app_
from .blueprints import product_blueprint

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:Rajiv123@172.18.0.3:5432/codewave_test_db"
    init_app_(app)
    app.register_blueprint(product_blueprint.blueprint, url_prefix='/get')

    return app

