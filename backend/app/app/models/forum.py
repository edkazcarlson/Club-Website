from typing import TYPE_CHECKING
from sqlalchemy import Table, Boolean, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

class Forum(Base):
    __tablename__ = 'forum'
    id = Column(Integer, primary_key=True, index=True)
    club = Column(Integer, ForeignKey('club.id'))


class ForumFolder(Base):
    __tablename__ = 'forumFolder'
    id = Column(Integer, primary_key=True, index=True)
    forum = Column(Integer, ForeignKey('forum.id'))
    folderName = Column(String)
    folderOrder = Column(Integer)

class ForumChannel(Base):
    __tablename__ = 'forumChannel'
    id = Column(Integer, primary_key=True, index=True)
    forumFolder = Column(Integer, ForeignKey('forumFolder.id'))
    channelName = Column(String)
    channelOrder = Column(Integer)
    requiredRank = Column(Integer)

class ForumPost(Base):
    __tablename__ = 'forumPost'
    id = Column(Integer, primary_key=True, index=True)
    channel = Column(Integer, ForeignKey('forumChannel.id'))
    writer = Column(Integer, ForeignKey('clubMember.id'))
    timeStamp = Column(Date)
    beenEdited = Column(Boolean)    
