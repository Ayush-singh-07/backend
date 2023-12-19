from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_SERVER = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "test"

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
