from datetime import datetime

from flask_login.mixins import UserMixin

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

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


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    users = relationship('User',
                         secondary=lambda: UserTeam,
                         backref=backref('teams', lazy='dynamic'))

    def to_dict(self):
        return {
            'name': self.name,
            'users': [user.id for user in self.users],
        }


UserTeam = Table(
    'users_teams', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('team_id', Integer, ForeignKey('teams.id'))
)
