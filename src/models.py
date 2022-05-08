import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    follower = relationship('Follower', backref="profile")
    post = relationship('Post', backref="profile")
    comment = relationship('Comment', backref="profile")


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    profile_from_id= Column(Integer, ForeignKey('profile.id'))
    profile_to_id = Column(Integer, ForeignKey('profile.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    image = Column(String(250))
    text = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    profile_id = Column(Integer, ForeignKey('profile.id'))
    comment = relationship('Comment', backref="post")   

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    profile_id = Column(Integer, ForeignKey('profile.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')