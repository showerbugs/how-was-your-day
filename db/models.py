from datetime import datetime
from flask_login.mixins import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table
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

    def unwrap_localproxy(self):
        """ flask-login current_user's type is LocalProxy

        if you want to get User(sqlalchemy-Base) type,
        you need to unwrap from LocalProxy """

        return self

    def to_json(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
        }

    def __repr__(self):
        return '<User(\'{}\', \'{}\', \'{}\')>'.format(
            self.email, self.password, self.name)


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, unique=True)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.now,
                        onupdate=datetime.now)

    owner = relationship('User', backref='team')
    users = relationship('User',
                         secondary='users_teams',
                         backref=backref('teams', lazy='dynamic'))

    def to_json(self):
        return {
            'id': self.id,
            'ownerId': self.owner_id,
            'name': self.name,
            'description': self.description,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
        }


UserTeam = Table(
    'users_teams', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('team_id', Integer, ForeignKey('teams.id')),
    Column('created_at', DateTime(timezone=True), default=datetime.now),
    Column('updated_at', DateTime(timezone=True), default=datetime.now,
           onupdate=datetime.now),
)


class Story(Base):
    __tablename__ = 'stories'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
    content = Column(String)
    published_at = Column(DateTime(timezone=True), default=datetime.now)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.now,
                        onupdate=datetime.now)

    user = relationship('User', backref='stories')
    team = relationship('Team', backref='teams')

    def to_json(self):
        return {
            'id': self.id,
            'teamId': self.user_id,
            'userId': self.team_id,
            'content': self.content,
            'publishedAt': self.published_at,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
        }
