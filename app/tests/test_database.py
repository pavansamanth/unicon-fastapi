from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pytest
import logging

from ..database import get_db
from ..models import user_roles, user_table
from ..main import app
from decouple import config


# db intializations to overwrite the db

db_username = config("DB_USERNAME")
db_password = config("DB_PASSWORD")
host_server = config("HOST_SERVER")
db_server_port = config("DB_SERVER_PORT")
database_name = config("DATABASE_NAME_1")
Postgre_url = f"postgresql://{db_username}:{db_password}@{host_server}:{db_server_port}/{database_name}"


engine = create_engine(Postgre_url)


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


user_table.Base.metadata.create_all(engine)

user_roles.Base.metadata.create_all(engine)


# function to create session for the override db

def override_get_db():

    try:

        db = TestingSessionLocal()

        yield db

    finally:

        db.close()



# override the db

app.dependency_overrides[get_db] = override_get_db