from datetime import datetime

from flask_login.mixins import UserMixin

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

Base = declarative_base()


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.now,
                        onupdate=datetime.now)

    def __repr__(self):
        return '<User(\'{}\', \'{}\', \'{}\')>'.format(
            self.email, self.password, self.name)


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
