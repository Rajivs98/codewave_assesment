from dataclasses import dataclass
from sqlalchemy.engine.url import URL

@dataclass
class Application_Config(object):
    # SQLALCHEMY_DATABASE_URI:str = 'postgresql://postgres:Sujanix123@localhost:5432/codewave'
    postgres_uri = URL(
        drivername='postgresql',
        username='postgres',
        password='Sujanix123',
        host='db',  
        port=5432,
        database='codewave'
    )
    SQLALCHEMY_DATABASE_URI = str(postgres_uri)
    FLASK_APP_URI :str= 'http://0.0.0.0:5000'
    
