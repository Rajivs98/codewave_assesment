from dataclasses import dataclass
from sqlalchemy.engine.url import URL

@dataclass
class Application_Config(object):
    # SQLALCHEMY_DATABASE_URI:str = 'postgresql://postgres:Sujanix123@localhost:5432/codewave'

    postgres_uri = URL(
        drivername='postgresql',
        username='root',
        password='Rajiv321',
        host='172.18.0.3',  
        port=5432,
        database='codewave_test_db'
    )

    SQLALCHEMY_DATABASE_URI = str(postgres_uri)
    FLASK_APP_URI :str= 'http://0.0.0.0:5000'
    
