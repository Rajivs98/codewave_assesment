from dataclasses import dataclass
from sqlalchemy.engine.url import URL

@dataclass
class Application_Config(object):
    # SQLALCHEMY_DATABASE_URI:str = 'postgresql://postgres:Sujanix123@localhost:5432/codewave'

# Assuming the Docker container is linked to a PostgreSQL container named 'db'
    docker_postgres_uri = URL(
        drivername='postgresql',
        username='postgres',
        password='Sujanix123',
        host='db',  # Use the Docker service name or IP address of your PostgreSQL container
        port=5432,
        database='codewave'
    )

    SQLALCHEMY_DATABASE_URI = str(docker_postgres_uri)
    FLASK_APP_URI :str= 'http://0.0.0.0:5000'
    