from sqlalchemy import  Column, Integer, String
from ..db.dbsession import Base


class User(Base):
    __tablename__ = "testusers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
