from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from decouple import config

database_username = config("DB_USERNAME")
database_password = config("DB_PASSWORD")
host_server = config("HOST_SERVER")
server_port = config("DB_SERVER_PORT")
database_name = config("DATABASE_NAME")

Postgre_url = f"postgresql://{database_username}:{database_password}@{host_server}:{server_port}/{database_name}"

engine = create_engine(Postgre_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
