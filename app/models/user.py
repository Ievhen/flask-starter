from sqlalchemy import Column, sql
from sqlalchemy import Integer, String, DateTime

from .metadata import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    created_at  = Column('created_at', DateTime, server_default=sql.func.now())
    modified_at = Column('modified_at', DateTime, server_default=sql.func.now(), onupdate=sql.func.current_timestamp())
    login = Column('login', String, nullable=False, unique=True)
    password =  Column('password', String, nullable=False)
