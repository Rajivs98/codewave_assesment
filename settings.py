from flask import Flask
from config import Application_Config

def init(app:Flask):
    app.config.update(
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_DATABASE_URI=Application_Config.SQLALCHEMY_DATABASE_URI,
        BASE_URI=Application_Config.FLASK_APP_URI
    )